#!/bin/bash
set -eo pipefail

function build () {
    echo "Building the Chaos Toolkit bundle"
    
    export CHAOSTOOLKIT_PATH=`which chaos`

    if [[ $TRAVIS_TAG =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        VERSION=$TRAVIS_TAG
    else
        VERSION=${TRAVIS_COMMIT::8}
    fi

    if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
        pyinstaller chaos.spec
        mv dist/chaos dist/chaostoolkit-bundle_darwin-amd64-${VERSION}
    else
        pyinstaller chaos.spec
        mv dist/chaos dist/chaostoolkit-bundle_linux-amd64-${VERSION}
    fi
}

function main () {
    build || return 1
}

main "$@" || exit 1
exit 0
