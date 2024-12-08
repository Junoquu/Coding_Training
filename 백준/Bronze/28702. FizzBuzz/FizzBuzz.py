def fizz_buzz(num):
    num = int(num) % 15
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def process_input(value, increment):
    if value.isdigit():
        new_value = int(value) + increment
        result = fizz_buzz(new_value)
        return new_value if isinstance(result, int) else result
    return None

inputs = [input() for _ in range(3)]
increments = [3, 2, 1]

for value, increment in zip(inputs, increments):
    result = process_input(value, increment)
    if result is not None:
        print(result)
        break