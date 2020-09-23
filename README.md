# alfred-python-template

Cookiecutter template for amazing
[Alfred-Workflow](https://github.com/deanishe/alfred-workflow) 🍪🎩

## Features

- 🚀 Extremely quick bootstrapping of a new Workflow. One command and you're
  ready to start the development:
  ```shell script
  make
  ```
  _(Alfred-Workflow is installed and path resolution is configured)_
- 🏗 Automated releases to GitHub. With a single command of course:
  ```shell script
  make release
  ```
  _(Under the hood it will push the tag parsed from `info.plist` and run a
  GitHub action to build the package and attach it to GitHub release)_
- 👀 A couple of ready-to-go pre-commit hooks

More information is in the [README](./{{cookiecutter.workflow_dir}}/README.md)
