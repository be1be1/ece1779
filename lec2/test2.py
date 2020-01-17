def upper_case(s):
	cnt = 0 
	for word in s:
		if word.isupper():
			cnt += 1
	
	return cnt

print(upper_case("SssSssS"))
		
	