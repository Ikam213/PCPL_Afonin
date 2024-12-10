import random

def gen_random(num_count, begin, end):
    ans = []
    for i in range(num_count):
        ans.append(random.randint(begin, end))
    return ans
