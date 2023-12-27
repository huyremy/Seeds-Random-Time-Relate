import time
import random
def calculate_sum(random_number):
    number_str = str(random_number)
    digit_sum = sum(int(digit) for digit in number_str)
    return digit_sum

def countdown():
    for i in range(30, -1, -1):
        if i == 16:
            random_number = random.randint(10000, 99999)
            print(f"Random number: {random_number}")
            ran = random_number - 16
            sum_of_digits = calculate_sum(ran)
            check_sum = calculate_sum(sum_of_digits)
            check_sum2 = calculate_sum(check_sum)
            print(check_sum2)
        elif i == 0:
            result = random.choice(["Tài", "Xỉu"])
            print(f"Result: {result}")
        else:
            print(f"{i:02d}")
        time.sleep(1)

while True:
    countdown()
    print("Restarting countdown...\n")
