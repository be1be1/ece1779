def count_steps(n):
	steps = 0
	result = n
	while result != 1:
		if n%2 == 0:
			n = n//2
		else:
			n = n*3+1
		result = n
		steps = steps + 1
	return steps
print(count_steps(10))