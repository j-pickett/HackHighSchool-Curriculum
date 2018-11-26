# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_mathclass.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/16 17:28:32 by apickett          #+#    #+#              #
#    Updated: 2018/10/17 12:53:48 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
import sys
from collections import Counter

def mmin(numbers):
   return min(numbers)

def mmax(numbers):
   return max(numbers)

def mode(numbers):
   return Counter(numbers).most_common(1)[0][0]

def rrange(numbers):
    return int(mmax(numbers)) - int(mmin(numbers))
def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
   sorted_x = sorted(numbers)
   length_n = len(numbers)
   middle = length_n // 2
   if length_n % 2 == 0:
       return (int(sorted_x[middle - 1]) + int(sorted_x[middle])) / 2
   return(sorted_x[middle])

def main(argv):
    ac = len(argv)
    if ac:
        argv = argv[1:]
        print("min: " + str(mmin(argv)))
        print("max: " + str(mmax(argv)))
        print("median: " + str(median(argv)))
        print("mode: " +  str(mode(argv)))
        print("range: " + str(int(rrange(argv))))

main(sys.argv)
