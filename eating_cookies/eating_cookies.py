#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

  # if cookies is negative, there will be 0 ways of eating cookies
  count = 0

  # only 1 way of eating 0 cookies.
  # only 1 way of eating 1 cookie
  if n == 0 or n ==1: 
    return 1
  elif n==2:
    return 2
  else:
    # arr  = ways of eating 0, 1, and 2 cookies
    arr = [1,1,2]

    # Every subsequent cookie will have a total amount of ways to eat it EQUAL to the sum of the count of the 3 below it.
    for number in range(3, n+1):
      count = arr[-3]+arr[-2]+arr[-1]
      arr.append(count)
  return count

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

    