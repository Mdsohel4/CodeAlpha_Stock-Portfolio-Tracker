portfolio = {}

def add_stock(symbol, shares):
    portfolio[symbol] = portfolio.get(symbol, 0) + shares
    print(f"Added {shares} shares of {symbol}")

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol}")
    else:
        print("Stock not found.")

def view_portfolio():
    print("\nCurrent Portfolio:")
    for symbol, shares in portfolio.items():
        print(f"{symbol}: {shares} shares")

while True:
    print("\nOptions: add, remove, view, exit")
    choice = input("Choose an action: ").lower()

    if choice == "add":
        symbol = input("Enter stock symbol: ").upper()
        shares = int(input("Enter number of shares: "))
        add_stock(symbol, shares)
    elif choice == "remove":
        symbol = input("Enter stock symbol to remove: ").upper()
        remove_stock(symbol)
    elif choice == "view":
        view_portfolio()
    elif choice == "exit":
        break
    else:
        print("Invalid option.")
