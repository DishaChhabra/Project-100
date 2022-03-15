cardNum = int(input('enter the card number: '))
cardPin = int(input('enter the card pin for security: '))
print('thank you!')
print('')
print('please enter "1" if you wish to check your bank balance.')
print('please enter "2" if you wish to withdraw some money.')
print('please enter "3" if you wish to get your card details.')
option = int(input('enter a number from the following options: '))
print('')

class ATM:
    def __init__(self, cardNum, cardPin):
        self.cardNum = cardNum
        self.cardPin = cardPin
    def moneyWithdrawal(self):
        amount = int(input('enter the amount of money to be withdrawn- '))
        print('₹',amount, 'has been withdrawn from your account. There are now ₹', 100000-amount, 'in your bank account.')
    def checkBalance(self):
        print('there are currently 1,00,000 rupees in your bank account.')
    def bankdDetails(self):
        print('CARD NUMBER = ', cardNum)
        print('CARD PIN = ', cardPin)
        print('BALANCE = ', 100000)

new = ATM(cardNum, cardPin)
if option == 1:
    new.checkBalance()
elif option == 2:
    new.moneyWithdrawal()
elif option == 3:
    new.bankdDetails()
