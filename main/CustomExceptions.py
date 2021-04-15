class ProductTitleException(Exception):
    def __init__(self):
        print("Product title is not valid!")


class ProductPriceException(Exception):
    def __init__(self):
        print("Product price is not valid!")