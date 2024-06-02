#!/usr/bin/env python3

class CashRegister:
    overall_total = 0
    overall_items = []

    def __init__(self, discount=0):
        self.discount = discount
        self.items = []
        self.total = 0
        self.last_transaction = None

    def add_item(self, title="", price=0, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
        self.total += price * quantity
        CashRegister.overall_total += price * quantity
        CashRegister.overall_items += self.items
        self.last_transaction = (title, price, quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = int(self.total * (self.discount / 100))
            self.total -= discount_amount
            CashRegister.overall_total -= discount_amount
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction:
            title, price, quantity = self.last_transaction
            transaction_total = price * quantity
            
            self.total -= transaction_total
            CashRegister.overall_total -= transaction_total
            
            for _ in range(quantity):
                self.items.remove(title)
                CashRegister.overall_items.remove(title)

            # Clear the last transaction
            self.last_transaction = None


