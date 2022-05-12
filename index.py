class rentalProp():

    def __init__(self):
        self.income = []
        self.expenses = []
        self.total = []

    def rentalIncome(self):
        rent = int(input('What is the rental income of the property? '))
        self.income.append(rent)

    def rentalExpenses(self):
        expen = int(input('What is the expense of the property? '))
        self.expenses.append(expen)

    def totalInvest(self):
        spend = int(input('How much did you pay? '))
        self.total.append(spend)

rental = rentalProp()

def run():
    while True:
        house = input('Would you like to know your your ROI? ')
        if house.lower() == 'yes':
            rental.rentalIncome()
            rental.rentalExpenses()
            rental.totalInvest()
            cashFlow = (rental.income[0] - rental.expenses[0])*12
            roi = (cashFlow / rental.total[0])*100
            print(f'Your cash flow would be {cashFlow} per year and your ROI is {roi}%!')
            rental.income.clear()
            rental.expenses.clear()
            rental.total.clear()

        else:
            print('Then find a deal to annalize!')

run()