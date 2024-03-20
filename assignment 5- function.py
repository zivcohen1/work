#Assignment 5 Function


def menu():
    print('Option 1: Deposit')
    print('Option 2: Withdraw')
    print('Option 3: Check Balance')
    print('Option 4: Exit')

    
def validate_card_number (card_number):
    run = True
    if card_number < 1000 or card_number > 9999:
        print('The card number must be 1000-9999!')
        return True
    
    else:
         return False

    
def validate_card_password (card_number, input_password):
     if input_password != (card_number % 1000):
         print('The password is incorrect!')
         return True
     else:
          
         return False

    
def withdraw (balance, amount):
    

    if amount < 0:
        print('The withdraw amount is negative!')
        print('The transaction is done!')
    elif amount > balance:
        print('The amount is greater than the balance!')
        print('The transaction is done!')
    else:
        balance -= amount
    print('')
    menu()

    return balance
    

        
def deposit(balance, amount):
    
    if amount < 0:
        print('The deposit amount is negative!')
        print('The transaction is done!')
         
    else:
        balance += amount
    print('')
    menu()
    return balance
    

def display_balance(balance):
    print(f'Your balance is {balance:.1f}')
    print('')

    menu()

def main():
    balance = 1000
    run = True 
    while run:
        card_number = int(input('What is your BOA card number (1000-9999)? '))
    
        run = validate_card_number(card_number)
    print('Welcome to BOA!')
    count = 0
    run = True
    while run:
        input_password = int(input('What is your password? '))
        run = validate_card_password(card_number, input_password)
        if not run:
            print('                     ')
            menu()
            while True:
                print(' ')
                option = int(input('Please choose one option from the menu by typing 1, 2, 3, or 4! '))
                if option not in [1, 2, 3, 4]:
                     print('The option is invalid!')
                     print(' ')
                     menu()
                elif option == 1:
                    amount = int(input( 'How much to deposit?'))
                    balance = deposit(balance, amount)
                elif option == 2:
                    amount = int(input( 'How much to withdraw?'))
                    balance = withdraw(balance, amount)
                elif option == 3:
                    display_balance(balance)
                elif option == 4:
                    print('Goodbye!')
                    return
        else:
            count += 1
            if count < 3:
                print(f'You have {3 - count} more times to type your password!')
            else:
                    print('Your card is locked!')
                    print('Goodbye!')
                    break
            
    
if __name__ == '__main__':
    main()

    
    
        
