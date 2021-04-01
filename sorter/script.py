from bs4 import BeautifulSoup
import requests
import tkinter as tk
import os
from sales import Sales


class Application:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def Window(self):

        root = tk.Tk()
        root.title(self.title)
        root.minsize(640, 480)

        sales = Sales()
        sales.getData

        canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#293b59")
        canvas.pack()

        itemFrame = tk.Frame(root, bg="#38598f")
        itemFrame.place(relwidth=0.5, relheight=1, relx=0)

        selectedFrame = tk.Frame(root, bg="#38598f")
        selectedFrame.place(relwidth=0.5, relheight=1, relx=0.5)

        label = tk.Label(root, text="Text")
        label.pack()

        openFile = tk.Button(
            itemFrame,
            text="Refresh ",
            padx=10,
            pady=5,
            fg="black",
            bg="white",
        )
        openFile.pack()

        root.mainloop()


def main():
    app = Application(1280, 720, "Alennukset")
    app.Window()


if __name__ == "__main__":
    main()