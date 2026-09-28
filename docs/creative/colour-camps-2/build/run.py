import sys, asyncio, importlib
sys.path.insert(0, "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/sets3")
import core
mod=importlib.import_module(sys.argv[1]); cmd=sys.argv[2] if len(sys.argv)>2 else "render"
only=sys.argv[3].split(",") if len(sys.argv)>3 and sys.argv[3] else None
fmts=tuple(sys.argv[4].split(",")) if len(sys.argv)>4 else ("feed","story")
bad=core.gate(mod); print("stock gate:", "PASS" if not bad else bad)
asyncio.run(core.render(mod, only, fmts)); print("rendered")
