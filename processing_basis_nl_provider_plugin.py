# -*- coding: utf-8 -*-

"""
***************************************************************************
    processing_basis_nl_provider_plugin.py
    ---------------------
    Date                 : October 2015
    Copyright            : (C) 2015 by Diethard Jansen
    Email                : diethard.jansen at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Diethard Jansen'
__date__ = 'October 2015'
__copyright__ = '(C) 2015, Diethard Jansen'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from processing.core.Processing import Processing
from nl_basis.basis_nl_algorithm_provider import Basis_nl_algorithm_provider
cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class Processing_basis_nl_provider_plugin:

    def __init__(self):
        self.provider = Basis_nl_algorithm_provider()

    def initGui(self):
        Processing.addProvider(self.provider, True)

    def unload(self):
        Processing.removeProvider(self.provider)
