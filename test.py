numbers = [1, 2, 3, 4, 5]

# Shorten the loop using lambda and list comprehension
squared_numbers = [(lambda x: x**2)(num) for num in numbers]

print(squared_numbers)