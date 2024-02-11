#!/usr/bin/env python3

import subprocess
import sys
import os

def check_root():
    if os.geteuid() != 0:
        print("Please execute as root or with sudo.")
        print("HINT: sudo python3 apt-who-needs.py <PackageName>")
        sys.exit(0)

def check_packagename_given():
    if len(sys.argv) < 2:
        print("ERROR: No packagename given.")
        print("HINT: python3 apt-who-needs.py <PackageName>")
        sys.exit(0)

def update_package_lists():
    subprocess.check_call(['apt-get', '-qq', 'update'])

def get_installed_dependencies(package_name):
    rdepends_output = subprocess.check_output(['apt-rdepends', '--reverse', package_name], text=True)
    installed_packages_output = subprocess.check_output(['dpkg', '-l'], text=True)
    installed_packages = [line.split()[1] for line in installed_packages_output.splitlines() if line.startswith("ii")]

    for line in rdepends_output.splitlines():
        if line.strip() in installed_packages:
            if line != package_name:
                print(f"\033[32m{line}\033[0m is installed and requires \033[32m{package_name}\033[0m")

if __name__ == "__main__":
    check_root()
    check_packagename_given()
    package_name = sys.argv[1]
    update_package_lists()
    get_installed_dependencies(package_name)
    sys.exit(0)
