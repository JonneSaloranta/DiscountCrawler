from bs4 import BeautifulSoup
import requests


class Sales:

    itemCount = 0
    productList = []
    priceList = []

    def __init__(self):
        """Sales class init"""
        print("Sales init")

    @property
    def getData(self):
        """Load sales data from lidl website"""
        self.productList = []
        self.priceList = []
        self.itemCount = 0
        src = requests.get("https://www.lidl.fi/tarjoukset").text

        soup = BeautifulSoup(src, "lxml")

        products = soup.find_all("article", class_="product product--tile")

        for product in products:

            try:
                src_product_title = product.find("h3", class_="product__title").text
                product_title = " ".join(src_product_title.split())
                self.productList.append(product_title)

            except Exception:
                product_title = "Null"
                self.productList.append(product_title)

            try:
                src_product_price = product.find("span", class_="pricebox__price").text
                product_price = " ".join(src_product_price.split())
                self.priceList.append(product_price)

            except Exception:
                product_price = "Null"
                self.priceList.append(product_price)

            self.itemCount += 1

    @property
    def getItemCount(self):
        """Returns sales item count

        Returns:
            int: itemCount
        """
        return self.itemCount

    def getItemName(self, number):
        """Get item from sale item list

        Args:
            number (int): n item from the list

        Returns:
            str: returns a item name
        """
        return self.productList[number]

    def getItemPrice(self, number):
        return self.priceList[number]

    @property
    def displayAllItems(self):
        """Returns with all of the items in a sales list"""
        for (item, price) in zip(self.productList, self.priceList):
            print(str(item + " - " + price))


def _test():
    sales = Sales()
    sales.getData
    print(sales.getItemCount)
    sales.displayAllItems


if __name__ == "__main__":
    _test()