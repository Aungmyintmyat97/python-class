#if break statement

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equal', x, '*', n//x)
			break
		else:
			print(n, 'is a prime number')

#if continue statement

#for num in range(2, 10):
#	if num % 2 == 0:
#		print('Found an even number', num)
#		continue
#	print('Found a number', num)



# n = 1000
# first = 0
# second = 1
# for i in range(n):
# 	print(first)
# 	temp = first
# 	first = second, second = temp + second
# 	print(first, end=' ')