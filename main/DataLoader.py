from bs4 import BeautifulSoup
import requests
import json
import CustomExceptions

# -*- coding: utf-8 -*-

path = "./"
fileName = "data"

data = {}
data["Products"] = []

ce = CustomExceptions


class Discounts:

    itemCount = 0
    productList = []
    priceList = []

    def __init__(self):
        """Discount class init"""
        print("Discount init")

    @staticmethod
    def WriteToJsonFile(path, fileName, data):
        """Writes data into json file

        Args:
            path (str): Filepath
            fileName (str): Json file name
            data (str): Data to be dumped into json file
        """

        filePathNameWithExt = "./" + path + "/" + fileName + ".json"
        content = None
        with open(filePathNameWithExt, "r", encoding="utf-8") as of:
            content = json.load(of)

        if content != data:
            print("Saved new data!")
            with open(filePathNameWithExt, "w", encoding="utf-8") as fp:
                json.dump(data, fp, sort_keys=True, indent=4, ensure_ascii=False)
        else:
            print("New data is the same as the old data!")

    @staticmethod
    def ReadJsonData(path, fileName):
        """Reads data from json file

        Args:
            path (str): Filepath
            fileName (str): File name for file to be read
        """
        filePathNameWithExt = "./" + path + "/" + fileName + ".json"
        with open(filePathNameWithExt) as of:
            content = json.load(of)

    def parseData(self, bs4set):
        """Parses data in to an array.

        Args:
            bs4set (bs4.element.ResultSet): Type must be bs4.element.ResultSet

        Raises:
            ValueError: Raises ValueError if bs4set type is not bs4.element.ResultSet
            ce.ProductTitleException: Raises ProductTitleException if title is not a string
            ce.ProductPriceException: Raises ProductPriceException if title is not a string
        """
        if isinstance(bs4set, type("bs4.element.ResultSet")):
            raise ValueError("File type must be bs4.element.ResultSet")

        for product in bs4set:
            try:
                src_product_title = product.find("h3", class_="product__title").text
                src_product_price = product.find("span", class_="pricebox__price").text

                if type(src_product_title) is not str:
                    raise ce.ProductTitleException

                if type(src_product_price) is not str:
                    raise ce.ProductPriceException

                product_title = " ".join(src_product_title.split())
                product_price = " ".join(src_product_price.split())

                self.productList.append(product_title)
                self.priceList.append(product_price)

                self.itemCount += 1

                temp = {"name": product_title, "price": product_price}

                data["Products"].append(temp)
            except Exception as e:
                print(e)

    @property
    def getData(self):
        """""Load discount data from lidl website""" ""
        src = requests.get("https://www.lidl.fi/tarjoukset").text

        soup = BeautifulSoup(src, "lxml")

        products = soup.find_all("article", class_="product product--tile")

        self.parseData(products)
        self.WriteToJsonFile(path, fileName, data)
        self.ReadJsonData(path, fileName)

    @property
    def getItemCount(self):
        """Returns discount item count

        Returns:
            int: itemCount
        """
        return self.itemCount

    def getItemName(self, number):
        """Get item from discount item list

        Args:
            number (int): n item from the list

        Returns:
            str: returns a item name
        """
        return self.productList[number]

    def getItemPrice(self, number):
        return self.priceList[number]

    def displayAllItems(self, path, fileName):
        content = None

        filePathNameWithExt = "./" + path + "/" + fileName + ".json"
        with open(filePathNameWithExt) as of:
            content = json.load(of)

        for i in content["Products"]:
            print(i["name"], i["price"])


def _test():
    disc = Discounts()
    disc.getData
    print(disc.getItemCount)
    disc.displayAllItems(path, fileName)


if __name__ == "__main__":
    _test()