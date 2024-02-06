p = int(input("Enter principle amount:"))
n = int(input("Enter number of compounding periods per year "))
r = float(input("Enter interest rate "))
y = int(input("Enter the amount of years "))

fv = p * ((1 + ((r/100.0)/n)) ** (n*y))

print(f"The final amount after{y}, years is {fv}")