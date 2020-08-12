# The Fizz Buzz Test
# The Fizz Buzz test is a poplular interview question used to help filter out the 99.5% of programming job candidates who can't seem to program their way out of a wet paper bag.

# Write a program that returns a list of all the numbers from 1 to an integer argument. But for multiples of three use “Fizz” instead of the number and for the multiples of five use “Buzz”. For numbers which are multiples of both three and five use “FizzBuzz”.

# Example
# fizz_buzz(10) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]

# fizz_buzz(15) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
# Notes
# Make sure to return a list.

def fizz_buzz(maximum):
    arr = []
    for i in range(1, maximum + 1):
        if i % 5 == 0 and i % 3 == 0:
            arr.append('FizzBuzz')
        elif i % 3 == 0:
            arr.append('Fizz')
        elif i % 5 == 0:
            arr.append('Buzz')
        else:
            arr.append(i)
    return arr


print(fizz_buzz(15))
