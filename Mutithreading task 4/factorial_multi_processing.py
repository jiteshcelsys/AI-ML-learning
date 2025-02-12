'''
Real world -example : Multi Processing for CPU-bound tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computaional work .MultiProcessing can be used to distribute the workload
across multiple CPU cores,  improving performance.

'''
import sys
import time
import math
import multiprocessing

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number

def computer_factorial(number):
    print(f'Computing factorial of {number}')
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

start_time = time.time()

numbers = [6002, 2121, 1921, 3412, 3312, 3212]

# Calculate factorial for each number in the array
resultant_array = [computer_factorial(num) for num in numbers]

# Print the resultant array
print("Resultant array of factorials:", resultant_array)

end_time = time.time()

print(f'time taken to complete this task is {end_time - start_time}seconds')

if __name__ == '__main__':
    numbers = [6002,2121, 1921, 2813, 3312, 3412]
    # numbers = [3002, 3241,6423,3121]
    start_time1 = time.time()

    with multiprocessing.Pool() as pool:
        result = pool.map(computer_factorial, numbers)

    end_time2 = time.time()

    print(f'Results: {result}')
    print(f'Time taken: {end_time2-start_time1} seconds')
