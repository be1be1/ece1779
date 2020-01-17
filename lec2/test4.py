def can_pay_with_two_coins(denoms, amount):
	for i in denoms:
		second = amount - i
		if second in denoms:
			return True
	return False

print(can_pay_with_two_coins([1,5,10,25], 12))