#!/usr/bin/env python
# https://github.com/jethrokuan/braindump/blob/master/build.py

import glob
from pathlib import Path
#  command = emacs --batch -l init.el -l publish.el --eval \'(jethro/publish \\"$in\\")'
files = glob.glob("./references/notes/*.org")

with open("build.ninja", "w") as ninja_file:
    ninja_file.write(
        """
rule org2md
  command = emacs --batch -l init.el -l publish.el --eval \'(boyang/publish \"$in\")\'
  description = org2md $in
"""
    )

    for f in files:
        path = Path(f)
        output_file = f"~/personalblog/content/notes/{path.with_suffix('.md').name}"
        ninja_file.write(
            f"""
build {output_file}: org2md {path}
"""
        )

import subprocess

subprocess.call(["ninja"])
