#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  value = 0
  chosen = []
  testvalue = []
  test = []

  # run through the list of items and find all iterations of items

  # if a current iteration has a higher value than the previous iteration (while also being at or below capacity)...

  # replace the value and chosen array with current iteration and keep going

  # While True:
    for obj in items:
      print(obj.index)
      print(obj.size)
      print(obj.value)
  # print("******************************")
  # print(capacity)
  # print("******************************")
  return {'Value': value, 'Chosen': chosen}
  # pass
  # {'Value': 197, 'Chosen': [1, 7, 8]}

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')