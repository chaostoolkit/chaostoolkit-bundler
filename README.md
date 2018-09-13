# Chaos Toolkit Bundler

Bundle the Chaos Toolkit CLI and all the drivers/plugins into one
standalone binary for Linux and MacOSX platforms.

## Create a standalone bundle

If you need to create a standalone bundle of the Chaos Toolkit with all its
drivers and plugins (except reporting for now), please do as follows:

```
$ python -m venv .bundler
$ source .bundler/bin/activate
(.bundler) $ pip install -U -r requirements.txt
(.bundler) $ pyinstaller chaos.spec
```

You need to do that on all the platforms you want to target. Once generated,
a `chaos` binary will be found in the `dist` directory. You can copy and
run this binary without having to create a virtual environment or install
the drivers any more.

Be aware that the generated binary does not keep the drivers up-to-date by
itself. You need to regenerate it whenever a new release of the toolkit or a
driver is made.

## Contribute

If you wish to contribute more functions to this package, you are more than
welcome to do so. Please fork this project, make your changes following the
usual [PEP 8][pep8] code style, add appropriate tests and submit a PR for
review.

[pep8]: https://pycodestyle.readthedocs.io/en/latest/

The Chaos Toolkit projects require all contributors must sign a
[Developer Certificate of Origin][dco] on each commit they would like to merge
into the master branch of the repository. Please, make sure you can abide by
the rules of the DCO before submitting a PR.

[dco]: https://github.com/probot/dco#how-it-works