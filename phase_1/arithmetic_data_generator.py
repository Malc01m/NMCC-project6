from random import randint

num_sums = 3000
min_val = 0
max_val = 100

def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

# Comment out op types as needed
ops = [
    ("add", add), 
    ("sub", sub)
]

with open('sub_data.csv', 'w+') as f_in:
    for i in range(0, 3000):
        op_1 = randint(min_val, max_val)
        op_2 = randint(min_val, max_val)
        op = ops[randint(0, len(ops) - 1)]
        res = op[1](op_1, op_2)
        line = str(op_1) + "," + str(op_2) + "," + op[0] + "," + str(res)
        print(line, file = f_in)
