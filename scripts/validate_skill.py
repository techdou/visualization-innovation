#!/usr/bin/env python3
"""Validate structure, not task quality. Requires PyYAML; no network or writes."""
import argparse, re, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    raise SystemExit('Install PyYAML to validate YAML safely.')

def validate(root):
    errors=[]; warnings=[]
    manifest=root/'SKILL.md'
    if not manifest.is_file(): return ['Missing root SKILL.md'],warnings
    text=manifest.read_text(encoding='utf-8')
    match=re.match(r'^---\r?\n(.*?)\r?\n---(?:\r?\n|$)',text,re.S)
    fm=None
    if not match: errors.append('Missing YAML frontmatter')
    else:
        try: fm=yaml.safe_load(match.group(1))
        except yaml.YAMLError as e: errors.append('Invalid YAML: '+str(e))
    if not isinstance(fm,dict): errors.append('Frontmatter must be a mapping')
    else:
        name=fm.get('name'); description=fm.get('description')
        if not isinstance(name,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) or len(name)>64:
            errors.append('Invalid name')
        elif root.name != name and not re.fullmatch(r'skill-[a-zA-Z0-9]+',root.name):
            errors.append('Portable directory must match name; managed skill-ID directories are allowed locally')
        if not isinstance(description,str) or not 1<=len(description.strip())<=1024:
            errors.append('description must be a nonempty string of at most 1024 characters')
        extra=set(fm)-{'name','description'}
        if extra: warnings.append('This authoring profile uses only name/description; extra fields: '+str(sorted(extra)))
    if len(text.splitlines())>500: warnings.append('Main instructions exceed recommended 500 lines')
    files=[p for p in root.rglob('*') if p.is_file()]
    if len([p for p in files if p.name.lower()=='skill.md'])!=1: errors.append('Expected one SKILL.md')
    for p in files:
        if p.is_symlink(): errors.append('Symlink not portable: '+str(p.relative_to(root)))
        if p.suffix in {'.pyc','.pyo'} or '__pycache__' in p.parts: warnings.append('Generated cache: '+str(p.relative_to(root)))
        if p.suffix=='.md':
            content=p.read_text(encoding='utf-8')
            refs=set(re.findall(r'`((?:references|assets|scripts)/[^`\s]+)`',content))
            refs.update(re.findall(r'\]\(((?:references|assets|scripts)/[^)\s]+)\)',content))
            for ref in refs:
                target=(root/ref.split('#')[0]).resolve()
                if not target.is_relative_to(root): errors.append('Out-of-bundle reference: '+ref)
                elif not target.exists(): errors.append(str(p.relative_to(root))+': missing '+ref)
    for p in (root/'references').glob('*.md'):
        if 'references/'+p.name not in text: warnings.append('Reference not directly routed: '+p.name)
    meta=root/'agents/openai.yaml'
    if meta.exists():
        try:
            data=yaml.safe_load(meta.read_text()); interface=data['interface']
            if not 25<=len(interface['short_description'])<=64: errors.append('UI short_description must be 25–64 chars')
            if isinstance(fm,dict) and '$'+str(fm.get('name')) not in interface['default_prompt']: errors.append('UI default_prompt must name the skill')
        except (yaml.YAMLError,KeyError,TypeError): errors.append('Invalid agents/openai.yaml')
    return errors,warnings

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',nargs='?',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args()
    try: errors,warnings=validate(a.root.resolve())
    except (OSError,UnicodeError) as e: errors,warnings=[str(e)],[]
    print(json_result(a.root,errors,warnings))
    return int(bool(errors))
def json_result(root,errors,warnings):
    import json
    return json.dumps({'skill':root.name,'errors':errors,'warnings':warnings},ensure_ascii=False)
if __name__=='__main__': sys.exit(main())
