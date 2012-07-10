# -*- coding: utf-8 -*-
# Copyright (C) 2006-2010  Vodafone España, S.A.
# Copyright (C) 2008-2009  Warp Networks, S.L.
# Author:  Andrew Bird
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

try:
    from core.hardware.qualcomm import QualcommWCDMADevicePlugin
except ImportError:
    # Try the pre-3.00 import path
    from wader.common.hardware.qualcomm import QualcommWCDMADevicePlugin


class VodafoneWCDMAML27(QualcommWCDMADevicePlugin):
    """:class:`~wader.common.plugin.DevicePlugin` for Vodafone Mobile Link 27"""
    name = "Vodafone Mobile Link 27"
    version = "0.1"
    author = u"Glenn Washburn"

    __remote_name__ = "Vodafone Mobile Link 27"

    __properties__ = {
        'ID_VENDOR_ID': [0x20a6],
        'ID_MODEL_ID': [0x1105],
    }


vodafonewcdmaml27 = VodafoneWCDMAML27()
