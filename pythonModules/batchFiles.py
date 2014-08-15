#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bellie
#
# Created:     08/08/2014
# Copyright:   (c) Bellie 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import subprocess, os
import config as cfg
def csv2grd(grid):
    c2g = cfg.scriptFP + '\\bin\\csv2gdr.bat'
    CGd = cfg.SCommand + '\n'
    CGd += 'saga_cmd io_table "Import Text Table" -TABLE='+cfg.scriptFP + '\\bin\\xyz.csv -HEADLINE -SEPARATOR=2 -SEP_OTHER=* -FILENAME='+cfg.scriptFP + '\\bin\\xyz.csv'
    CGd += '\nsaga_cmd shapes_points "Convert Table to Points" -POINTS='+cfg.scriptFP + '\\bin\\xyz.shp -TABLE='+cfg.scriptFP + '\\bin\\xyz.csv -X=0 -Y=1 -Z=2'
    CGd += '\nsaga_cmd shapes_points "Thiessen Polygons" -POINTS='+cfg.scriptFP + '\\bin\\xyz.shp -POLYGONS='+cfg.scriptFP + '\\bin\\xyzP.shp -FRAME=10.000000'
    CGd += '\nsaga_cmd grid_gridding "Shapes to Grid" -INPUT='+cfg.scriptFP + '\\bin\\xyzP.shp -FIELD=2 -OUTPUT=2 -MULTIPLE=1 -LINE_TYPE=1 -POLY_TYPE=1 -GRID_TYPE=3 -TARGET=0 -USER_XMIN=1781320.466000 -USER_XMAX=1821170.466000 -USER_YMIN=5566281.328000 -USER_YMAX=5617231.328000 -USER_SIZE=50.000000 -USER_FIT=1 -USER_GRID='+ grid + ' -USER_COUNT=NULL -GRID_GRID= -GRID_COUNT=NULL'
    CGd += '\nPause'
    open(c2g, 'w').write(CGd)
    subprocess.call(c2g)