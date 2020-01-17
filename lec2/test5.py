def express_checkout(p):
	total = 0
	for key, value in p.items():
		total = total + value
	if total <= 8:
		return True
	return False
	
# 
	
print(express_checkout({'banana': 3, 'soy milk': 1, 'twinkie': 5}))