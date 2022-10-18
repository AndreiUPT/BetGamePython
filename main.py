from tkinter import *
import random

root = Tk()
root.title('Andrei Casino')
root.geometry('1000x500')
root.configure(background='purple')

balance = 1

def main():
    global currentBalance

    titleGame = Label(root, text='The GUESS NUMBER game', bg='purple', fg='yellow')
    titleGameFont = ('Arial', 47, 'bold')
    titleGame.configure(font=titleGameFont)
    titleGame.grid(row=2, column=1, rowspan=2, columnspan=30, padx=150)

    currentBalance = Label(root, text=f"Your current balance is: {balance} EURO", bg='purple', fg='yellow')
    balanceFont = ('Arial', 24)
    currentBalance.configure(font=balanceFont)
    currentBalance.grid(row=17, column=2, rowspan=15, columnspan=15, padx=10, pady=10)

    increaseMessage = Label(root, text = 'You have to pay the rest of the money if your balance is < 0!', bg = 'purple', fg = 'yellow')
    increaseFont = ('Arial', 15)
    increaseMessage.configure(font = increaseFont)
    increaseMessage.grid(row=40, column=1, rowspan=15, columnspan=15, padx=10, pady=20)

    investButton = Button(root, text="Increase balance", bd=2, height=2, width=10, command=increase)
    investButton.grid(column=12, row=20, rowspan=16, columnspan=15, padx=3, pady=10)


def increase():
    global balance

    currentBalance.destroy()
    balance+=100
    currentBalanceIncreased = Label(root, text=f"Your current balance is: {balance} EURO", bg='purple', fg='yellow')
    balanceFontIncreased = ('Arial', 24)
    currentBalanceIncreased.configure(font=balanceFontIncreased)
    currentBalanceIncreased.grid(row=17, column=2, rowspan=15, columnspan=15, padx=10, pady=10)

def betGame():
    global balance, R, random_number

    number_list = [1, 2, 3, 4, 5]
    random_number = random.choice(number_list)
    number_label = Label(root, text = f"The number of the game is: {random_number}", bg = 'purple', fg = 'yellow')
    number_font = ('Arial', 30)
    number_label.configure(font = number_font)
    number_label.grid(row=500, column=2, rowspan=150, columnspan=15, padx=10, pady=10)


def betChoose():
    global entry_number, N

    chooseLabel = Label(root, text = "Choose a number from range [1,5]: ", bg = 'purple', fg = 'yellow')
    chooseFont = ('Arial', 24)
    chooseLabel.configure(font = chooseFont)
    chooseLabel.grid(row=90, column=2, rowspan=15, columnspan=15, padx=10, pady=10)

    entry_number = Entry(root, width=2, bg="yellow", fg="purple")
    entry_number_font = ('Arial', 24)
    entry_number.configure(font = entry_number_font)
    entry_number.grid(row=90, column = 10, rowspan=16, columnspan=15, padx=3, pady=10)

    betButton = Button(root, text="Bet", bd=2, height=2, width=6, command = actionBetButton)
    betButton.grid(column=14, row=90, rowspan=16, columnspan=15, padx=3, pady=10)


def win():
    Win = Label(root, text="Bravo,you won 100 euro!", bg='purple', fg='yellow')
    Win_font = ('Arial', 30)
    Win.configure(font=Win_font)
    Win.grid(row=900, column = 12, rowspan=16, columnspan=15, padx=3, pady=10)

def loose():
    Loose = Label(root, text="Oops,you lost 55 euro!", bg='purple', fg='yellow')
    Loose_font = ('Arial', 30)
    Loose.configure(font=Loose_font)
    Loose.grid(row=900, column = 12, rowspan=16, columnspan=15, padx=3, pady=10)


def actionBetButton():
    global balance

    N = int(entry_number.get())
    betGame()
    R = random_number

    if N == R:
        currentBalance.destroy()
        balance += 100
        currentBalanceWin = Label(root, text=f"Your current balance is: {balance} EURO", bg='purple', fg='yellow')
        balanceFontWin = ('Arial', 24)
        currentBalanceWin.configure(font=balanceFontWin)
        currentBalanceWin.grid(row=17, column=2, rowspan=15, columnspan=15, padx=10, pady=10)
        win()
    else:
        currentBalance.destroy()
        balance -= 55
        currentBalanceWin = Label(root, text=f"Your current balance is: {balance} EURO", bg='purple', fg='yellow')
        balanceFontWin = ('Arial', 24)
        currentBalanceWin.configure(font=balanceFontWin)
        currentBalanceWin.grid(row=17, column=2, rowspan=15, columnspan=15, padx=10, pady=10)
        loose()


main()
betChoose()
root.mainloop()
