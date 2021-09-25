import requests

API_KEY = "FTMAIZA6AGF1YALG"

def getQuote(symbol):
    global API_KEY
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}'.format(symbol, API_KEY)
    r = requests.get(url)
    
    print(r.text)
    try:
        data = r.json()
        print("The current price of {} is: {}".format(symbol, data['Global Quote']['05. price']))
        print("Stock Quotes retrieved successfully!")
    except KeyError:
        print("Invalid response")
    

def main():
    symbol = input("Stock Symbol: ").strip()
    while symbol != "quit":
        getQuote(symbol)
        symbol = input("Stock Symbol: ").strip()

if __name__ == "__main__":
    main()