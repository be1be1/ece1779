class Event:
	def duration(self):
		return self.end_time-self.start_time
	
	def __str__(self):
		#result = self.name+": "+"from "+str(self.start_time)+" to "+str(self.end_time)
		result = "{0}: from {1} to {2}".format(self.name, self.start_time, self.end_time)
		return result
	
	def __eq__(self, other):
		if (other.start_time == self.start_time) and (other.end_time == self.end_time):
			return True
		else:
			return False
		
	def __overlaps__(self, other):
		if (self.end_time <= other.start_time) or (other.end_time <= self.start_time):
			return False
		else:
			return True
		
	def __init__(self, start_time, end_time, event_name):
		self.start_time = start_time
		self.end_time = end_time
		self.name = event_name
	
e = Event(12,13,'lunch')
print(e.start_time)
print(e.end_time)
print(e.name)
print(e.duration())
print(e.__str__())
e1 = Event(11, 13, 'breakfast')
print(e.__eq__(e1))
print(e.__overlaps__(e1))