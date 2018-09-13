#!/bin/bash
set -eo pipefail

function build () {
    echo "Building the Chaos Toolkit bundle"
    
    export CHAOSTOOLKIT=`which chaos`
    sed -i "s|<CHAOS_PATH>|${CHAOSTOOLKIT}|" chaos.spec

    if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
        pyinstaller chaos.spec
        mv dist/chaos dist/chaos-darwin-amd64
    else
        pyinstaller chaos.spec
        mv dist/chaos dist/chaos-linux-amd64
    fi
}

function main () {
    build || return 1
}

main "$@" || exit 1
exit 0
