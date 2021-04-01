from bs4 import BeautifulSoup
import requests
import tkinter as tk
import os
from DataLoader import Sales


class Application:
    def __init__(self, width, height, title):
        self.sales = Sales()
        self.width = width
        self.height = height
        self.title = title

    def reloadData(self):
        self.sales.getData
        print(f"Loaded {self.sales.getItemCount} items")

    def window(self):

        sales = self.sales
        sales.getData

        root = tk.Tk()
        root.title(self.title)
        root.geometry(str(self.width) + "x" + str(self.height))
        root.minsize(640, 480)
        root.update_idletasks()
        root.bind("<Escape>", lambda x: root.destroy())

        canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#293b59")
        canvas.pack()
        canvas.update_idletasks()

        itemFrame = tk.Frame(root, bg="#38598f")
        itemFrame.place(relwidth=0.5, relheight=1, relx=0)

        itemFrame.update_idletasks()

        selectedFrame = tk.Frame(root, bg="#38598f", borderwidth=10)
        selectedFrame.place(relwidth=0.5, relheight=1, relx=0.5)
        selectedFrame.update_idletasks()

        label = tk.Label(itemFrame, text="All sales items")
        label.pack(ipadx=200, padx=15, pady=15)
        label.update_idletasks()

        listBox = tk.Listbox(
            itemFrame,
            width=itemFrame.winfo_width(),
            height=int(itemFrame.winfo_height() / 40),
            selectmode=tk.MULTIPLE,
            font=("TkDefaultFont", 12),
            activestyle="none",
            borderwidth=3,
        )
        listBox.pack(padx=15, pady=15, side=tk.TOP)
        listBox.update_idletasks()

        for i in range(sales.getItemCount):
            listBox.insert(
                tk.END, str(sales.getItemName(i) + " - " + sales.getItemPrice(i) + "€")
            )

        btn = tk.Button(
            itemFrame, text="Refresh data", command=lambda: self.reloadData()
        )
        btn.pack()
        btn.update_idletasks()

        root.mainloop()


def main():
    app = Application(1280, 720, "Alennukset")
    app.window()


if __name__ == "__main__":
    main()