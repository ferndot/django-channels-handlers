# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at
<https://github.com/joshua-s/django-channels-handlers/issues>.

If you are reporting a bug, please include:
- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and
"help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement
it.

### Write Documentation

django-channels-handlers could always use more documentation, whether as
part of the official django-channels-handlers docs, in docstrings, or
even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/joshua-s/django-channels-handlers/issues>.

If you are proposing a feature:
- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are welcome :)

## Get Started

Ready to contribute? Here's how to set up
django-channels-handlers for local
development.

1. Fork the django-channels-handlers repo on GitHub.

2. Clone your fork locally:
```bash
git clone git@github.com:joshua-s/django-channels-handlers.git
```

3. Install development dependencies and initialize pre-commit
```bash
export PIPENV_VENV_IN_PROJECT=1
pipenv install --dev
pipenv run pre-commit install
```

4. Create a branch for local development:
```bash
git checkout -b name-of-your-bugfix-or-feature
```
    
5. Now you can make your changes locally. When you're done making changes, check that the tests are still passing:
```bash
pipenv run pytest
```

6. Commit your changes and push your branch to GitHub:
```bash
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:
1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.rst.
3. The pull request should work for Python 2.7, 3.4, 3.5 and 3.6, and
    for PyPy. Check
    <https://travis-ci.org/joshua-s/django-channels-handlers/pull_requests>
    and make sure that the tests pass for all supported Python versions.

## Tips

To run a subset of tests:
```bash
pytest channels_handlers
```

## Deploying

A reminder for the maintainers on how to deploy. Make sure all your
changes are committed (including an entry in HISTORY.rst). Then run:
```bash
bumpversion patch # possible: major / minor / patch
git push
git push --tags
```

Travis will then deploy to PyPI if tests pass.
