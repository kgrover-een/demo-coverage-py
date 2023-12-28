from typing import List

class Shop:
    def __init__(self) -> None:
        self.items: List[str] = []

    def add(self, item:str):
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_list):
        pass