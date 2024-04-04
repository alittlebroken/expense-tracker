"""Expense class

Keyword arguments:
name - Name of the expense
amount - Who much money did the expense cost
category - Which category does the expense belong in
type - The type of expense ( credit or Debit )

Return: return_description
"""
class Expense:
    def __init__(self, name, amount, category, type):
        self.name = name
        self.amount = amount
        self.category = category
        self.type = type