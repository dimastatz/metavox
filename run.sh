#!/bin/bash

abort()
{
    echo "*** FAILED ***" >&2
    exit 1
}

if [ "$#" -eq 0 ]; then
    echo "No arguments provided. Usage: 
    1. '-local' to build local environment
    2. '-docker' to build and run docker container
    3. '-test' to run linter, formatter and tests
    4. '-test-package' to run package setup"
elif [ $1 = "-local" ]; then
    trap 'abort' 0
    set -e
    echo "Running format, linter and tests"
    rm -rf .venv
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r ./requirements.txt

    black whisperflow tests
    pylint --fail-under=9.9 whisperflow tests
    pytest --ignore=tests/benchmark --cov-fail-under=95 --cov whisperflow -v tests
elif [ $1 = "-test" ]; then
    trap 'abort' 0
    set -e
    echo "Running format, linter and tests"
    source .venv/bin/activate
    black whisperflow tests
    pylint --fail-under=9.9 whisperflow tests
    pytest --ignore=tests/benchmark --cov-fail-under=95 --cov --log-cli-level=INFO whisperflow -v tests
elif [ $1 = "-docker" ]; then
    echo "Building and running docker image"
    docker stop whisperflow-container
    docker rm whisperflow-container
    docker rmi whisperflow-image
    # build docker and run
    docker build --tag whisperflow-image --build-arg CACHEBUST=$(date +%s) . --file Dockerfile.test
    docker run --name whisperflow-container -p 8888:8888 -d whisperflow-image
elif [ $1 = "-test-package" ]; then
    echo "Running WhisperFlow package setup"
    # pip install twine
    # pip install wheel
    python setup.py sdist bdist_wheel
    rm -rf .venv_test
    python3 -m venv .venv_test
    source .venv_test/bin/activate
    pip install ./dist/whisperflow-0.1.0-py3-none-any.whl
    pytest --ignore=tests/benchmark --cov-fail-under=95 --cov whisperflow -v tests
    # twine upload ./dist/*
else
  echo "Wrong argument is provided. Usage:
    1. '-local' to build local environment
    2. '-docker' to build and run docker container
    3. '-test' to run linter, formatter and tests
    4. '-test-package' to run package setup"
fi

trap : 0
echo >&2 '*** DONE ***'