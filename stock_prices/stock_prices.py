#!/usr/bin/python

import argparse

def find_max_profit(prices):

  #take in prices
  print(prices)

  #split prices into an array based on spaces

  #take first item

  #for every other item... subtract the first item. Whichever is the biggest number, store that.

  #go to next item. If any subsequent item minus current item is larger than the previously stored item, replace stored item.

  #if last item in array, don't do anything.

  #return final stored item




  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))