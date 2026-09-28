#!/usr/bin/env python3
"""Diagnostic candidate triage. JSON: {candidate: {criterion: 0..4 or null}}."""
import argparse, json, math, sys
from pathlib import Path
GATES=('task_fit','evidence_gain','perceptual_clarity','scientific_honesty')
OPTIONAL=('innovation','interaction_value','coordination_value','story_coherence','learnability','scalability','implementability','evaluation_tractability','reproducibility','prior_art_separation')
CRITERIA=GATES+OPTIONAL

def assess(data):
    if not isinstance(data,dict) or not data: raise ValueError('Input must be a nonempty candidate object')
    rows=[]
    for name,scores in data.items():
        if not isinstance(name,str) or not name.strip() or not isinstance(scores,dict): raise ValueError('Candidate needs a name and score object')
        unknown=set(scores)-set(CRITERIA)
        if unknown: raise ValueError(f'{name}: unknown criteria {sorted(unknown)}')
        for key,value in scores.items():
            if value is not None and (isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or not 0<=value<=4): raise ValueError(f'{name}.{key}: use finite numeric 0–4 or null')
        failed=[g for g in GATES if scores.get(g) is not None and scores[g]<2]
        missing=[g for g in GATES if scores.get(g) is None]
        status='reject' if failed else 'hold' if missing else 'eligible'
        values=[v for v in scores.values() if v is not None]
        rows.append({'name':name,'status':status,'failed_gates':failed,'unknown_gates':missing,'scored_dimensions':len(values),'diagnostic_mean':round(sum(values)/len(values),3) if status=='eligible' else None})
    # Deliberately avoid an automatic ranking: partial score sets are not comparable.
    return {'notice':'Assessor judgments, not empirical validation or a winner ranking. Gate pass is provisional.','candidates':rows}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try: result=assess(json.loads(a.input.read_text(encoding='utf-8')))
    except (OSError,ValueError,TypeError) as e: print('ERROR: '+str(e),file=sys.stderr);return 2
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0
if __name__=='__main__':sys.exit(main())
