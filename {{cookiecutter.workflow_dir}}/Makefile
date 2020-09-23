SRC := main.py info.plist lib icon.png
WF_DIR := ${HOME}/Documents/Alfred/Alfred.alfredpreferences/workflows/{{ cookiecutter.workflow_dir }}
VERSION := $(shell grep -Eo 'string.*[0-9]+\.[0-9]+\.[0-9]+.*string' info.plist | cut -d">" -f2 | cut -d"<" -f1)

all: pip link

pip:
	python2 -m pip install --upgrade pip
	python2 -m pip install --target=./lib -r _requirements.txt

link:
	mkdir -p "${WF_DIR}"
	for f in ${SRC} ; do \
  		ln -sf "${PWD}/$$f" "${WF_DIR}/$$f"; \
  	done

clean:
	for f in ${SRC} ; do \
  		unlink "${WF_DIR}/$$f"; \
  	done

release:
	git tag ${VERSION}
	git push origin ${VERSION}
