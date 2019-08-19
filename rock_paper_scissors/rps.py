#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  return_list = []
  one_list = ['rock','paper','scissors']

  # while True:
  for num in range(0,n**3):
    # for item in one_list:
    #   return_list[num].append(item)
    return_list.append([])

    # n -= 1
    # if n == 0:
      # break

  print(len(return_list))


  # pass 
rock_paper_scissors(3)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

#3 - 27
#2 - 9
#1 3

