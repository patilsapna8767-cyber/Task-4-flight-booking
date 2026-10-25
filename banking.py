balance = 10000
print("Welcome to Kiran Bank")
print(f"Opening Balance: Rs {balance}")

# Automatic Transaction - Jaise PDF me Expected Output hai
print("\n--- Depositing Rs 1500 ---")
deposit = 1500
balance = balance + deposit
print("Deposit successful!")
print(f"Updated Balance: Rs {balance}")

print("\n--- Withdrawing Rs 2000 ---")
withdraw = 2000
if withdraw > balance:
    print("Transaction Failed: Insufficient balance.")
else:
    balance = balance - withdraw
    print("Withdrawal successful!")
    print(f"Updated Balance: Rs {balance}")

print("\n--- Trying to withdraw Rs 12000 (Should Fail) ---")
withdraw2 = 12000
if withdraw2 > balance:
    print("Transaction Failed: Insufficient balance.")
else:
    balance = balance - withdraw2
    print(f"Updated Balance: Rs {balance}")

print(f"\nFinal Balance: Rs {balance}")
print("Thank you for banking with us. Goodbye!")
