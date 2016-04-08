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

## Development Data

Included is a shell script (written against `ZSH`; it should work with `BASH`) that can generate a small set of test data from the full set of Yelp data provided for the challenge.  You can run the script as follows:

```bash
./lib/create_dev_data.sh PATH_TO_REVIEW_DATA_FILE PATH_TO_BUSINESS_DATA_FILE
```

This will create files at `./data/review-data-dev.json` and `./data/business-data-dev.json` respectively.  The Review data takes the first 1000 reviews from the full set; the business data is built by finding the businesses that correspond to those reviews and pulling them out into a separate file.

Note: to parse JSON data on the command line, the `jq` tool is required.  More information about it can be found [here](https://stedolan.github.io/jq/).

## Running Tests

From the root of the project directory, run

```bash
$ py.test
```

You can find out more information about `pytest`, you can find the documentation [here](http://pytest.org/latest/contents.html).

## Continuous Integration

Travis CI will automatically run tests for all pull requests and report back to Github with the results (pass or fail).  Just a warning: the dependency installation can take a *really* long time.  This will only be done when versions of dependencies change, or if the dependency cache is cleared.  Normally, this shouldn't be the case; it will use the version of dependencies that were installed previously to avoid a lengthy build process.  Just a warning: if you end up clearing the cache, it _will_ take a long time to run the tests.
