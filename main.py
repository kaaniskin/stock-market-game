#stock market game

import tkinter as tk
import random

# Window
root = tk.Tk()
root.title("Stock Game")

# Game data
coins = 2500
stock = 100
shares = 0
day = 0

news_list = [
    "the ceo retired",
    "tech bubble bursted",
    "share holds are selling",
    "CEO found on epstin files"
]

# UI labels
coins_label = tk.Label(root, text=f"Coins: {coins}", font=("Arial", 16))
coins_label.pack()

stock_label = tk.Label(root, text=f"Stock Price: {stock}", font=("Arial", 16))
stock_label.pack(pady=10)

shares_label = tk.Label(root, text=f"Shares: {shares}", font=("Arial", 12))
shares_label.pack()

news_label = tk.Label(root, text="News:", font=("Arial", 12))
news_label.pack(pady=5)

def update_stock():
    global stock
    day += 1

    news = random.choice(news_list)
    news_label.config(text=f"News: {news}")

    if news == "the ceo retired":
        stock -= random.randint(1, 10)
    elif news == "tech bubble bursted":
        stock += random.randint(1, 10)
    elif news == "share holds are selling":
        stock += random.randint(1, 10)
    elif news == "CEO found on epstin files":
        stock -= random.randint(1, 10)

    if stock < 50:
        stock = 50
    if stock > 150:
        stock = 150





    stock_label.config(text=f"Stock Price: {stock}")

def buy_stock():
    global coins, shares

    if coins >= stock:
        coins -= stock
        shares += 1
        coins_label.config(text=f"Coins: {coins}")
        shares_label.config(text=f"Shares: {shares}")
    else:
        news_label.config(text="Not enough coins to buy!")

def sell_stock():
    global coins, shares

    if shares > 0:
        shares -= 1
        coins += stock
        coins_label.config(text=f"Coins: {coins}")
        shares_label.config(text=f"Shares: {shares}")
    else:
        news_label.config(text="Not enough shares to sell!")

# Buttons
tk.Button(root, text="Buy Stock", command=buy_stock).pack(pady=5)
tk.Button(root, text="Sell Stock", command=sell_stock).pack(pady=5)
tk.Button(root, text="Next Day", command=update_stock).pack(pady=10)

root.mainloop()