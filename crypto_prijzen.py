import tkinter as tk
import requests

class CryptoPricesApp:
    def __init__(self, master):
        self.master = master
        master.title("Crypto Prices in Euro")
        self.btc_price = tk.StringVar()
        self.eth_price = tk.StringVar()
        self.ada_price = tk.StringVar()
        self.btc_change = tk.StringVar()
        self.eth_change = tk.StringVar()
        self.ada_change = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="BTC Price in Euro:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.master, textvariable=self.btc_price).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.master, textvariable=self.btc_change).grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self.master, text="ETH Price in Euro:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.master, textvariable=self.eth_price).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.master, textvariable=self.eth_change).grid(row=1, column=2, padx=5, pady=5)
        tk.Label(self.master, text="ADA Price in Euro:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.master, textvariable=self.ada_price).grid(row=2, column=1, padx=5, pady=5)
        tk.Label(self.master, textvariable=self.ada_change).grid(row=2, column=2, padx=5, pady=5)

        self.update_prices()

    def update_prices(self):
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Ccardano&vs_currencies=eur&include_24hr_change=true")
        prices = response.json()
        self.btc_price.set("{:.2f}".format(prices["bitcoin"]["eur"]))
        self.eth_price.set("{:.2f}".format(prices["ethereum"]["eur"]))
        self.ada_price.set("{:.2f}".format(prices["cardano"]["eur"]))
        self.btc_change.set("{:.2f}%".format(prices["bitcoin"]["eur_24h_change"]))
        self.eth_change.set("{:.2f}%".format(prices["ethereum"]["eur_24h_change"]))
        self.ada_change.set("{:.2f}%".format(prices["cardano"]["eur_24h_change"]))
        self.master.after(60000, self.update_prices) # Update prices every minute

root = tk.Tk()
app = CryptoPricesApp(root)
root.mainloop()
