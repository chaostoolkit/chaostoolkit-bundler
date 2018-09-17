#!/bin/bash
set -eo pipefail

function build () {
    echo "Building the Chaos Toolkit bundle"
    
    export CHAOSTOOLKIT_PATH=`which chaos`

    pyinstaller chaos.spec

    if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
        mv dist/chaos dist/chaostoolkit-bundle_darwin-amd64-${CAL_VERSION}
    else
        mv dist/chaos dist/chaostoolkit-bundle_linux-amd64-${CAL_VERSION}
    fi
}

function tag_if_needed () {
    echo "Creating a new tag if needed"
    
    cd /tmp
        
    git clone https://${GH_USER}:${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git bundler > /dev/null 2>&1
        
    cd bundler

    git config user.name "${GH_USER}"
    git config user.email "${GH_EMAIL}"
    git config push.default simple

    python3 update-requirements.py

    # have we updated the requirements?
    if [[ $? == 1 ]]; then
        # for debugging purpose
        git diff requirements-chaostoolkit.txt

        # today's version (suffixed if more than one per-day)
        # potential race condition here when multiple concurrent builds
        # let's assume it won't happen very often and we can fix it manually
        # Simplicity...
        export CAL_VERSION=`python3 get-next-version.py`

        echo ${CAL_VERSION} > VERSION
        git add VERSION requirements-chaostoolkit.txt
        git commit -s -m "$(printf "Prepare ${CAL_VERSION}\n\n[ci skip]")"
        git push -q origin > /dev/null

        local changes=`cat requirements-chaostoolkit.txt`
        git tag -a ${CAL_VERSION} -m "$(printf "Release ${CAL_VERSION}\n\nContains:\n${changes}")"
        git push -q origin $CAL_VERSION > /dev/null
    else
        echo "None of the dependencies have changed since the last release."
    fi
}

function release () {
    echo "Creating a new release from a tag"

    build
}

function main () {
    if [[ $TRAVIS_TAG =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        release || return 1
    else
        if [[ $TRAVIS_BRANCH != master ]]; then
            return 0
        fi

        if [[ $TRAVIS_OS_NAME == 'linux' ]]; then
            tag_if_needed || return 1
        fi
    fi
}

main "$@" || exit 1
exit 0
