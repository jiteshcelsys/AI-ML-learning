# Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square: {number*number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10, 23]

intial_time = time.time()

if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)

final_time = time.time() - intial_time

print(final_time)