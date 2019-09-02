from pcraster import *
from pcraster.framework import *

class Fire(DynamicModel):
	def __init__(self):
		DynamicModel.__init__(self)
		setclone('clone.map')

	def initial(self):
		pass

	def dynamic(self):
		pass

nrOfTimeSteps=100
myModel = Fire()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()

