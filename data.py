import requests
from tkinter import *

THEME_COLOR = "#375362"


class GameData:
    def __init__(self):
        self.parameters = {
            "amount": 0,
            "type": "boolean",
            "category": 0
        }
        self.window = Tk()
        self.window.title("Game Parameters")
        self.window.config(padx=10, pady=15, bg=THEME_COLOR)
        self.window.iconbitmap("images\logo.ico")
        self.top_label = Label(text="Game Setup", bg=THEME_COLOR, fg="#ffffff", font=("Arial", 25, "normal"))
        self.top_label.grid(row=0, column=2, columnspan=4, pady=(0, 15))
        self.q_label = Label(text="Number of questions:", bg=THEME_COLOR, fg="#ffffff", font=("Arial", 10, "normal"))
        self.q_label.grid(row=3, column=2)
        q_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20]
        self.q_var = StringVar(self.window)
        self.q_var.set(q_options[0])
        self.q_menu = OptionMenu(self.window, self.q_var, *q_options)
        self.q_menu.config(highlightthickness=0)
        self.q_menu.grid(row=3, column=4)
        self.cat_label = Label(text="Category:", bg=THEME_COLOR, fg="#ffffff", font=("Arial", 10, "normal"))
        self.cat_label.grid(row=4, column=2)
        self.cat_options = {"General Knowledge": 9, "Entertainment: Film": 11, "Entertainment: Music": 12,
                            "Entertainment: Television": 14, "Entertainment: Video games": 15,
                            "Entertainment: Board Games": 16, "Science: Computers": 18, "Mythology": 20,
                            "Sports": 21, "Celebrities": 26, "Animals": 27, "Entertainment: Comics": 29,
                            "Science: Gadgets": 29, "Entertainment: Cartoon & Animations": 32}
        self.cat_var = StringVar(self.window)
        self.cat_var.set("Select Category")
        self.cat_menu = OptionMenu(self.window, self.cat_var, *self.cat_options.keys())
        self.cat_menu.config(highlightthickness=0)
        self.cat_menu.grid(row=4, column=4)
        self.quit_button = Button(text="Close", highlightthickness=0, command=self.quit)
        self.quit_button.grid(row=5, column=4)
        self.save_button = Button(text="Save", highlightthickness=0, command=self.get_params)
        self.save_button.grid(row=5, column=3, pady=10, padx=10)
        self.is_clicked = False
        self.window.mainloop()

    def get_params(self):
        num_of_q = int(self.q_var.get())
        category = self.cat_options[self.cat_var.get()]
        self.parameters["amount"] = num_of_q
        self.parameters["category"] = category
        response = requests.get(url="https://opentdb.com/api.php?", params=self.parameters)
        data = response.json()
        question_data = data["results"]
        return question_data

    def quit(self):
        self.window.destroy()