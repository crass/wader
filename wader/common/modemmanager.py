# -*- coding: utf-8 -*-
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

import dbus

from wader.common import consts

class ModemManager(object):
    """A simple wrapper to access the devices on a hassle-free way"""

    def __init__(self):
        super(ModemManager, self).__init__()
        self.bus = dbus.SystemBus()
        self.mm_obj = None
        self._opaths = []
        self._init_modemmanager()

    def _init_modemmanager(self):
        self.mm_obj = self.bus.get_object(consts.WADER_SERVICE,
                                          consts.WADER_OBJPATH)
        self._opaths = self.mm_obj.EnumerateDevices()
        if not self._opaths:
            raise RuntimeException("No devices found")

    def get_devices(self):
        devices = [self.bus.get_object(consts.WADER_SERVICE, opath)
                            for opath in self._opaths]
        return devices