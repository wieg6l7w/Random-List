import random

def generate_random_list(num_elements):
    return [random.randint(5, 500) for _ in range(num_elements)]

result = generate_random_list(15)
print(result)