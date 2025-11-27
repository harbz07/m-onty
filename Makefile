APP := m-onty-v1
ZIP := $(APP).zip

.PHONY: all init install clean zip

all: zip

init:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip

install:
	. .venv/bin/activate && pip install -r requirements.txt

zip:
	rm -f $(ZIP)
	zip -r $(ZIP) README.md CONTEXT_MANIFEST.md dashboard schema data src requirements.txt .gitignore

clean:
	rm -f $(ZIP)
