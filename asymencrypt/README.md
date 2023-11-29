# Asymmetric Encryption Practice

This program encrypts a given text, and prints out the cipher text.

## Setup

This setup is specific to Windows OS.

- Create and activate environment

```sh
$ python -m venv venv
```

```sh
$ .\venv\Scripts\activate
```

- Install dependencies

```sh
pip install -r requirements.txt
```

- You might want to update your pip

```sh
python -m pip install --upgrade pip
```

RUN

```sh
uvicorn encrypt:app --reload
```
