# Next steps:

> Remove this section, this is just FYI

1. Open Alfred to check your workflow is visible
2. Modify `main.py`
3. Add `icon.png` file and update icon in the workflow
4. Push to GitHub
5. Release your first version
   ```shell script
   make release
   ```

👻 Important: when adding new file make sure to update `SRC` variable at the top
of `Makefile`

🐍 Adding new python dependency:

1. Add it to the `_requirements.txt`

   (_It's not called `requirements.txt` cause
   libraries are being installed in the `lib` folder, and (at least) PyCharm complains
   about packages resolution_)
2. Install: `make pip ` 
   

> Next part is a suggested README

---

### Installation

[Download]({{ cookiecutter.github_repo }}/releases/) Alfred workflow and open it

### Usage

Invoke Alfred and type `hello <world>`

### Local development

```bash
make
```

It will create a `{{ cookiecutter.workflow_dir }}` folder in your default Alfred
installation and add all required source files as symlinks.

Then just open Alfred on Workflows tab and you'll find it.

---

Made with [Alfred-Workflow](https://github.com/deanishe/alfred-workflow)

Bootstrapped from
[alfred-python-template](https://github.com/fbjorn/alfred-python-template)
