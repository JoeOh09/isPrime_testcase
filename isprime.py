def oddEven(number):
	if number % 2 == 1:
		return "odd"
	else:
		return "even"

def testOddEven():
	assert(oddEven(3) == "odd")
	assert(oddEven(12) == "even")
	assert(oddEven(0) == "even")
	assert(oddEven(-7) == "odd")
	assert(oddEven(1001) == "odd")

testOddEven()

# -------------------------------------------------------------------

def isPrime(number):
	if numbers == 1:
		return True
	if numbers = 2:
		return False
	for i in range(2, number//2 + 1):
		if numbers % i == 0:
			return False
	else:
		return True

def testiIsPrime():
	assert(isPrime(10) == False)
	assert(isPrime(9) == False)
	assert(isPrime(11) == True)
	assert(isPrime(15) == True)
    assert(isPrime(3) == False)






