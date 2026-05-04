import random
import time
# eval() fnc can take any string expr and calculate it as if it is a  valid python code
operators = ["+", "-", "*"]

MIN_operand = 3
MAX_operand = 12
TOTAL_problem = 10


def generate_problem():
    left = random.randint(MIN_operand, MAX_operand)
    right = random.randint(MIN_operand, MAX_operand)

    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)

    return expr, answer


expr, answer = generate_problem()
print(f"{expr} = {answer}")

wrong = 0
input("press enter to start!")
print("--------------------")

start_time = time.time()

for i in range(TOTAL_problem):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem {i+1} : {expr} = ")
        if guess == str(answer):
            break
        wrong += 1
        

end_time = time.time()
total_time = round(end_time - start_time)
print("--------------------")
print(f"Nice Work! you finished in {total_time} ,seccond ")
