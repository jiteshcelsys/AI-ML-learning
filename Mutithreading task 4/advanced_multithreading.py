# MutiThreading witht thread pool executor
from concurrent.futures import ThreadPoolExecutor
import time
# in this we are giving 13 inputs to the functions with a delay of 1 second on every
# execution because of advanced multithreading it is distributing the task to different workers an
# and complete the given task with in 6 sec instead of 15 sec

def print_numbers(number):
    time.sleep(1)
    return f"Number:{number}"
t = time.time()

numbers = [1,12,23,14,15,26,16,37,58,76,859,39,39, 12,14]

with ThreadPoolExecutor(max_workers=3) as executor:
    results= executor.map(print_numbers, numbers)

for result in results:
    print(result)
finalized_time = time.time() - t
print(finalized_time, 'finalized time')
