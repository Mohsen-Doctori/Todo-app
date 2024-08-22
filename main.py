from parsers import parse
import random
user_input = input("Enter a lower bound and an upper bound divided a comma (e.g., 2,10)")
parsed = parse(user_input)
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])
print(rand)