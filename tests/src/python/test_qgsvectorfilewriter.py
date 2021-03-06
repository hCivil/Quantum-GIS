# -*- coding: utf-8 -*-
"""QGIS Unit tests for QgsVectorFileWriter.

.. note:: This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""
__author__ = 'Tim Sutton'
__date__ = '20/08/2012'
__copyright__ = 'Copyright 2012, The Quantum GIS Project'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

import os

from PyQt4.QtCore import QVariant, QDir, QString, QStringList

from qgis.core import (QgsVectorLayer,
                       QgsFeature,
                       QgsField,
                       QgsGeometry,
                       QgsPoint,
                       QgsVectorFileWriter,
                       QgsCoordinateReferenceSystem)

from utilities import (unitTestDataPath,
                       getQgisTestApp,
                       TestCase,
                       unittest,
                       expectedFailure
                       )
QGISAPP, CANVAS, IFACE, PARENT = getQgisTestApp()


class TestQgsVectorLayer(TestCase):

    mMemoryLayer = None

    @expectedFailure
    def testWrite(self):
        """Check we can write a vector file."""
        self.mMemoryLayer = QgsVectorLayer(
            ('Point?crs=epsg:4326&field=name:string(20)&'
            'field=age:integer&field=size:double&index=yes'),
            'test',
            'memory')

        assert self.mMemoryLayer is not None, 'Provider not initialised'
        myProvider = self.mMemoryLayer.dataProvider()
        assert myProvider is not None

        ft = QgsFeature()
        ft.setGeometry(QgsGeometry.fromPoint(QgsPoint(10,10)))
        ft.setAttributeMap({0 : QVariant('Johny'),
                            1 : QVariant(20),
                            2 : QVariant(0.3)})
        myResult, myFeatures = myProvider.addFeatures([ft])
        assert myResult == True
        assert len(myFeatures) > 0

        myFileName = os.path.join(str(QDir.tempPath()), 'writetest.shp')
        print myFileName
        # Explicitly giving all options, not really needed but nice for clarity
        myErrorMessage = QString()
        myOptions = QStringList()
        myLayerOptions = QStringList()
        mySelectedOnlyFlag = False
        mySkipAttributesFlag = False
        myGeoCrs = QgsCoordinateReferenceSystem()
        myGeoCrs.createFromId(4326, QgsCoordinateReferenceSystem.EpsgCrsId)
        myResult = QgsVectorFileWriter.writeAsVectorFormat(
            self.mMemoryLayer,
            myFileName,
            'utf-8',
            myGeoCrs,
            'ESRI Shapefile',
            mySelectedOnlyFlag,
            myErrorMessage,
            myOptions,
            myLayerOptions,
            mySkipAttributesFlag)
        assert myResult==True

if __name__ == '__main__':
    unittest.main()
