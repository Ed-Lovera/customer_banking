# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

def numeric_prompt(title, number_type):
    number = None
    input_msg = f"Please enter your {title}: "
    input_retry_msg = f"Please enter a valid number for your {title}: "
    while number is None or isinstance(number, str):
        input_text = input_msg if number is None else input_retry_msg
        response = input(input_text).strip().replace("%", "")
        if response.isnumeric(): number = number_type(response) 
    return number

def process_account(create_method):
    if create_method not in [create_savings_account, create_cd_account]:
        raise ValueError("Invalid account create method")
    
    account_name = "CD" if create_method == create_cd_account else "Savings"

    # Prompt the user to set the account balance, interest rate, and months for the account.
    balance = numeric_prompt(f"{account_name} balance", float)
    interest = numeric_prompt(f"{account_name} interest rate as a percent", float)
    maturity = numeric_prompt(f"{account_name} maturity in months", int)

    # Call the create_method function and pass the variables from the user.
    updated_balance, interest_earned = create_method(balance, interest, maturity)

    # Print out the interest earned and updated account balance with interest earned for the given months.
    print(f"""
    Interest earned on the {account_name} account is: {interest_earned}
    {account_name} account balance after interest earned is: {updated_balance}
    """)

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    input("Welcome to PythonBank Interest Rate calculator! (Press any key to continue)")
    process_account(create_savings_account)
    process_account(create_cd_account)

if __name__ == "__main__": main()
