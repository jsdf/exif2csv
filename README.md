## Development Quickstart
### Install pyenv on OSX

```bash
brew install pyenv
brew install pyenv-virtualenv
```

### Installing project deps

```bash
# in repo root dir
pyenv install -s # installs .python-version if necessary
pyenv virtualenv exif2csv 
pip install -r requirements.txt
```
