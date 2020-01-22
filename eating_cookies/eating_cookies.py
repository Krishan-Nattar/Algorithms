#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

  arr = [1,1,2] + [0] * (n-2)
    # Every subsequent cookie will have a total amount of ways to eat it EQUAL to the sum of the count of the 3 below it.
  for number in range(3, n+1):
    arr[number] = arr[number-3]+arr[number-2]+arr[number-1]
  return arr[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

    