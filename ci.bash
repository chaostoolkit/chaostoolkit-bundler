#!/bin/bash
set -eo pipefail

function build () {
    echo "Building the Chaos Toolkit bundle"
    
    if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
        pyinstaller chaos.spec
    else
        pyinstaller chaos.spec
    fi
}

function main () {
    build || return 1
}

main "$@" || exit 1
exit 0
