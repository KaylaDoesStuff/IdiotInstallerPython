import os
from variables import *

def check_distro():
    if os.path.exists(pacman_path):
        distro = "Arch"
    elif os.path.exists(apt_path):
        distro = "Debian"
    elif os.path.exists(emerge_path):
        distro = "Gentoo"
    elif os.path.exists(apk_path):
        distro = "Alpine"
    elif os.path.exists(pkg_path):
        distro = "FreeBSD"
    elif os.path.exists(xbps_path):
        distro = "Void"
    elif os.path.exists(dnf_path):
        distro = "RHEL-Based"
    else:
        distro = "Unknown"
    return distro

def type_print():
    for i in TYPE:
        print(i, ">", TYPE[i])
