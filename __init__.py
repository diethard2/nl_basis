# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : September 201
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
__date__ = 'September 2015'
__copyright__ = '(C) 2015, Diethard Jansen'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from nl_basis.processing_basis_nl_provider_plugin import Processing_basis_nl_provider_plugin

def classFactory(iface):
    return Processing_basis_nl_provider_plugin()
