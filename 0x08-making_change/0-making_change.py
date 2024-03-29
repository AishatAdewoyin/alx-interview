#!/usr/bin/python3
'''This module contains the makeChange function.'''
import sys


def makeChange(coins, total):
    '''
    determine the fewest number of coins needed to meet
    a given amount total
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0

    # Initialize the table with sys.maxsize
    table = [sys.maxsize] * (total + 1)
    table[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                change = table[i - coin]
                if change != sys.maxsize and change + 1 < table[i]:
                    table[i] = change + 1

    return table[total] if table[total] != sys.maxsize else -1
