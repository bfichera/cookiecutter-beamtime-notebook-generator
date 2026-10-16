# cookiecutter-beamtime-notebook-generator

People at user facilities love jupyter notebooks. They're only human.

This is a snakemake project where you---the Enlightened---write code in .py
files, with parameters templated with jinja2 and injected at build time. The
result is a collection of .ipynb files (one for each run number) that are ready
to execute.

## Usage

1. `cookiecutter gh:bfichera/cookiecutter-beamtime-notebook-generator.git`
2. Configure run numbers in `config/analyses.yaml`
3. Write `.py.j2` files in `workflow/notebooks`
4. run `make` and be merry
