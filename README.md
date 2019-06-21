# Chives

[![Build Status](https://travis-ci.org/klreeher/chives.svg?branch=master)](https://travis-ci.org/klreeher/chives)

## APPS

### chives

### pages

## used

- pipenv
- django

## build and docker push

- automatically builds docker image from dockerfile
- pushes to docker using docker_push.sh

## makefile

- makefile uses pipenv and runs pytest (using django-pytest)
- https://docs.pipenv.org/en/latest/advanced/#travis-ci
- todo: actually have tests that run

- if you run into write error using pipenv with python3, 

    ```pipenv --three --python=`which python3` ```
    
  and add python as a bash alias for python3


## reference

- https://wsvincent.com/django-hello-world-with-docker/ 