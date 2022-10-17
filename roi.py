import time

class Return_on_Investment:

    def __init__(self, calculate_income):
            self.calculate_income = calculate_income


class Income(Return_on_Investment):

    def __init__(self, calculate_income, income, laundry, storage, misc_income):
        self.income = income
        self.laundry = laundry
        self.storage = storage
        self.misc_income = misc_income
        Return_on_Investment.__init__(self, calculate_income)

    def get_rent(self):
        print('Now to get into what you make gross income! ')
        time.sleep(2)
        while True:
            income = int(input("How much do your tenants pay in rent per month? \n"))
            time.sleep(1)
            if income is not None:
                self.calculate_income += income
                laundry = int(input("How much do you charge your tenants monthly for laundry? \n"))
                time.sleep(1)
            if laundry is not None:
                self.calculate_income += laundry
                storage = int(input("How much do you charge your tenants monthly for storage? \n"))
                time.sleep(1)
            if storage is not None:
                self.calculate_income += storage
                misc_income = int(input("How much do you charge your tenants for additional services? \n"))
                time.sleep(1)
            if misc_income is not None:
                self.calculate_income += misc_income
            print(f"Your income per month from the rental property is ${self.calculate_income}\n")
            time.sleep(1)
            return

    def calculate_expenses(self, expenses):
        self.expenses = 0
        print("Now let's get into what you pay monthly! ")
        time.sleep(2)
        while True:
            tax = int(input("How much do you pay in taxes for this property? \n"))
            time.sleep(1)
            if tax is not None:
                self.expenses += tax
            insurance = int(input("How much do you pay insurance for this property? \n"))
            time.sleep(1)
            if insurance is not None:
                self.expenses += insurance
            utilities = int(input("How much do you pay for the utilities at this property? \n"))
            time.sleep(1)
            if utilities is not None:
                self.expenses += utilities
            other_expenses = int(input("If there are any other expenses that you cover for this property, how much do you pay? \n"))
            time.sleep(1)
            if other_expenses is not None:
                self.expenses += other_expenses
            print(f"Your monthly expenses come up to a total of ${self.expenses}. \n")
            time.sleep(1)
            return


    def calculate_profit(self, monthly_profit):
        self.monthly_profit = self.calculate_income - self.expenses
        print(f"Your profit per month from your property comes up to ${self.monthly_profit}. \n")

    def calculate_return(self, down_payment, costs):
        self.down_payment = down_payment
        self.costs = costs


i = Income(0,0,0,0,0)
i.get_rent()
i.calculate_expenses(0)
i.calculate_profit(0)

