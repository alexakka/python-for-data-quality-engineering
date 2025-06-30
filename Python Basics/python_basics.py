# create list of 100 random numbers from 0 to 1000
import random as rnd

rnd_numbers = [rnd.randint(0, 1000) for _ in range(100)]


# sort list from min to max (without using sort())
for i in range(len(rnd_numbers) - 1):
    for j in range(i + 1, len(rnd_numbers)):
        if rnd_numbers[i] > rnd_numbers[j]:
            rnd_numbers[i], rnd_numbers[j] = rnd_numbers[j], rnd_numbers[i]


# calculate average for even and odd numbers
even_numbers = [num for num in rnd_numbers if num % 2 == 0]
odd_numbers = [num for num in rnd_numbers if num % 2 == 1]

sum_even_numbers = sum(even_numbers)
sum_odd_numbers = sum(odd_numbers)

avg_even_numbers = sum_even_numbers / len(even_numbers)
avg_odd_numbers = sum_odd_numbers / len(odd_numbers)


# print both average result in console 
print(f"Average for even numbers: {avg_even_numbers}")
print(f"Average for odd numbers: {avg_odd_numbers}")
