# -*- coding: utf-8 -*-

"""
***************************************************************************
    basis_nl_algorithm_provider.py
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
from PyQt4.QtGui import *
from processing.core.AlgorithmProvider import AlgorithmProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig
from nl_basis.algorithms.bag_algorithm import Bag_algorithm


class Basis_nl_algorithm_provider(AlgorithmProvider):

    INPUT_FOLDER = "C:\\data\\bag\\input"
    OUTPUT_FOLDER = "C:\\data\\bag"
    
    def __init__(self):
        AlgorithmProvider.__init__(self)

        # Activate provider by default
        self.activate = True

        # Load algorithms
        self.alglist = [Bag_algorithm()]
        for alg in self.alglist:
            alg.provider = self

    def initializeSettings(self):
        """In this method we add settings needed to configure our
        provider.

        Do not forget to call the parent method, since it takes care
        or automatically adding a setting for activating or
        deactivating the algorithms in the provider.
        """
        AlgorithmProvider.initializeSettings(self)
        ProcessingConfig.addSetting(Setting('Basis NL algorithms',
            Basis_nl_algorithm_provider.INPUT_FOLDER,
            'C:\\data\\bag\\input', 'Default value'))

    def unload(self):
        """Setting should be removed here, so they do not appear anymore
        when the plugin is unloaded.
        """
        AlgorithmProvider.unload(self)
        ProcessingConfig.removeSetting(
            Basis_nl_algorithm_provider.INPUT_FOLDER)

    def getName(self):
        """This is the name that will appear on the toolbox group.

        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return 'Basis NL'

    def getDescription(self):
        """This is the provider's full name.
        """
        return 'Basis NL'

    def getIcon(self):
        """We return the default icon.
        """
        return QIcon(os.path.dirname(__file__) + '/../basis_nl.png')

    def _loadAlgorithms(self):
        """Here we fill the list of algorithms in self.algs.

        This method is called whenever the list of algorithms should
        be updated. If the list of algorithms can change (for instance,
        if it contains algorithms from user-defined scripts and a new
        script might have been added), you should create the list again
        here.

        In this case, since the list is always the same, we assign from
        the pre-made list. This assignment has to be done in this method
        even if the list does not change, since the self.algs list is
        cleared before calling this method.
        """
        self.algs = self.alglist
