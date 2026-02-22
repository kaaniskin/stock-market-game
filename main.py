#stock market game

import tkinter as tk
from tkinter import font
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

# Window Setup with Dark Theme
root = tk.Tk()
root.title("Stock Market Game")
root.geometry("1000x800")
root.configure(bg="#1e1e1e")

# Color Scheme
BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
ACCENT_COLOR = "#00d4ff"
SUCCESS_COLOR = "#00ff41"
DANGER_COLOR = "#ff006e"
WARNING_COLOR = "#ffbe0b"

# Game data
coins = 2500
stock = 100
shares = 0
day = 0
stock_history = [100]
portfolio_history = []

news_list = [
    "the ceo retired",
    "tech bubble bursted",
    "share holds are selling",
    "CEO found on epstein files"
]

# Define custom fonts
title_font = font.Font(family="Helvetica", size=24, weight="bold")
header_font = font.Font(family="Helvetica", size=16, weight="bold")
normal_font = font.Font(family="Helvetica", size=12)
small_font = font.Font(family="Helvetica", size=10)

# Top frame for title and stats
top_frame = tk.Frame(root, bg=BG_COLOR)
top_frame.pack(fill=tk.X, padx=20, pady=20)

title_label = tk.Label(top_frame, text="💹 STOCK MARKET GAME", font=title_font, bg=BG_COLOR, fg=ACCENT_COLOR)
title_label.pack()

# Stats frame
stats_frame = tk.Frame(root, bg="#2d2d2d", relief=tk.RAISED, bd=2)
stats_frame.pack(fill=tk.X, padx=20, pady=10)

coins_label = tk.Label(stats_frame, text=f"💰 Coins: ${coins}", font=header_font, bg="#2d2d2d", fg=SUCCESS_COLOR)
coins_label.pack(side=tk.LEFT, padx=20, pady=15)

stock_label = tk.Label(stats_frame, text=f"📈 Stock Price: ${stock}", font=header_font, bg="#2d2d2d", fg=ACCENT_COLOR)
stock_label.pack(side=tk.LEFT, padx=20, pady=15)

shares_label = tk.Label(stats_frame, text=f"📊 Shares: {shares}", font=header_font, bg="#2d2d2d", fg=WARNING_COLOR)
shares_label.pack(side=tk.LEFT, padx=20, pady=15)

day_label = tk.Label(stats_frame, text=f"📅 Day: {day}", font=header_font, bg="#2d2d2d", fg=ACCENT_COLOR)
day_label.pack(side=tk.LEFT, padx=20, pady=15)

# News section
news_frame = tk.Frame(root, bg="#2d2d2d", relief=tk.SUNKEN, bd=2)
news_frame.pack(fill=tk.X, padx=20, pady=10)

news_label = tk.Label(news_frame, text="📰 News: Market Opening...", font=header_font, bg="#2d2d2d", fg=DANGER_COLOR, wraplength=900)
news_label.pack(padx=15, pady=15)

# Create frame for graphs
graph_frame = tk.Frame(root, bg=BG_COLOR)
graph_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Create figure with dark theme
fig = Figure(figsize=(10, 4), dpi=100, facecolor="#2d2d2d", edgecolor=ACCENT_COLOR)
ax1 = fig.add_subplot(121, facecolor="#1e1e1e")
ax2 = fig.add_subplot(122, facecolor="#1e1e1e")

