# Inheritance:
#   - A class can inherit properties and methods from another class.
# Encapsulated:

class ATM:
    def __init__(self, BankName="BOI", Pin=1234, Balance=5000):
        self.__bankName = BankName
        self.__pin = Pin
        self.__balance = Balance

    def verification(self):
        print("Wait for few sec...")
        print("Details are varifying...")
        print("Verification is successfully done: ")
        pin = int(input("Enter your Pin:"))
        self.__userValidation(pin)

    def __userValidation(self, Pin):
        while (True):
            if self.__pin == Pin:
                print("1. Withdrawl Amount:")
                print("2. Check Balance:")
                print("3. Get Back:")
                chooice = int(input("Enter :"))
                match(chooice):
                    case 1:
                        amt = int(input("Enter your Amount : "))
                        self.__withdrawlAmt(amt)
                    case 2:
                        self.__checkBalance()
                    case 3:
                        print("Thank you for using our ATM")
                        break
                    case _:
                        print("Invalid choice")

                # if chooice == 1:
                #     self.WithdrawlAmt()
                # elif chooice == 2:
                #     self.checkBalance()
                # else:
                #     print("Invalid choice")

            else:
                print("Invalid Pin: ")

    def __withdrawlAmt(self, W_Atm):
        if self.__balance >= W_Atm:
            self.__balance -= W_Atm
            print("Withdrawl is successfully done! \n(Kindly Collect Your Cash)")
        else:
            print("Insufficient Balance: ")

    def __checkBalance(self):
        print("Your Current Balance is: ", self.__balance)


atm = ATM()
atm.verification()
