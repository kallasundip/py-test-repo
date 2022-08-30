import random


def reverse_number():
    num = range(11, 99)
    numbers = random.randint(11, 99)
    # numbers = random.choice(num)
    print(f"Given Number is: {numbers}")
    given_number = str(numbers)
    size = len(given_number)
    reversed_num = given_number[size::-1]
    print("revers number : ", reversed_num)

    '''
    # User Input
    user_input = input("Enter the Number: ")
    print(f"Reverse Number is: {user_input[len(user_input)::-1]}")

    # :: increment
    # num = [1,2,3,4,5,6,7,8,9]
    # print(num[::1])     # Increment one
    # print(num[::2])     # Increment 2
    # print(num[::-1])    # Decrement of -1
    '''


def find_index():
    # Exercise 2: A number sequence is as follows:
    num_sequence = (5, 100, 6, 200, 7, 400, 8, 800, 9, 1600, 10, 3200)
    print(f"Enter Index Value between {0} and {len(num_sequence) - 1}")
    num = int(input("Enter Index Value: "))
    print(num_sequence[num])


def divisors_of_number():
    import random as rd
    # Exercise 3: list of all the divisors
    number = rd.randint(1, 100)
    print(f"Given number {number}")
    total_divisors = []
    for item in range(2, 100):
        if (number % item) == 0:
            total_divisors.append(item)
            if number == item:
                break
    print(f"iteration {item}")
    return total_divisors


reverse_number()
# find_index()
print(divisors_of_number())
