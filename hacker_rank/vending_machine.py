#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_coins):

        self.num_items = num_items
        self.item_coins = item_coins
        self.num_coins = 0

    def buy(self, num_items, num_coins):
        # Implement the buy method here
        if num_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        if num_coins < num_items * self.item_coins:
            raise ValueError("Not enough coins")
        self.num_items -= num_items
        self.num_coins += num_coins
        return num_coins - num_items * self.item_coins
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()