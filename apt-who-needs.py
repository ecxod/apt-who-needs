#!/usr/bin/env python3

import subprocess
import sys

def update_package_lists():
    subprocess.check_call(['apt-get', '-qq', 'update'])

def get_installed_dependencies(package_name):
    rdepends_output = subprocess.check_output(['apt-rdepends', '--reverse', package_name], text=True)
    installed_packages_output = subprocess.check_output(['dpkg', '-l'], text=True)
    installed_packages = [line.split()[1] for line in installed_packages_output.splitlines() if line.startswith("ii")]

    for line in rdepends_output.splitlines():
        if line.strip() in installed_packages:
            if line != package_name:
                print(f"\033[34m\033[47m{line}\033[0m is installed and requires \033[34m\033[47m{package_name}\033[0m")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No packagename givven.")
        print("HINT: python3 apt-who-needs.py <PackageName>")
        sys.exit(1)

    package_name = sys.argv[1]
    update_package_lists()
    get_installed_dependencies(package_name)
