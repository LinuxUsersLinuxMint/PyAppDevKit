#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
PyAppDevKit Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyAppDevKit All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/PyAppDevKit
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/PyAppDevKit"""

import pyappdevkit

PYTHON_LIB_NAME="PyAppDevKit"
PYTHON_LIB_LICENCE="GPL2"
PYTHON_LIB_IMPLEMENTED_CONTRACTS="LinuxUsersLinuxMint Privacy and Security Agreement , LinuxUsersLinuxMint Web Site Agreement"
PYTHON_LIB_IMPLEMENTED_CONTRACTS_WEB_SITE="https://linuxuserslinuxmint.github.io/Contracts/privacyandsecutryagreement/privacyandsecutryagreement.html , https://linuxuserslinuxmint.github.io/Contracts/linuxuserslinuxmintwebsiteagreement/linuxuserslinuxmintwebsiteagreement.html"
PYTHON_LIB_VER="2.2"
PYTHON_LIB_SUPPORT_PLATFORM="Windows/Linux/macOS/otherOS"
PYTHON_LIB_RELEASE_DATE="6/9/2024, Time: 17:54"
PYTHON_LIB_LAST_UPDATE_DATE="8/15/2025, Time: 23:44 / 11:44 PM"
PYTHON_LIB_AUTHOR="LinuxUsersLinuxMint"
PYTHON_LIB_AUTHOR_WEB_SITE="https://linuxuserslinuxmint.github.io"

def LibAbout():
    pyappdevkit.app_info("Python Library Name:",PYTHON_LIB_NAME,"Python Library Version:",PYTHON_LIB_VER,"Python Library Support OS:",PYTHON_LIB_SUPPORT_PLATFORM,"Python Library Licence Name:",PYTHON_LIB_LICENCE,"Python Library Implemented Contracts:",PYTHON_LIB_IMPLEMENTED_CONTRACTS,"Python Library Implemented Contracts Web Site:",PYTHON_LIB_IMPLEMENTED_CONTRACTS_WEB_SITE,"Python Library Author Name:",PYTHON_LIB_AUTHOR,"Python Library Author Web Site:",PYTHON_LIB_AUTHOR_WEB_SITE,"Python Library Release Date:",PYTHON_LIB_RELEASE_DATE,"Python Library Last Update Date:",PYTHON_LIB_LAST_UPDATE_DATE)