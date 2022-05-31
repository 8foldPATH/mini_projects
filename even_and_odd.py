n = int(input("Enter a number: "))
numbers = list(range(1, n))

total_even = 0
total_odd = 0

for number in numbers:
    if number %2 == 0:
        total_even += number
    if number %2 != 0:
        total_odd += number 
        
print(f"The sum of all the even numbers between 1 and {n} is {total_even}")
print(f"The sum of all the odd numbers between 1 and {n} is {total_odd}")