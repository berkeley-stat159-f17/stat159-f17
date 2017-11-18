#!/usr/bin/env python
"""Copy data files to final html directory.
"""

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

import os
import sys

from os.path import join as pjoin

#-----------------------------------------------------------------------------
# Config
#-----------------------------------------------------------------------------

VERBOSE = False
#VERBOSE = True

# Directory with source files
src_dir = '.'
# Directory where final html tree is built - set in the Makefile
out_dir = '_build/html'

# Prefix of directories to skip (set when sphinx-quickstart was run)
skip_prefix = '_'
skip_extensions = {'.rst', '.tex'}

# Other directory trees to skip

# Any top-level files that may need to be copied as well
top_files = []

# Update with info from sphinx conf.py
sphinx_conf = {}
exec(open('conf.py').read(), {}, sphinx_conf)
skip_trees = {'.git', '.ipynb_checkpoints', 'misc'}

# Always skip source files, since shpinx already copies those
if 'source_suffix' in sphinx_conf:
    skip_extensions.update(sphinx_conf['source_suffix'])

# And skip anything sphinx would too
if 'exclude_patterns' in sphinx_conf:
    xp = sphinx_conf['exclude_patterns']
    skip_trees.update(p.replace('*', '') for p in xp)


#-----------------------------------------------------------------------------
# Functions
#-----------------------------------------------------------------------------

def print(*a, **k):
    import builtins

    if VERBOSE:
        builtins.print(*a, **k)


def keep_filename(f, skip_ext=skip_extensions):
    """Return whether to keep a file based on a list of extensions.

    Note that filenames ending in ~ are always excluded."""

    if f.endswith('~'):
        return False

    return os.path.splitext(f)[1] not in skip_ext


def copy_files(root, files):
    did_copy = False
    for fname in files:
        target = pjoin(out_dir, root, fname)
        if not (os.path.isfile(target) or os.path.islink(target)):
            print(target, end='')
            os.link(pjoin(root, fname), target)
            did_copy = True
    if did_copy:
        print()


def main():
    if not os.path.isdir(out_dir):
        err = 'ERROR: Output directory {0} not found.'.format(out_dir)
        print(err, file=sys.stderr)
        sys.exit(1)

    #skip_base = pjoin(src_dir, skip_prefix)

    for root, dirs, files in os.walk(src_dir, followlinks=True):
        dirs.sort()
        print('root', root)

        if root == src_dir:
            # Only from the top, remove subdirs starting with skip prefix
            dirs[:] = [d for d in dirs if not
                       (d.startswith(skip_prefix) or d in skip_trees)]
            print('top-level dirs:', dirs)
            #continue

        files = [ f for f in (filter(keep_filename, files)) 
                  if f not in skip_trees ]

        print('  dirs:', dirs)
        print('   files:', files)
        # Now, create the list of subdirs and files in the output
        for subdir in dirs:
            new_dir = pjoin(out_dir, root, subdir)
            if not os.path.isdir(new_dir):
                print("Making dir:", new_dir)
                os.mkdir(new_dir)

        if root == src_dir:
            # Only copy files for subdirs, not for the top-level (so we don't
            # copy makefiles and stuff like that)
            copy_files(root, set(top_files) & set(files))

        copy_files(root, files)

#-----------------------------------------------------------------------------
# Execute as a script
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
