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

        echo $CAL_VERSION > VERSION

        git config --global user.name "${GH_USER}"
        git config --global user.email "${GH_EMAIL}"
        git config --global push.default simple
        git remote add ghorig https://${GH_USER}:${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git > /dev/null 2>&1

        git add VERSION requirements-chaostoolkit.txt
        git commit -s -m "Release $CAL_VERSION"
        git push -q ghorig master > /dev/null

        git tag $CAL_VERSION
        git push -q ghorig $CAL_VERSION > /dev/null
    else
        echo "None of the dependencies have changed since the last release."
    fi
}

function release () {
    echo "Creating a new release from a tag"

    build
}

function main () {
    # let's not build tags
    if [[ $TRAVIS_TAG =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        release || return 1
    else
        if [[ $TRAVIS_OS_NAME == 'linux' ]]; then
            tag_if_needed || return 1
        fi
    fi
}

main "$@" || exit 1
exit 0
