'''
10. Problem-Solving:
a. Given an array of integers, write an algorithm to find the two numbers that add up to a specific target sum.
b. Solve the classic FizzBuzz problem: Print numbers from 1 to 100, but replace multiples of 3 with "Fizz" and multiples of 5 with "Buzz."
'''
# Fizzbuzz problem
a = list(range(1,101))
for i in range(len(a)):
    if a[i] % 3 ==0 and a[i] % 5 == 0:
        a[i] = 'Fizzbuzz'
    elif a[i] % 3 == 0:
        a[i] = 'Fizz'
    elif a[i] % 5 == 0:
        a[i] = 'buzz'
print(a)