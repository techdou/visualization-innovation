#!/usr/bin/env python3
"""Validate and export one skill with its frontmatter name as the ZIP root."""
import argparse, subprocess, sys, tempfile, zipfile
from pathlib import Path
import yaml

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root',nargs='?',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('destination',nargs='?',type=Path)
    p.add_argument('--output',type=Path)
    a=p.parse_args();root=a.root.resolve();out=a.output or a.destination
    if out is None: p.error('Provide destination or --output')
    out=out.resolve()
    if out.is_relative_to(root): p.error('Output must be outside the skill directory')
    if out.exists(): p.error('Output exists; choose a new path')
    check=subprocess.run([sys.executable,str(root/'scripts/validate_skill.py'),str(root)])
    if check.returncode: return check.returncode
    name=yaml.safe_load((root/'SKILL.md').read_text().split('---',2)[1])['name']
    out.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=out.parent,suffix='.zip',delete=False) as f: temp=Path(f.name)
    try:
        with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as z:
            for item in sorted(root.rglob('*')):
                if not item.is_file() or item.is_symlink() or item.suffix in {'.pyc','.pyo','.zip'} or '__pycache__' in item.parts or item.name in {'.DS_Store','Thumbs.db'}: continue
                z.write(item,str(Path(name)/item.relative_to(root)))
        with zipfile.ZipFile(temp) as z:
            if z.testzip(): raise ValueError('ZIP integrity failure')
        temp.replace(out);print(out)
    finally: temp.unlink(missing_ok=True)
    return 0
if __name__=='__main__': sys.exit(main())
