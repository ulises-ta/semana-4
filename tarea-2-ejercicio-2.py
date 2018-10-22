num = int(input("Enter a number: "))
min = int(input("Enter the min limit for the range: "))
max = int(input("Enter the max limit for the range: "))

def is_in_range(num, min, max):
    if (num >= min) and (num <= max):
        return num
    print(num, "is in the range")
    else:
        print(num, "is not in the range")

is_in_range(num, min, max)