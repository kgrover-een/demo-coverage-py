def calc_tax(age, income):
    if (age < 60):
        if (income <= 250000):
            tax_percent = 0  
        elif(income >= 250001 and income <= 500000):
            tax_percent = 0.1 
        elif(income >= 500001 and income <= 1000000): 
            tax_percent = 0.2 
        else:
            tax_percent = 0.3 
    elif (age >= 60 and age < 80):
        if (income <= 300000):
            tax_percent = 0 
        elif (income >= 300001 and income <= 500000): 
            tax_percent = 0.1 
        elif (income >= 500001 and income <= 1000000):
            tax_percent = 0.2 
        else:
            tax_percent = 0.3  
    else:
        if(income <= 500000):
            tax_percent = 0 
        elif (income >= 500001 and income <= 1000000):
            tax_percent = 0.2 
        else: 
            tax_percent = 0.3 
    tax = tax_percent * income
    return round(tax)