master_pw = "Pass123!"

def add_account(account_name, username, password):
    
  new_data = {
        "account_name": account_name,
        "username": username,
        "password": password
    }
  with open("passwords.txt", "a") as file:
        file.write(str(new_data) + "\n")
        print("Account information saved successfully.")

def delete_account(account_name):
    found = False
    updated_lines = []

    with open("passwords.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        account_data = eval(line)
        if account_data.get("account_name") == account_name:
            found = True
        else:
            updated_lines.append(line)

    if found:
        with open("passwords.txt", "w") as file:
            file.writelines(updated_lines)
        print("Account information deleted successfully.")
    else:
        print("Account not found.")

def retrieve_account(account_name):
    found = False

    with open("passwords.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        account_data = eval(line)
        if account_data.get("account_name") == account_name:
            found = True
            print("=============================================")
            print("Account Name:", account_data["account_name"])
            print("Username:", account_data["username"])
            print("Password:", account_data["password"])
            print("=============================================")
            break

    if not found:
        print("Account not found.")

def print_accounts():
    pw = input("Enter Master Password: ")
    if pw == master_pw:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            account_data = eval(line)
            print("Account Name:", account_data["account_name"])
            print("Username:", account_data["username"])
            print("Password:", account_data["password"])
            print("")
    else:
        print("Wrong Password!!!")
  
   
print("1. Add an account")
print("2. Retrieve an account")
print("3. Delete an account")
print("4. Display all passwords")
print("5. Quit")

choice = input("Enter your choice: ")

if choice == "1":
  account_name = input("Enter account name: ")
  username = input("Enter username: ")
  password = input("Enter password: ")
  add_account(account_name,username,password)
            
elif choice == "2":
  account_name = input("Enter account name: ")
  retrieve_account(account_name)
    
elif choice == "3":
  account_name = input("Enter account name: ")
  delete_account(account_name)
elif choice == "4":
     print_accounts()
elif choice == "5":
  print("==============================================") 
  print("Thanks for using this simple Password Manager!")
  print("==============================================")