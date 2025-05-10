def is_divisible_by_5(number):
    return number % 5 == 0

num = int(input("Enter a number :"))

if is_divisible_by_5(num):
    print("True")
else:
    print("False")
    
    