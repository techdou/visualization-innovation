#!/usr/bin/env python3
"""Copy the canonical brief template without overwriting an existing file."""
import argparse
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('title',nargs='?',default='Visualization Innovation Brief');p.add_argument('output',nargs='?',type=Path,default=Path('innovation-brief.md'))
    a=p.parse_args();root=Path(__file__).resolve().parents[1]
    text=(root/'assets'/'innovation-brief-template.md').read_text(encoding='utf-8')
    text='# '+a.title+'\n'+text.split('\n',1)[1]
    try:
        with a.output.open('x',encoding='utf-8') as f: f.write(text)
    except OSError as e: p.error(str(e))
    print(a.output.resolve())
if __name__=='__main__':main()
