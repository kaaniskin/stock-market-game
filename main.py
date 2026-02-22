#stock market game

import tkinter as tk
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

# Window
root = tk.Tk()
root.title("Stock Game")
root.geometry("900x700")

# Game data
coins = 2500
stock = 100
shares = 0
day = 0
stock_history = [100]  # Track stock price history
portfolio_history = []  # Track portfolio value history

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

day_label = tk.Label(root, text=f"Day: {day}", font=("Arial", 12))
day_label.pack()

news_label = tk.Label(root, text="News:", font=("Arial", 12))
news_label.pack(pady=5)

# Create frame for graphs
graph_frame = tk.Frame(root)
graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create figure with two subplots
fig = Figure(figsize=(9, 4), dpi=100)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Setup stock price graph
ax1.set_title("Stock Price History")
ax1.set_xlabel("Day")
ax1.set_ylabel("Price")
ax1.set_ylim(40, 160)
ax1.grid(True, alpha=0.3)

# Setup portfolio value graph
ax2.set_title("Portfolio Value Over Time")
ax2.set_xlabel("Day")
ax2.set_ylabel("Total Value ($)")
ax2.grid(True, alpha=0.3)

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def update_graphs():
    """Update both graphs with current data"""
    ax1.clear()
    ax1.plot(range(len(stock_history)), stock_history, marker='o', color='blue', linewidth=2)
    ax1.set_title("Stock Price History")
    ax1.set_xlabel("Day")
    ax1.set_ylabel("Price")
    ax1.set_ylim(40, 160)
    ax1.grid(True, alpha=0.3)
    
    ax2.clear()
    ax2.plot(range(len(portfolio_history)), portfolio_history, marker='o', color='green', linewidth=2)
    ax2.set_title("Portfolio Value Over Time")
    ax2.set_xlabel("Day")
    ax2.set_ylabel("Total Value ($)")
    ax2.grid(True, alpha=0.3)
    
    canvas.draw()

def calculate_portfolio_value():
    """Calculate total portfolio value (coins + shares worth)"""
    return coins + (shares * stock)

def update_stock():
    global stock, day, coins, shares
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
    
    # Update history
    stock_history.append(stock)
    portfolio_value = calculate_portfolio_value()
    portfolio_history.append(portfolio_value)
    
    stock_label.config(text=f"Stock Price: {stock}")
    day_label.config(text=f"Day: {day}")
    update_graphs()

def buy_stock():
    global coins, shares
    
    if coins >= stock:
        coins -= stock
        shares += 1
        coins_label.config(text=f"Coins: {coins}")
        shares_label.config(text=f"Shares: {shares}")
        portfolio_history[-1] = calculate_portfolio_value() if portfolio_history else calculate_portfolio_value()
        update_graphs()
    else:
        news_label.config(text="Not enough coins to buy!")

def sell_stock():
    global coins, shares
    
    if shares > 0:
        shares -= 1
        coins += stock
        coins_label.config(text=f"Coins: {coins}")
        shares_label.config(text=f"Shares: {shares}")
        portfolio_history[-1] = calculate_portfolio_value() if portfolio_history else calculate_portfolio_value()
        update_graphs()
    else:
        news_label.config(text="Not enough shares to sell!")

# Buttons
tk.Button(root, text="Buy Stock", command=buy_stock).pack(pady=5)
tk.Button(root, text="Sell Stock", command=sell_stock).pack(pady=5)
tk.Button(root, text="Next Day", command=update_stock).pack(pady=10)

# Initialize portfolio history
portfolio_history.append(calculate_portfolio_value())

root.mainloop()