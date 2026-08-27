#Returning Values from a function
def calculate_salary(name,basic_salary,hra_percent,da_percent):
    hra=(basic_salary*hra_percent)/100
    da=(basic_salary*da_percent)/100
    gross_salary=basic_salary+hra+da
    #tax calculation according to gross salaries:
    if gross_salary<=50000:
        tax_rate=0
    elif gross_salary>50000 and gross_salary<100000:
        tax_rate=10
    elif gross_salary>=100000 and gross_salary<=150000:
        tax_rate=15
    else:
        tax_rate=20

    tax_cal=(gross_salary*tax_rate)/100
    net_salary=gross_salary-tax_cal

    return hra,da,gross_salary,tax_cal,tax_rate

