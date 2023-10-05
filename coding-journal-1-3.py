# this program defines f(x) and retruns the example of f(9)

# the def f(x) checks if an answer is greater than 27, and retruns 'yay'
# if the answer is true. otherwise it returns the answer of the expression
def f(x):
	ans = (int(x * 3 + 8))
	if ans > 27:
		return ("YAY " + str(ans))
	else:
		return (ans)

print(f(9))


