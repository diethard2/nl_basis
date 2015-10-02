NL Basis
========
A QGIS plugin to generate Spatiale databases from big zipped xml-files holding the basis registration geodata
of the Netherlands.

The basic idea behind NL Basis
------------------------------
To provide local access to public basis registration geodata provided for free by the Dutch government
to use and to serve.
I want do this using a standard QGIS installation only and a QGIS plugin written in Python that can be added easily.
The processing of the data is not allowed to last for days, a few hours is acceptable.
The plugin should process the delivery without unzipping the provided zipped xml-files first.
The result should be in a usable form for many endusers, simple and fast enough to work with.
Styles and symbology should be included and loaded as wel when adding the spatialite layers in QGIS.
Unit tests should be provided to create an agile test driven development environment where code can 
be easily improved (refactored).
I start with BAG and continue with BGT, topo_nl, IMRO and other xml based deliveries.
The QGIS plugin should really be implemented as several QGIS processing algoritms so you can build your own 
processing model maybe skipping some steps or adding some steps.
I really would like to get more involvement of other developers to work on this idea so it becomes a 
more community driven idea.

The geodata is currently provided as many, many XML-files that are zipped into one basis registry zip-file. 
After unzipping the xml files can not be used directly in a geodatabase, it still needs some conversion.
The basis registry for building (BAG) for example is zipped 1.4 GB but unzipped more than 60 GB.

2-10-2015 
I still need to develop the QGIS plugin.
Currently the code provided can be used to generate the following output:

* A Spatialite database with the name `bag.sqlite*`

The input are two files:

* inspireadressen.zip
* Tabel33 Gemeententabel (gesorteerd op omschrijving).csv

The database bag.sqlite, holds all boundaries of places (towns/cities), buildings, houseboats and trailerstands 
that are registrated in the Netherlands as an official place to stay that can be shutdown to have some privacy. 
Included are offices, garage boxes and tiny transformer buildings. A building can provide a place for several 
families or shops that can have an adress. Points for each residence has been provides as well with address.

How to set up
-------------
Currently described for Windows OS only.
First download and install QGIS 2.8 and python 2.7.
Now you should have a folder named `C:\Python27` with python installed. 
Create a batch file `C:\Python27\run_idle.bat` with following contents:

```dos
SET PATH=%PATH%;C:\Program Files\QGIS Wien\bin;C:\Program Files\QGIS Wien\apps\qgis\bin
SET PYTHONPATH=C:\Program Files\QGIS Wien\apps\qgis\python
SET PYTHONPATH=%PYTHONPATH%;C:\Program Files\QGIS Wien\apps\Python27\Lib\site-packages
SET PYTHONPATH=%PYTHONPATH%;C:\Program Files\QGIS Wien\apps\qgis\python\plugins 
CALL %~dp0\Lib\idlelib\idle.bat
```

When you start this batchfile IDLE will start but you will have access to all python libraries included in QGIS as well.

Create following folders 
C:\data\bag
C:\data\bag\input

Download following files and put them in input-folder C:\data\bag\input
inspireadressen.zip from: 
http://geodata.nationaalgeoregister.nl/inspireadressen/extract/inspireadressen.zip

Tabel33 Gemeententabel (gesorteerd op omschrijving).csv from:
http://www.rijksdienstvooridentiteitsgegevens.nl/dsresource?objectid=16993&type=org

Create a local repository using git of this project, start idle using run_idle.bat and open the python file test_all.py.
Press F5 (Run) to get an initialised python-console and give following statements.

import test_all
test_all.full_run()

Now do something else for a couple of hours, you can see the progress is pretty slow, but finally you will find the 
following file which size is about 6 GB.
C:\data\bag\bag.sqlite

Connect to this database in QGIS and you will see the following layers can be selected and loaded with provided style. 
Not everything is visible initially until you are zoomed in on streetlevel. 

Following 5 layers are provided (with styling for QGIS):

* verblijfsplaats (points with address and a foreign key to pand)
* pand (polygons of buildings)
* standplaats (polygons of trailerstands with address)
* ligplaats (polygons of houseboats with address)
* woonplaats (polygons of cities and town borders that together cover the whole of the Netherlands) 

Using QGIS relations, you can set up a relation between pand and verblijfsplaats.
In QGIS select Project --> Project Properties...
Select on the left side relation and add a relation using the button [Add Relation]

Provide following values:
* Name: Adressen 
* Referencing Layer (Child): verblijfplaats
* Referencing Field: id_pand
* Referenced Layer (Parent): pand
* Referenced Field: id





