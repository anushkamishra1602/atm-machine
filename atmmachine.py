class ATM:
    def __init__(self):
        self.account = {'0123':{'Saving':5000000, 'Checking':980000}}
        self.__pin = None
        self.enter_pin()
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin):
        self.__pin = pin
    
    def enter_pin(self):
        while True:
            pin1, pin2 = input("Enter pin: "), input("Verify Pin: ")
            if (len(pin1) + len(pin2) == 8) and (pin1 == pin2) and (pin1 in self.account):
                self.set_pin(pin1)
                self.choice()
            print("Enter pin again!")
    
    def choice(self):
        while True:
            ch = input("Enter choice: ")
            if ch == '1':
                self.ch1()
            elif ch == '2':
                self.ch2()
            elif ch == '3':
                self.ch3()
            elif ch == '4':
                self.ch4()
            else:
                print("Invalid choice!")
                self.enter_pin()
    
    def ch1(self):
        print(self.account[self.get_pin()]['Saving'])
    
    def ch2(self):
        deposit = int(input("Enter Deposit Money: "))
        self.account[self.get_pin()]['Saving'] += deposit
        print(self.account[self.get_pin()]['Saving'])
    
    def ch3(self):
        withdraw = int(input("Enter Withdraw Money: "))
        if self.account[self.get_pin()]['Saving'] >= withdraw:
            self.account[self.get_pin()]['Saving'] -= withdraw
            print(self.account[self.get_pin()]['Saving'])
        else:
            print("Not Enough Balance!")
    
    def ch4(self):
        transfer = int(input("Enter Transfer Amount: "))
        if self.account[self.get_pin()]['Checking'] >= transfer:
            self.account[self.get_pin()]['Checking'] -= transfer
            self.account[self.get_pin()]['Saving'] += transfer
            print("Saving balance:", self.account[self.get_pin()]['Saving'])
            print("Checking balance:", self.account[self.get_pin()]['Checking'])
        else:
            print("Not Enough Balance!")

if __name__ == '__main__':
    atm = ATM()