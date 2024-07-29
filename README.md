# customer_banking
Execute `customer_banking.py` in the repository's root directory to run the program.

## Background
You'll be creating a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.

## Requirements
Create the Savings Account Function (35 points)
- The Account class from the Accounts.py file is imported. (4 points)
- In the create_savings_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. (6 points)
- The interest earned is calculated and assigned to a variable. (4 points)
- The savings account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)
- The updated balance is passed to the set balance method using the instance of the Account class. (6 points)
- The interest earned is passed to the set balance method using the instance of the Account class. (6 points)
- The updated balance and interest earned are returned by the function. (5 points)

Create the CD Account Function (35 points)
- The Account class from the Accounts.py file is imported. (4 points)
- In the create_cd_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. (6 points)
- The interest earned is calculated and assigned to a variable. (4 points)
- The CD account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)
- The updated balance is passed to the set balance method using the instance of the Account class. (6 points)
- The interest earned is passed to the set balance method using the instance of the Account class. (6 points)
- The updated balance and interest earned are returned by the function. (5 points)

Create the Main Function (30 points)
- The user is prompted to set the savings balance, interest rate, and months for the savings account. (8 points)
- Code is written to print out the interest earned and updated savings account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)
- The user is prompted to set the savings balance, interest rate, and months for the CD account. (8 points)
- Code is written to print out the interest earned and updated CD account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)
- The main function is called to run the program. (2 points)
