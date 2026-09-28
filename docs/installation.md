# Installation and local checks

Use a host Agent that supports SKILL.md skills and local Python execution.
The helpers require Python 3.9 or later and only its standard library.

Download [looksift-2.0.zip](https://github.com/lzhfirst/looksift/releases/download/v2.0.0/looksift-2.0.zip)
and install its complete looksift folder using your host's supported skill
installation mechanism. This runtime ZIP excludes the repository homepages,
case pages, example images, maintenance documents and tests. GitHub's automatic
Source code archives and a full clone contain the entire presentation repository.
Preserve the installation folder structure:
SKILL.md must remain at the bundle root. Install the entire numbered library and
official template directory; copying only the entry file is insufficient.
Configure the host's skill location rather than embedding your machine path in
this repository. Reload the skill after installing an update.

Start with a request such as “Use Looksift to write a prompt for a mountain lake.”
The Agent asks for unresolved choices and returns usable prompts. You can select
a style number at [Looksift](https://looksift.com), or use a reference when you
later generate the image. This skill does not generate images itself.

From the bundle root, check one exact numbered record with Python:

    python skills/looksift/scripts/lookup_style.py 1813

For development checks, clone the repository. Its preference test suite is not
part of the installation ZIP and creates isolated profiles and subprocesses.
From the repository root, prepare its ignored temporary directory, then run:

    python -c "from pathlib import Path; Path('tmp').mkdir(exist_ok=True)"
    python -m unittest discover -s tests -p test_looksift_preferences.py -v

Do not commit tmp or any generated database. For shared machines, configure a
reliable per-user profile according to the [preference guide](../skills/looksift/references/user-preferences.md).
Uninstalling or replacing this bundle does not automatically delete separately
stored preferences. No cross-host or cloud synchronization is provided.
