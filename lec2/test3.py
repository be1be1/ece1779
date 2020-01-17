def greatest_difference(num1, num2):
	diff = 0
	for idx, num in enumerate(num1):
		temp = abs(num1[idx]-num2[idx])
		if temp >= diff:
			diff = temp
	return diff

print(greatest_difference([1,2,3], [6,8,10])) 