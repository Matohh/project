import random
import time

def generate_random_number(start, end):
    return random.randint(start, end)

def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)

def find_largest_number(numbers):
    return max(numbers)

def find_smallest_number(numbers):
    return min(numbers)

def find_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

def find_mode(numbers):
    frequency = find_frequency(numbers)
    mode = [num for num, freq in frequency.items() if freq == max(frequency.values())]
    return mode

def find_median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        median = numbers[length // 2]
    return median

def find_range(numbers):
    return max(numbers) - min(numbers)

def find_variance(numbers):
    mean = calculate_average(numbers)
    variance = sum((num - mean) ** 2 for num in numbers) / len(numbers)
    return variance

def find_standard_deviation(numbers):
    variance = find_variance(numbers)
    standard_deviation = variance ** 0.5
    return standard_deviation

def generate_numbers(start, end, count):
    numbers = []
    while len(numbers) < count:
        num = generate_random_number(start, end)
        if num not in numbers:
            numbers.append(num)
    return numbers

def main():
    start_time = time.time()

    start = 1
    end = 100
    count = 1000

    numbers = generate_numbers(start, end,)