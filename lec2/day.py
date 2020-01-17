import event

class Day:
	def __init__(self, day, month, year):
		self.day = day
		self.month = month
		self.year = year
		self.events = []
		
	def schedule_event(self, new_event):
		for e in self.events:
			if e.__overlaps__(new_event):
				return False
		self.events.append(new_event)
		return True
		
	def __str__(self):
		result = "{0} {1} {2}:\n".format(self.day, self.month, self.year)
		
		for event in self.events:
			result = result + "- {0}\n".format(event)
		return result
		
d = Day(29, 'November', 2016)
print(d.schedule_event(event.Event(15, 16, 'Submit A3 work')))
print(d.schedule_event(event.Event(16, 23, 'Celebrate!')))
print(d.__str__())

		