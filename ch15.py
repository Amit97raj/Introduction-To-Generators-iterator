# Python Basics Chapter 15:
# =========================

# 1. Introduction To Generators

# generators are iterators

# 2. Generator Example

# generator function
# generator comprehension

# def print_nums(n):
#     for i in range(1, n+1):
#         yield i

# print(print_nums(10))

# numbers = print_nums(10)

# numbers = list(print_nums(10))

# print(numbers)

# for num in numbers:
#     print(num)

# 3. Exercise - 1

# Define a generator function
# Take one number as argument
# Generate a sequence of even numbers from 1 to that number

# 4. Exercise - 1 Solution

# def even_generator(n):
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             yield i

# def even_generator(n):
#     for i in range(2, n+1, 2):
#         yield i

# nums = even_generator(10)

# for num in nums:
#     print(num)

# 5. Generator Comprehension

# square = (i**2 for i in range(1, 11))

# for num in square:
#     print(num)

# print(next(square))

# 6. List Vs Generators

# memory usage, time
# when to use list, when to use generator

# import time

# t1 = time.time()
# l = [i**2 for i in range(10000000)] # 250 MB , 2.51 Seconds
# t2 = time.time()
# print(t2-t1) 

# t1 = time.time()
# g = (i**2 for i in range(10000000)) # No Memory , No Time
# t2 = time.time()
# print(t2-t1)
