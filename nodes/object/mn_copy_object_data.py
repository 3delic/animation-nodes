import bpy, random
from bpy.types import Node
from animation_nodes.mn_cache import getUniformRandom
from animation_nodes.mn_node_base import AnimationNode
from animation_nodes.mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling

class mn_CopyObjectData(Node, AnimationNode):
	bl_idname = "mn_CopyObjectData"
	bl_label = "Copy Object Data"
	
	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_ObjectSocket", "From")
		self.inputs.new("mn_ObjectSocket", "To")
		self.outputs.new("mn_ObjectSocket", "To")
		allowCompiling()
		
	def getInputSocketNames(self):
		return {"From" : "fromObject", "To" : "toObject"}
	def getOutputSocketNames(self):
		return {"To" : "toObject"}
		
	def execute(self, fromObject, toObject):
		if fromObject is not None and toObject is not None:
			if toObject.data != fromObject.data:
				toObject.data = fromObject.data
		return toObject
		

