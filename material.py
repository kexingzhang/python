from abaqus import *
from abaqusConstants import *
from part import *
myModel = mdb.models['Model-1']
partList = myModel.parts.keys()
keyword= "1"
for partName in partList:
    if keyword in partName:
	myPart=myModel.parts[partName]
myMaterial = myModel.Material(name='Steel')
myMaterial.Density(table=((7.8E-09, ), ))
myMaterial.Elastic(table=((200E+09, 0.3), ))
myModel.HomogeneousSolidSection(name='SteelSection', material='Steel', thickness=None)
region = (myPart.cells,)
myPart.SectionAssignment(region=region ,sectionName='SteelSection', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)