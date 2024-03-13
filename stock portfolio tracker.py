def main():
    portfolio = {}

    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            get_new_stock(portfolio)
        elif choice == '2':
            remove_stock(portfolio)
        elif choice == '3':
            view_portfolio(portfolio)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Enter a valid choice Please try again....!.")

def get_new_stock(portfolio):
    symbol = input("Enter stock symbol: ")
    shares = int(input("Enter number of shares: "))
    price = float(input("Enter purchase price per share: "))
    portfolio[symbol] = {'Shares': shares, 'Price': price}
    print(f"{shares} shares of {symbol} added to portfolio.")

def remove_stock(portfolio):
    symbol = input("Enter stock symbol to remove: ")
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from portfolio.")
    else:
        print(f"{symbol} not found in portfolio.")

def view_portfolio(portfolio):
    print("\nTotal Stocks\n\n ")
    
    print("Symbol\tShares\tPrice    Total worth")
    total_value = 0
    for symbol, details in portfolio.items():
        shares = details['Shares']
        price = details['Price']
        total = shares * price
        total_value += total
        print(f"{symbol}\t{shares}\t${price:.2f}\t    ${total}")
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")
    

if __name__ == "__main__":
    main()

