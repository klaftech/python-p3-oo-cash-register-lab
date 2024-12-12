#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
      self.discount = discount
      self.total = 0
      self.items = []
      self.last_transaction = {
         "price": 0,
         "qty": 0
      }

  def reset_register_totals(self):
      self.total = 0

  def add_item(self,product,price,qty=1):
      calc_total = (price * qty)
      new_total = self.total + calc_total
      #print(f"Prev Total: {self.total}. price: {price}. qty: {qty}. total add {calc_total}. new total: {new_total}")
      self.total = new_total
      self.last_transaction["price"] = price
      self.last_transaction["qty"] = qty
      for i in range(qty):
         self.items.append(product)

  def apply_discount(self):
      if self.discount == 0:
          print("There is no discount to apply.")
      else:
        sum = int(self.total - (self.discount/100) * self.total)
        self.total = sum
        print("After the discount, the total comes to $800.")

  def void_last_transaction(self):
     self.items.pop()
     self.total -= self.last_transaction["price"] * self.last_transaction["qty"]