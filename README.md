# Rem

Replace words in stdin and files using python standard library re.

## Install

```bash
$ pip install -e git+https://github.com/emilioag/rem.git#egg=rem
```

### Virtualenv (python3)

```bash
$ python3 -m venv venv-rem
$ source venv-rem/bin/activate
$ pip install -e git+https://github.com/emilioag/rem.git#egg=rem
```


## Use

### Replace stdin

```bash
$ rem stdin \
    --replace="(version:\s+?)\d+(.\d+)?(.\d+)?" \
    --by="\1rem" \
    --text="version: 1.0.1"

  version: rem
```

### Replace file

```
$ cat test_file.txt

  author: 312
  date: 00/00/99
  version: 1.0.1
```

```
$ rem file \
    --replace="(version:\s+?)\d+(.\d+)?(.\d+)?" \
    --by="\1rem" \
    --file-name=test_file.txt

  FOUND: test_file.txt
  - version: 1.0.1

  + version: rem

  Do you want to replace it? [y/N] [False]: y
  REPLACED: test_file.txt
```

### Replace directory

```
$ test_files/cat test_0.txt

Nothing to replace

$ test_files/cat test_1.txt

  some matches

  version: 1.0.1
  hello world
  version: 2.5.6

$ test_files/cat test_2.txt
  one match
  version: 3.4.0

  hello world
```


```bash
$ rem dir \
    --replace="(version:\s+?)\d+(.\d+)?(.\d+)?" \
    --by="\1rem" \
    --dir-name=test_files

  NO MATCHES FOUND: test_files/test_0.txt
  FOUND: test_files/test_1.txt
  - version: 1.0.1

  + version: rem

  - version: 2.5.6

  + version: rem

  Do you want to replace it? [y/N] [False]: y
  REPLACED: test_files/test_1.txt
  FOUND: test_files/test_2.txt
  - version: 3.4.0

  + version: rem

  Do you want to replace it? [y/N] [False]: y
  REPLACED: test_files/test_2.txt
```