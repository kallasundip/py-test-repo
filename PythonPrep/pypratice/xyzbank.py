is_logined = False
is_quit = False

user = {"name": "",
        "balance": 0
        }


def write_text():
    with open("xyz_company_user_details.txt", "w") as userdata:
        for line in user:
            userdata.write(line)
            userdata.write("\n")


def new_user():
    name = input("Enter user name: ")
    user["name"] = name
    acc_type = input("Enter Account Type salary/savings: ")
    id_number = input("Enter your id number: ")
    address = input("Enter Address: ")
    print(f"{name} Your Account Created...")
    return name
    global is_logined
    is_logined = True
    write_text()


def show_balance():
    print(f"your balance is {user['balance']}")
    print("")


def transfer_money():
    try:
        t_money = int(input("How much money you want to transfer: "))
        if t_money > user["balance"]:
            print("Your account does not have that much money")
        elif t_money == 0:
            print("Please Enter Valid Amount..")
        else:
            user["balance"] = user["balance"] - t_money
            print(f"{t_money} has been withdrawn form your account total balance left is {user['balance']}")
    except:
        print("Please Enter a Number...")


def deposit_money():
    try:
        d_amount = int(input("How much money you want to deposit: "))
        user["balance"] = user["balance"] + d_amount
        print(f"{d_amount} has been deposited to your account your total account balance is {user['balance']}")
        print("")
    except:
        print("Please Enter a number")


def start():
    while is_quit == False:
        if is_logined == False:
            print("Create your account: ")
            new_user()
        else:
            print(f"Welcome to bank {user['name']} what you want to do...!")
            given_input = input("""Press w for Withdraw,\nPress d to deposit,\nPress b to show your balance:,\nPress q to quit,\npress help: """)
            if given_input == 'w':
                transfer_money()
            elif given_input == 'd':
                deposit_money()
            elif given_input == 'b':
                show_balance()
            elif given_input == 'help':
                print("Press w for withdraw money")
                print("Press d for deposit money")
                print("Press b for show balance money")
                print("Press q for quit")
            elif given_input == 'q':
                break
            else:
                print("Enter a correct value from given type help")


start()
