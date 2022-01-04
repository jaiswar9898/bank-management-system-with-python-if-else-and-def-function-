# bank mamange,emt project

data = {}
list1 = ['Name', 'Address', 'Phone', 'Govt', 'ID', 'Account Type', 'Amount']


def take_data():
    acc_num = input("Enter account number")

    for item in list1:
        list2.append(input("Enter %s:" % item))

    # dic with convert the list1 and list2 in dictoinary
    data[acc_num] = dict(zip(list1, list2))
    print("Account Created")
    print("print 0 for money withdraw and deposit")
    return


def other_options():
    ch = int(input("1.Check balance\n2.Withdraw\n3.Deposit\nEnter the choice"))
    if ch == 1:
        print("Available balance:", data[acc_num]["Amount"])
        print("----------------------------------------------------")

    elif ch == 2:
        amt = int(input("Enter amount to withdraw:"))
        new_amt = int(data[acc_num]["Amount"]) - amt
        data[acc_num]["Amount"] = new_amt
        print("Withdraw Successful")
        print("availabe Balance:", data[acc_num]["Amount"])

    elif ch == 3:
        amt = int(input("Enter amount to Deposit:"))
        new_amt = int(data[acc_num]["Amount"]) + amt
        data[acc_num]["Amount"] = new_amt
        print("Deposit Successful")
        print("availabe Balance:", data[acc_num]["Amount"])


while True:
    list2 = []
    ch = int(input("Enter the choice"))

    if ch == 1:
        take_data()  # it will call def function

    elif ch == 0:
        acc_num = input("Enter your account number")
        if acc_num in data:
            print("Record Found")
            other_options()
        else:
            print("record not found")
