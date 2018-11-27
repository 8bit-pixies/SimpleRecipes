# Simple Recipes

Simple Recipes aims to be an alternative to `scikit-learn` for preprocessing data using vanilla python.

Whilst of course we can use `scikit-learn` for machine learning needs, sometimes we require something lighter or _simplier_ without worry about all the dependencies which come with `scikit-learn`. Use cases for this could include:

*  Microservices for Machine Learning algorithms without heavy dependencies on AWS Lambda
*  Ability to transcompile Python code to other languages for integration purposes

## Goals

Enable pure Python library for preprocessing so that it can be easily deployed in many contexts

## Non-goals

This project does not aim to be 100% one to one replacement of scikit-learn. It does not aim to replace the _machine learning_ portion of scikit-learn, rather it encourages uses to bring their own libraries, such as `tensorflow` or others. 

## Running Tests

Tests are runnable via `nose2`. 

```
pip install .['development']
python -m nose2
```