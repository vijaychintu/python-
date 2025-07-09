# Get user inputs
total_price = float(input("Enter the total price of the item: "))
down_payment = float(input("Enter the down payment amount: "))
r = float(input("Enter the annual interest rate (%): "))
n = int(input("Enter the tenure in years: "))

# Calculate the principal (loan amount)
p = total_price - down_payment

# Monthly interest rate and tenure in months
monthly_rate = r / (12 * 100)
tenure_months = n * 12

# EMI calculation
emi = (p * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
      ((1 + monthly_rate) ** tenure_months - 1)

# Total payable and interest
total_payable = emi * tenure_months
total_interest = total_payable - p

# Output
print(f"\nLoan Amount (after down payment): ₹{p:,.2f}")
print(f"Monthly EMI: ₹{emi:,.2f}")
print(f"Total Payable Amount over {n} years: ₹{total_payable:,.2f}")
print(f"Total Interest Paid: ₹{total_interest:,.2f}")
