# KTH Demos

This repository contains examples and demonstration code which you can build from
in your own work.

To add an example, please create a new subfolder and file for the example, and a
README.md in the root of the subfolder describing the demonstration.

Examples should be a simple as possible with as few dependencies as possible
to demonstrate functionality.  If data is required, please supply a small data
sample which works for the demo.

## Jupyter Notebooks in git

Make sure not to commit data inadvertently if working with jupyter notebooks. 
Suggest using `nbstripout` to automatically strip output.

Install git hooks to filter notebooks when committing to git:

`pip install nbstripout`
`cd /path/to/git-repo nbstripout --install`