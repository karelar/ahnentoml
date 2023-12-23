# Ahnentoml

Python library for an experimental genealogy research format - the goal is to let the researcher author TOML files
that describe individuals, scanned images, other sources, etc, and provide a format to validate, query, and transform
them to be consumed or shared in other ways.

Project name comes from https://en.wikipedia.org/wiki/Ahnentafel and TOML.

### Local development
To build locally from source:
1. First, optionally activate a venv
2. Next, build and install the package, using `pip install .`. This can also be done as `pip install -e .` to allow
   editing sources without needing a reinstall.

### Simple usage
After installation, a few commands are available to run from Python, in a directory that already contains a collection
of TOML files.

#### `python -m ahnentoml.validate_id [REFERENCE]...`
Reads a referenced entities based on their type and ID, and validates that the file can be correctly read. At this time,
this only checks if the ID points to a file, the file is not empty, and the TOML syntax is valid.

#### `python -m ahnentoml.validate_all`
Like validate_id, except reads the entire collection.

#### `python -m ahnentoml.collection`
Reads a collection and validates syntax, references between files.

### Genealogy TOML format
TODO - this is a work in progress.
