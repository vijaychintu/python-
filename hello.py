p = float(input("Enter the loan amount: "))
r = float(input("Enter the annual interest rate (%): "))
n = int(input("Enter the tenure in years: "))

monthly_rate = r / (12 * 100)
tenure_months = n * 12

emi = (p * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
      ((1 + monthly_rate) ** tenure_months - 1)

print(emi)


