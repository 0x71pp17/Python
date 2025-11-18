data = [
    (1500.00, "Monthly Salary"),
    (250.75, "Freelance Project"),
    (-85.99, "Online Subscription"),
    (-45.50, "Coffee Shop"),
    (500.00, "Investment Dividend"),
    (-120.00, "Electricity Bill"),
    (-300.00, "Rent Payment"),
    (75.20, "Birthday Gift"),
    (-65.30, "Dining Out"),
    (-15.99, "App Purchase"),
    (1200.00, "Consulting Fee"),
    (-220.40, "Grocery Shopping"),
    (-50.00, "Gym Membership"),
    (300.80, "Stock Sale"),
    (-25.00, "Charity Donation")
]

def print_transactions(transactions):
  for amount, statement in transactions:
    print(f"${amount} - {statement}")

def print_summary(transactions):
  deposits = [amount for amount, _ in transactions if amount >= 0]
  total_deposited = sum(deposits)
  print(f"Total Deposited: ${total_deposited:.2f}")
  
  withdrawals = [amount for amount, _ in transactions if amount < 0]
  total_withdrawn = sum(withdrawals)
  print(f"Total Withdrawn: ${total_withdrawn:.2f}")
  
  balance = total_deposited + total_withdrawn
  print(f"Balance: ${balance:.2f}")

def analyze_transactions(transactions):
  sorted_transactions = sorted(transactions)
  largest_withdrawal = sorted_transactions[0]
  largest_deposit = sorted_transactions[-1]
  print(f"Largest Withdrawal: ${largest_withdrawal[0]} - {largest_withdrawal[1]}")
  print(f"Largest Deposit: ${largest_deposit[0]} - {largest_deposit[1]}")

  deposits = [amount for amount, _ in transactions if amount > 0]
  total_deposit = sum(deposits)
  average_deposit = total_deposit / len(deposits) if deposits else 0
  print(f"Average Deposit: ${average_deposit:.2f}")

  withdrawals = [amount for amount, _ in transactions if amount < 0]
  total_withdrawal = sum(withdrawals)
  average_withdrawal = total_withdrawal / len(withdrawals) if withdrawals else 0
  print(f"Average Withdrawal: ${average_withdrawal:.2f}")

print("\nTransaction Analyzer")
while True:
  print("\nChoose an option:")
  print("1. Print summary (type 'print')")
  print("2. Analyze transactions (type 'analyze')")
  print("3. Stop program (type 'stop')")
  choice = input("Enter your option: ").strip().lower()
  
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "stop":
    break
  else:
    print("Invalid choice")   