# Setup stock price graph
ax1.set_title("Stock Price History", color=ACCENT_COLOR, fontsize=12, weight="bold")
ax1.set_xlabel("Day", color=FG_COLOR)
ax1.set_ylabel("Price ($)", color=FG_COLOR)
ax1.set_ylim(40, 160)
ax1.grid(True, alpha=0.2, color=ACCENT_COLOR)
ax1.tick_params(colors=FG_COLOR)
ax1.spines['bottom'].set_color(FG_COLOR)
ax1.spines['left'].set_color(FG_COLOR)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Setup portfolio value graph
ax2.set_title("Portfolio Value Over Time", color=SUCCESS_COLOR, fontsize=12, weight="bold")
ax2.set_xlabel("Day", color=FG_COLOR)
ax2.set_ylabel("Total Value ($)", color=FG_COLOR)
ax2.grid(True, alpha=0.2, color=SUCCESS_COLOR)
ax2.tick_params(colors=FG_COLOR)
ax2.spines['bottom'].set_color(FG_COLOR)
ax2.spines['left'].set_color(FG_COLOR)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def update_graphs():
    """Update both graphs with current data"""
    ax1.clear()
    ax1.plot(range(len(stock_history)), stock_history, marker='o', color=ACCENT_COLOR, linewidth=2.5, markersize=6)
    ax1.set_title("Stock Price History", color=ACCENT_COLOR, fontsize=12, weight="bold")
    ax1.set_xlabel("Day", color=FG_COLOR)
    ax1.set_ylabel("Price ($)", color=FG_COLOR)
    ax1.set_ylim(40, 160)
    ax1.grid(True, alpha=0.2, color=ACCENT_COLOR)
    ax1.tick_params(colors=FG_COLOR)
    ax1.set_facecolor("#1e1e1e")
    ax1.spines['bottom'].set_color(FG_COLOR)
    ax1.spines['left'].set_color(FG_COLOR)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    ax2.clear()
    ax2.plot(range(len(portfolio_history)), portfolio_history, marker='s', color=SUCCESS_COLOR, linewidth=2.5, markersize=6)
    ax2.set_title("Portfolio Value Over Time", color=SUCCESS_COLOR, fontsize=12, weight="bold")
    ax2.set_xlabel("Day", color=FG_COLOR)
    ax2.set_ylabel("Total Value ($)", color=FG_COLOR)
    ax2.grid(True, alpha=0.2, color=SUCCESS_COLOR)
    ax2.tick_params(colors=FG_COLOR)
    ax2.set_facecolor("#1e1e1e")
    ax2.spines['bottom'].set_color(FG_COLOR)
    ax2.spines['left'].set_color(FG_COLOR)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    canvas.draw()

def calculate_portfolio_value():
    """Calculate total portfolio value (coins + shares worth)"""
    return coins + (shares * stock)

def update_stock():
    global stock, day, coins, shares
    day += 1
    
    news = random.choice(news_list)
    news_label.config(text=f"📰 News: {news.upper()}")
    
    if news == "the ceo retired":
        stock -= random.randint(1, 10)
        news_label.config(fg=DANGER_COLOR)
    elif news == "tech bubble bursted":
        stock += random.randint(1, 10)
        news_label.config(fg=SUCCESS_COLOR)
    elif news == "share holds are selling":
        stock += random.randint(1, 10)
        news_label.config(fg=SUCCESS_COLOR)
    elif news == "CEO found on epstein files":
        stock -= random.randint(1, 10)
        news_label.config(fg=DANGER_COLOR)
    
    if stock < 50:
        stock = 50
    if stock > 150:
        stock = 150
    
    stock_history.append(stock)
    portfolio_value = calculate_portfolio_value()
    portfolio_history.append(portfolio_value)
    
    stock_label.config(text=f"📈 Stock Price: ${stock}")
    day_label.config(text=f"📅 Day: {day}")
    update_graphs()

def buy_stock():
    global coins, shares
    
    if coins >= stock:
        coins -= stock
        shares += 1
        coins_label.config(text=f"💰 Coins: ${coins}")
        shares_label.config(text=f"📊 Shares: {shares}")
        portfolio_history[-1] = calculate_portfolio_value() if portfolio_history else calculate_portfolio_value()
        news_label.config(text="✅ Successfully bought 1 share!", fg=SUCCESS_COLOR)
        update_graphs()
    else:
        news_label.config(text="❌ Not enough coins to buy!", fg=DANGER_COLOR)

def sell_stock():
    global coins, shares
    
    if shares > 0:
        shares -= 1
        coins += stock
        coins_label.config(text=f"💰 Coins: ${coins}")
        shares_label.config(text=f"📊 Shares: {shares}")
        portfolio_history[-1] = calculate_portfolio_value() if portfolio_history else calculate_portfolio_value()
        news_label.config(text="✅ Successfully sold 1 share!", fg=SUCCESS_COLOR)
        update_graphs()
    else:
        news_label.config(text="❌ Not enough shares to sell!", fg=DANGER_COLOR)

# Button frame
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(fill=tk.X, padx=20, pady=20)

# Styled buttons
def create_button(parent, text, command, color):
    btn = tk.Button(parent, text=text, command=command, font=header_font, 
                    bg=color, fg="black", padx=20, pady=15, 
                    relief=tk.RAISED, bd=2, activebackground=color, 
                    activeforeground="black", cursor="hand2")
    return btn

buy_btn = create_button(button_frame, "💳 BUY STOCK", buy_stock, SUCCESS_COLOR)
buy_btn.pack(side=tk.LEFT, padx=10)

sell_btn = create_button(button_frame, "💸 SELL STOCK", sell_stock, DANGER_COLOR)
sell_btn.pack(side=tk.LEFT, padx=10)

next_day_btn = create_button(button_frame, "⏭️  NEXT DAY", update_stock, ACCENT_COLOR)
next_day_btn.pack(side=tk.LEFT, padx=10)

# Initialize portfolio history
portfolio_history.append(calculate_portfolio_value())

root.mainloop()