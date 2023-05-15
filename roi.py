class ROI():

    def __init__(self):
        self.rent = 0
        self.num_properties = 0
        self.tax = 0
        self.insurance = 0
        self.utilities = 0
        self.hoa_fee = 0
        self.vacancy = 0
        self.repairs = 0
        self.capex = 0
        self.property_manage = 0
        self.mortgage = 0
        self.down_payment = 0
        self.closing_costs = 0
        self.rehab_budget = 0
        self.total_income = 0
        self.total_expenses = 0
        self.total_cashFlow = 0
        self.cashOnCashROI = 0

    def income(self):
        self.rent = float(input('How much do you charge for rent per unit? '))
        self.num_properties = float(input('How many units are in this property? '))

        self.total_income = self.num_properties * self.rent
        round(self.total_income, 2)

    def expenses(self):
        self.tax = float(input('What is monthly cost in property taxes for this property? ')) #Illinois state average is .0207
        self.insurance = float(input('What is the monthly insurance rate for this property? '))
        self.utilities = float(input('What is the average monthly rate for utilities? *Please enter 0 if the tenant will be covering utilities* '))
        self.hoa_fee = float(input('How much per month are HOA fees for this property? *Please enter 0 if there are no HOA fees* '))
        self.vacancy = .05 * self.total_income
        self.repairs = 100
        self.capex = 100
        self.property_manage = float(input('What is your monthly property management cost for this property? *Please enter 0 if you manage this property alone* '))
        self.mortgage = float(input('What is your monthly cost for your mortgage on this property? '))
        self.total_expenses = self.tax + self.insurance + self.utilities + self.hoa_fee + self.vacancy + self.repairs + self.capex + self.property_manage + self.mortgage
        round(self.total_expenses, 2)


    def cashFlow(self): 
        self.total_cashFlow = self.total_income - self.total_expenses
        round(self.total_cashFlow, 2)

    def cashROI(self): 
        self.down_payment = float(input('What was your downpayment on this property? '))
        self.closing_costs = float(input('What were your closing costs on this property? '))
        self.rehab_budget = float(input('What was your rehab budget on this property? *Please enter 0 of you do not have a rehab budget for this property* '))
        total_investment = self.down_payment + self.closing_costs + self.rehab_budget
        annual_cashFlow = self.total_cashFlow * 12
        self.cashOnCashROI = (annual_cashFlow / total_investment) * 100
        round(self.cashOnCashROI, 2)

    def runner(self): 
        while True: 
            self.income()
            self.expenses()
            self.cashFlow()
            self.cashROI()
            print(f'Your total monthly income for this property: ${self.total_income}')
            print(f'Your total monthly expenses for this property: ${self.total_expenses}')
            print(f'Your total monthly cash flow for this property: ${self.total_cashFlow}')
            print(f'Your cash on cash return for this property: {self.cashOnCashROI}%')
            break

prop = ROI()
prop.runner()