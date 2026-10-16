# cookiecutter-beamtime-notebook-generator

People at user facilities love jupyter notebooks. They're only human.

This is a snakemake project where you---the Enlightened---write code in .py
files, with parameters templated with jinja2 and injected at build time. The
result is a collection of .ipynb files (one for each run number) that are ready
to execute.
