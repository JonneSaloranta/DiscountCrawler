from bs4 import BeautifulSoup
import requests
import tkinter as tk
import os
from DataLoader import Discounts
import time


class Application:
    def __init__(self, width, height, title):
        self.disc = Discounts()
        self.width = width
        self.height = height
        self.title = title

    def load_timer(original_function):
        import time

        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = original_function(*args, **kwargs)
            t2 = time.time() - t1
            print(f"{original_function.__name__} ran in: {t2} sec")
            return result

        return wrapper

    @load_timer
    def reloadData(self):
        self.disc.getData
        print(f"Loaded {self.disc.getItemCount} items")

    def window(self):

        self.reloadData()
        disc = self.disc

        root = tk.Tk()
        root.title(self.title)
        root.geometry(str(self.width) + "x" + str(self.height))
        root.minsize(640, 480)
        root.update_idletasks()
        root.bind("<Escape>", lambda x: root.destroy())

        canvas = tk.Canvas(root, bg="#293b59")
        canvas.pack()
        canvas.update_idletasks()

        itemFrame = tk.Frame(root, bg="#38598f")
        itemFrame.place(relwidth=0.5, relheight=1, relx=0)

        itemFrame.update_idletasks()

        selectedFrame = tk.Frame(root, bg="#38598f")
        selectedFrame.place(relwidth=0.5, relheight=1, relx=0.5)
        selectedFrame.update_idletasks()

        label = tk.Label(itemFrame, text="All discount items")
        label.pack(padx=15, pady=15)
        label.update_idletasks()

        label1 = tk.Label(selectedFrame, text="All selected items")
        label1.pack(padx=15, pady=15)
        label1.update_idletasks()

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

        selBox = tk.Listbox(
            selectedFrame,
            width=selectedFrame.winfo_width(),
            height=int(selectedFrame.winfo_height() / 40),
            selectmode=tk.MULTIPLE,
            font=("TkDefaultFont", 12),
            activestyle="none",
            borderwidth=3,
        )
        selBox.pack(padx=15, pady=15, side=tk.TOP)
        selBox.update_idletasks()

        def addToList():
            listBox.delete(0, tk.END)
            for i in range(disc.getItemCount):
                listBox.insert(
                    tk.END,
                    str(disc.getItemName(i) + " - " + disc.getItemPrice(i) + "€"),
                )
            print("added")

        addToList()

        def reloadList():
            reloadData()
            addToList()

        btn = tk.Button(
            itemFrame,
            text="Deselect all",
            relief=tk.GROOVE,
            command=lambda: listBox.selection_clear(0, tk.END),
        )
        btn.pack(
            fill="x",
            padx=15,
            pady=10,
            ipadx=15,
            ipady=15,
            in_=itemFrame,
        )
        btn.update_idletasks()

        btn1 = tk.Button(
            itemFrame,
            text="Delete data",
            relief=tk.GROOVE,
            command=lambda: listBox.delete(0, tk.END),
        )
        btn1.pack(
            fill="x",
            padx=15,
            pady=10,
            ipadx=15,
            ipady=15,
            in_=itemFrame,
        )
        btn1.update_idletasks()

        btn2 = tk.Button(
            itemFrame,
            text="Refresh data",
            relief=tk.GROOVE,
            command=lambda: [self.reloadData(), addToList()],
        )
        btn2.pack(
            fill="x",
            padx=15,
            pady=10,
            ipadx=15,
            ipady=15,
            in_=itemFrame,
        )
        btn2.update_idletasks()

        btn3 = tk.Button(selectedFrame, text="Insert selected", relief=tk.GROOVE)
        btn3.pack(fill="x", padx=15, pady=10, ipadx=15, ipady=15, in_=selectedFrame)

        root.mainloop()


def main():
    app = Application(1280, 720, "Discounts")
    app.window()


if __name__ == "__main__":
    main()