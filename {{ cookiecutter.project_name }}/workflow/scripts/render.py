import argparse
from pathlib import Path

from jinja2 import Environment, StrictUndefined


parser = argparse.ArgumentParser()
parser.add_argument("template", type=Path)
parser.add_argument("output", type=Path)
parser.add_argument("run", type=int)
args = parser.parse_args()

environment = Environment(
    undefined=StrictUndefined,
    keep_trailing_newline=True,
)
template = environment.from_string(args.template.read_text())
args.output.write_text(template.render(run=args.run))
