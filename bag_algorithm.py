# -*- coding: utf-8 -*-

"""
***************************************************************************
    bag_algorithm.py
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import QgsVectorFileWriter

from processing.core.GeoAlgorithm import GeoAlgorithm
from processing.core.parameters import ParameterFile
from processing.core.outputs import OutputVector
from processing.core.ProcessingLog import ProcessingLog
from processing.tools import dataobjects, vector

class Bag_algorithm(GeoAlgorithm):
    """This is an example algorithm that takes a vector layer and
    creates a new one just with just those features of the input
    layer that are selected.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the GeoAlgorithm class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT_FOLDER = 'OUTPUT_FOLDER'
    INPUT_FOLDER = 'INPUT_FOLDER'

    def __init__(self):
        GeoAlgorithm.__init__(self)

    def getIcon(self):
        return QIcon(os.path.dirname(__file__) + '/basis_nl.png')

    def help(self):
        """Returns the help with the description of this algorithm.
        It returns a tuple boolean, string. IF the boolean value is True,
        it means that the string contains the actual description. If False,
        it is an url or path to a file where the description is stored.
        In both cases, the string or the content of the file have to be HTML,
        ready to be set into the help display component.

        Returns None if there is no help file available.

        The default implementation looks for an HTML page in the QGIS
        documentation site taking into account QGIS version.
        """
        helpUrl = os.path.dirname(__file__) + '/help/create_bag.html'
        return False, helpUrl

    def commandLineName(self):
        return 'basis_nl:create_bag'

    def defineCharacteristics(self):
        """Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # The name that the user will see in the toolbox
        self.name = 'Create BAG database'

        # The branch of the toolbox under which the algorithm will appear
        self.group = 'Database'

        # We add the input folder. It is a mandatory  hence the False argument
        self.addParameter(ParameterFile(self.INPUT_FOLDER,
            self.tr('Input folder'), isFolder=True, optional=False))

        # We add the output folder. It is a mandatory  hence the False argument
        self.addParameter(ParameterFile(self.OUTPUT_FOLDER,
            self.tr('Output folder'), isFolder=True, optional=False))

    def processAlgorithm(self, progress):
        """Here is where the processing itself takes place."""

        # The first thing to do is retrieve the values of the parameters
        # entered by the user
        input_folder = self.getParameterValue(self.INPUT_FOLDER)
        output_folder = self.getParameterValue(self.OUTPUT_FOLDER)

        # And now we can process, let's see if I can write something to 
        # the logfile.
        ProcessingLog.addToLog(ProcessingLog.LOG_INFO, "Started creating BAG database")
        progress.setPercentage(90)
        import time
        time.sleep(10)
        progress.setText("The BAG database is created!")
        ProcessingLog.addToLog(ProcessingLog.LOG_INFO, "Finished creating BAG database")
        
        

