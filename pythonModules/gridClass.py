#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bellie
#
# Created:     11/08/2014
# Copyright:   (c) Bellie 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import gdal
import numpy as np
from gdalconst import *

class writeGrid(object):
    def __init__(self,grid,data,gformat):
        self.grid = grid
        self.rows = data.shape[0]
        self.columns = data.shape[1]
        self.data = data
        self.gformat = gformat                                                  #List of formats at http://www.gdal.org/formats_list.html
        gdal.AllRegister()
    def createGrid(self):
        driver = gdal.GetDriverByName(self.gformat)
        outDs = driver.Create(self.grid, self.columns, self.rows, 1, GDT_Float32)
        outBand = outDs.GetRasterBand(1)
        outBand.WriteArray(self.data, 0, 0)

a = np.array([[1,2],[3,4]])
fp = 'J:\\Projects\\SMB_Model\\bin\\temp.sdat'
b = writeGrid(fp,a,'SAGA')
b.createGrid()