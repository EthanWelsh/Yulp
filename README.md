# Yulp [![Build Status](https://travis-ci.org/EthanWelsh/Yulp.svg?branch=master)](https://travis-ci.org/EthanWelsh/Yulp)
Yelp data challenge project to attempt to ascertain restaurant price ratings from written user reviews

## Installing Dependencies

Python version: 3.5.0

```bash
$ pip install -r requirements.txt
$ python
```

then, once Python is loaded:

```python
import nltk
nltk.download()
```

and choose to download "all" (at least, for now).

If you need to add new dependencies to the `requirements.txt` file, the easiest way to do so is like so:

```bash
$ pip freeze > requirements.txt
```

which will output your current dependency list to the file.  You should probably only do that if you're using a `virtualenv` to isolate the dependencies for just this project.

## Running Tests

From the root of the project directory, run

```bash
$ py.test
```

You can find out more information about `pytest`, you can find the documentation [here](http://pytest.org/latest/contents.html).
