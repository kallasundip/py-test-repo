from datetime import datetime
import pandas


def new_policy():
    present_date_time = datetime.now()
    exp_year = present_date_time.year + 10
    modified_formate = present_date_time.strftime(f"%d-%B-%Y %I-%M %p")
    policy_exp_year = present_date_time.strftime(f"%d-%B-{exp_year} %I-%M %p")

    print("User Registration:")
    user_name = input("Enter user Name: ")
    dob = input("Enter data of Birth: ")
    submit = input("Submit Application(y/n): ")
    print(dob)
    if submit == "y":
        print(f"Registration Completed...{modified_formate}")
        print(f"Policy expiry date: {policy_exp_year}")


def policy_expery():
    # companies = [('ram', 0o5 - "September" - 2022 07-10 "PM"),
    #              ('google', 2019, 134.81),
    #              ('Apple', 2019, 260.2),
    #              ('Facebook', 2019, 70.7)]
    # print(companies)

    today = datetime.today()
    x = today.strftime("%m/%d/%Y")
    print(x)





# new_policy()
# policy_expery()
