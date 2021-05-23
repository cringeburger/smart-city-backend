import json


class json_serializable():
	def __init__(self, name):
		self.name = name
		self.data = [{}]
		self.t_index = 0

	def add_features(self, name, value):
		self.data[self.t_index][name] = value

	def new_features_tuple(self):
		self.data.append({})
		self.t_index += 1

	def add_feature_list(self, name):
		self.data[self.t_index][name] = []

	#def feature_list_add(self, name)
	