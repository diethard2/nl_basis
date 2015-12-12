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
#from processing.tools import dataobjects, vector

import nl_basis.create_bag_db
import nl_basis.fill_bag_db
import time

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
        self.__bag_db = None

    def get_bag_db(self):
        return self.__bag_db

    def set_bag_db(self, bag_db):
        self.__bag_db = bag_db

    def getIcon(self):
        return QIcon(os.path.dirname(__file__) + '/../basis_nl.png')

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
        output_folder = self.getParameterValue(self.OUTPUT_FOLDER)

        # And now we can process, let's see if I can write something to 
        # the logfile.
        ProcessingLog.addToLog(ProcessingLog.LOG_INFO, "Started creating BAG database")
        bag_db = os.path.join(output_folder, 'bag.sqlite')
        self.set_bag_db(bag_db)
        self.create_spatialite_database(progress)
        self.create_datamodel(progress)
        self.fill_database(progress)
        self.create_views(progress)
        self.flatten_tables(progress)
        self.drop_views_and_tables(progress)
        self.create_styles(progress)
        ProcessingLog.addToLog(ProcessingLog.LOG_INFO, "Finished creating BAG database")
        
    def create_spatialite_database(self, progress):
        """Create BAG spatialite database."""
      
        ProcessingLog.addToLog(ProcessingLog.LOG_INFO, "Started creating BAG database")
        bag_db = self.get_bag_db()
        nl_basis.create_bag_db.create_db(bag_db)
        # give process 5 seconds to finish.. 
        time.sleep(5)
        progress.setPercentage(3)
        progress.setText("The BAG database is created!")
        
    def create_datamodel(self, progress):
        """Create initial BAG datamodel.

        The initial BAG datamodel will hold all tables to contain the information
        parsed from xml-files that are used for input.
        """
        
        progress.setText("Create initial datamodel BAG database")
        bag_db = self.get_bag_db()
        nl_basis.create_bag_db.create_datamodel(bag_db)
        progress.setPercentage(5)
        progress.setText("Datamodel BAG database is created!")

    def fill_database(self, progress):
        progress.setText("Start to read data in input folder and fill BAG database")
        input_folder = self.getParameterValue(self.INPUT_FOLDER)
        bag_db = self.get_bag_db()
        filler = nl_basis.fill_bag_db.FillDB(bag_db, input_folder)
        filler.run()
        progress.setPercentage(60)
        progress.setText("All data is read into BAG database")

    def create_views(self, progress):
        progress.setText("Start to create spatial views for better access")
        bag_db = self.get_bag_db()
        nl_basis.create_bag_db.create_views(bag_db)
        progress.setPercentage(65)
        progress.setText("Created spatial views")

    def flatten_tables(self, progress):
        """Create physical tables from spatial views to improve performance."""
        bag_db = self.get_bag_db()
        nl_basis.create_bag_db.flatten_tables(bag_db)
        progress.setPercentage(90)
        progress.setText("Physical tables have been created from spatial views")

    def drop_views_and_tables(self, progress):
        """Drop the views and tables that are not necessary anymore"""
        bag_db = self.get_bag_db()
        nl_basis.create_bag_db.drop_tables(bag_db)
        progress.setPercentage(95)
        progress.setText("Unneccesary tables and views are removed from BAG database")

    def create_styles(self, progress):
        """Insert styles in the BAG database that will be used by QGIS"""
        bag_db = self.get_bag_db()
        nl_basis.create_bag_db.create_styles(bag_db)
        progress.setText("Default styles are inserted in BAG database")
       
              
        
