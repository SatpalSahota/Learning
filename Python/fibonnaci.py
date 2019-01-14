def fib(n):
		a, b = 0, 1
		while a < n:
			print(a, end=' ')
			a, b = b, a+b
		print()

print("How high would you like to go? ")
limit = input()
fib(int(limit))
