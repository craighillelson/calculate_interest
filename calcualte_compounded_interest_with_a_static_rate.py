import math


def compound_interest(p, r, t):
    amount = p * (math.pow((1 + (r/100)), t))
    amount_rounded = round(amount, 2)
    print(f"\nPrincipal plus interest: ${amount_rounded:,}")
    return amount_rounded


def output_interest_earned():
    interest_earned = amount_rounded - principal
    interest_earned_rounded = f"${round(amount_rounded - principal, 2):,}"
    print(f"Compounded interest: {interest_earned_rounded}\n")


principal = float(input("\nEnter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time Period in years: "))
amount_rounded = compound_interest(principal, rate, time)
output_interest_earned()
