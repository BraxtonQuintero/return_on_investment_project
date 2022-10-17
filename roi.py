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
        while True:
            income = int(input("How much do your tenants pay in rent per month? "))
            if income is not None:
                self.calculate_income += income
                laundry = int(input("How much do you charge your tenants monthly for laundry? "))
            if laundry is not None:
                self.calculate_income += laundry
                storage = int(input("How much do you charge your tenants monthly for storage? "))
            if storage is not None:
                self.calculate_income += storage
                misc_income = int(input("How much do you charge your tenants for additional services? "))
            if misc_income is not None:
                self.calculate_income += misc_income
            print(f"Your income per month from the rental property is ${self.calculate_income}")
            return

    def calculate_expenses(self, expenses):
        self.expenses = 0
        while True:
            tax = int(input("How much do you pay in taxes for this property? "))
            if tax is not None:
                self.expenses += tax
            insurance = int(input("How much do you pay insurance for this property? "))
            if insurance is not None:
                self.expenses += insurance
            utilities = int(input("How much do you pay for the utilities at this property? "))
            if utilities is not None:
                self.expenses += utilities
            other_expenses = int(input("If there are any other expenses that you cover for this property, how much do you pay? "))
            if other_expenses is not None:
                self.expenses += other_expenses
            print(f"Your monthly expenses come up to a total of ${self.expenses}. ")
            return


    def calculate_profit(self, monthly_profit):
        self.monthly_profit = self.calculate_income - self.expenses
        print(f"Your profit per month from your property comes up to ${self.monthly_profit}.")

    def calculate_return(self, down_payment, costs):
        self.down_payment = down_payment
        self.costs = costs


i = Income(0,0,0,0,0)
i.get_rent()
i.calculate_expenses(0)
i.calculate_profit(0)

