def calculate_SI(p,t,r):
    SI=(p*t*r)/100
    return SI

principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time in years: ")) 
rate = float(input("Enter the rate of interest: "))
simple_interest = calculate_SI(principal, time, rate)
print("The simple interest is:", simple_interest)