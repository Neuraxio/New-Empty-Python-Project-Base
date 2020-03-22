# [New Empty Python Project Base](https://github.com/Neuraxio/New-Empty-Python-Project-Base)

> This is just what you need to start a new Python project.

Simply use this project template to start new python projects.

## How to use it

1. Fork or clone this repo, and rename the `project/` folder (and all references to this folder in other files) to customize your project name that is currently named `project` as per the folder's name. You'll also want to rename the repository.
2. You can run tests by running `pytest` in the root, or by running `python3 setup.py test`. Code coverage is enabled with pytest-cov.
3. Edit the `setup.py` of your project to make it truly yours. Remove my email and info from here and put your own info. You may as well delete the full `setup.py` file instead of adapting it if you don't intend to publish your project on `pip` nor on `conda` as  a package. 
4. Start coding in your now-renamed project folder and add some more tests under the `testing/` folder!
5. [Upload](https://packaging.python.org/tutorials/packaging-projects/) your project as a package on [PyPI](https://pypi.org/), the Python Package Index, to make it available on `pip`! (optional)

## Understanding how this template works

The article [The optimal python project structure](https://awaywithideas.com/the-optimal-python-project-structure/) by Luke Tonin does a good job at explaining how a template like the present one works. The present template is a bit more complete and complex than in the article, thought, as it already includes a test suite (including a starter test example), and a thorough `setup.py` file for your project to be properly packaged.

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Guillaume Chevalier](https://github.com/guillaume-chevalier) and [Neuraxio Inc.](https://github.com/Neuraxio) have waived all copyright and related or neighboring rights to this work.

Citations that link to this repository will be appreciated, but are not required.
