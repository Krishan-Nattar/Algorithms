#!/usr/bin/python

import sys
# resultarray = []
# a= [1,2,3]
# b= [5,6,7]

# resultarray.append(a.pop(0))

# resultarray.append(a[0])
# a = a[1:]
total = 0
count = 0
sub_count = 1
# def making_change(amount, denominations):
#   global total
#   holding = [1] * amount
#   new_array = []
#   if len(holding) < 5:
#     total += 1
#   else:

#   return total

#   0,1,5,10,25
# # [1,1,1,1,1,2,2,2,2,2,2]
def making_change(amount, denominations):

  test = [1] * (amount +1)

  for index in denominations:
    if index != 1:
      for place in range(index, amount + 1):
        test[place] = test[place] + test[place - index]
  return test[amount]



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")