"""Update only the experiment_runner-owned handoff block."""
import sys
from pathlib import Path
p=Path('STATE.md');text=p.read_text();a='<!-- NEURICO_AGENT_NOTES_START:experiment_runner -->';b='<!-- NEURICO_AGENT_NOTES_END:experiment_runner -->'
p.write_text(text.split(a)[0]+a+'\n'+sys.argv[1]+'\n'+b+text.split(b)[1])
