import heapq

grades = [24,56,57,25,99,100]

print(heapq.nlargest(3,grades))

print(heapq.nsmallest(2,grades))

stocks = [
    {'ticker':'A','price':43},
    {'ticker':'B', 'price': 65},
    {'ticker':'C', 'price': 99},
    {'ticker': 'X', 'price': 28}
]

print(heapq.nsmallest(2,stocks, key=lambda stock: stock['price']))