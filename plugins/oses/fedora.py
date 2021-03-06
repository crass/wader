# -*- coding: utf-8 -*-
# Copyright (C) 2006-2008  Vodafone España, S.A.
# Copyright (C) 2008-2009  Warp Networks, S.L.
# Author:  Pablo Martí
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""Fedora OSPlugin"""

from os.path import exists
import re

from twisted.internet.utils import getProcessValue

from core.oses.linux import LinuxPlugin
from wader.common.utils import get_file_data


class FedoraBasedDistro(LinuxPlugin):
    """
    OSPlugin for Fedora-based distros
    """

    def is_valid(self):
        paths = ['/etc/redhat-release', '/etc/fedora-release']
        return any(map(exists, paths))

    def update_dns_cache(self):
        if exists("/usr/sbin/nscd"):
            getProcessValue("/etc/init.d/nscd", ["condrestart"])
            getProcessValue("/etc/init.d/nscd", ["-i", "hosts"])


fedora = FedoraBasedDistro()
