import sys

try:
    from pip.index import PackageFinder
except ImportError:
    from pip._internal.index import PackageFinder

import requests
import semver
from semver import VersionInfo


REQ_FILE = 'requirements-chaostoolkit.txt'


def get_finder() -> PackageFinder:
    return PackageFinder(
        [],
        ['https://pypi.python.org/simple'],
        session=requests.Session()
    )


def get_latest_release_version(finder: PackageFinder,
                               package: str) -> VersionInfo:
    results = finder.find_all_candidates(package)
    versions = sorted(set([p.version for p in results]), reverse=True)
    return semver.parse_version_info(str(versions[0]))


def update_requirements():
    finder = get_finder()

    changed = False
    reqs = []
    updated_reqs = []

    with open(REQ_FILE) as f:
        for line in f:
            package, version = line.strip().split('==', 1)
            current = semver.parse_version_info(version)
            latest = get_latest_release_version(finder, package)

            version = latest if latest > current else current
            reqs.append("{}=={}".format(package, str(version)))

            if latest > current:
                changed = True
                updated_reqs.append("{}=={}".format(package, str(latest)))

    if changed:
        updates = '\n'.join(updated_reqs)

        with open(REQ_FILE, 'w') as f:
            f.write('\n'.join(reqs) + '\n')

        print(updates)
        sys.exit(1)


if __name__ == '__main__':
    run()