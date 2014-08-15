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
import os

scriptFP = os.path.dirname(os.path.realpath(__file__))[:-13]
Saga = scriptFP+"\saga_2.1"
SCommand = '@ECHO OFF\n'
SCommand = SCommand + 'SET SAGA_MLB="'+Saga+'\modules"\n'
SCommand = SCommand + 'SET PATH=%PATH%;"'+Saga+'"\n'

try:
    os.makedirs(scriptFP+'\\results\\csv')
except:
    pass
grid_RF = scriptFP + '\\bin\\rainfall.sgrd'
grid_PET = scriptFP + '\\bin\\PET.sgrd'
grid_SMB = scriptFP + '\\bin\\SMB'