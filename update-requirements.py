from optparse import Values
from pathlib import Path
import sys

from pip._internal.index.collector import LinkCollector
from pip._internal.models.selection_prefs import SelectionPreferences
from pip._internal.network.session import PipSession
from pip._internal.index.package_finder import PackageFinder
import semver
from semver import VersionInfo


REQ_FILE = 'requirements-chaostoolkit.txt'
MASTER_REQ_FILE = 'master-requirements-chaostoolkit.txt'


def get_finder() -> PackageFinder:
    return PackageFinder.create(
        LinkCollector.create(
            session=PipSession(),
            options=Values(defaults=dict(
                no_index=False, index_url="https://pypi.python.org/simple",
                find_links=None, extra_index_urls=[""]))
        ),
        SelectionPreferences(
            allow_yanked=False,
            allow_all_prereleases=True
        ),
        use_deprecated_html5lib=False,
    )


def get_latest_release_version(finder: PackageFinder,
                               package: str) -> VersionInfo:
    results = finder.find_all_candidates(package)
    versions = sorted(set([p.version for p in results]), reverse=True)
    return semver.parse_version_info(str(versions[0]).replace('rc', '-rc'))


def update_requirements():
    finder = get_finder()

    changed = False
    reqs = []
    updated_reqs = []

    with open(MASTER_REQ_FILE) as f:
        for line in f:
            line = line.strip()

            version = '0.0.0'
            package = line

            if '==' in line:
                package, version = line.split('==', 1)

            current = semver.parse_version_info(version.replace('rc', '-rc'))
            latest = get_latest_release_version(finder, package)

            version = latest if latest > current else current
            reqs.append("{}=={}".format(
                package, str(version).replace('-rc', 'rc')))

            if latest > current:
                changed = True
                updated_reqs.append("{}=={}".format(
                    package, str(latest).replace('-rc', 'rc')))

    if changed:
        updates = '\n'.join(updated_reqs)

        with open(REQ_FILE, 'w') as f:
            f.write('\n'.join(reqs) + '\n')

        print(updates)
        Path("./has_changes.txt").touch()


if __name__ == '__main__':
    update_requirements()
