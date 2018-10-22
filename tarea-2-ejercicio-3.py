num = int(input("Enter a number: "))

def PerfectNumber(num):
    sum = 0

    for i in range(1, num):
        if (num % i == 0):
            sum += i
    if num == sum:
        return True
    else:
        return False

if PerfectNumber(num):
    print(num, "is a 'Perfect Number'")
else:
    print(num, "is not a 'Perfect Number'")