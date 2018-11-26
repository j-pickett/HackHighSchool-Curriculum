# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_parentheses.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/06 12:25:54 by apickett          #+#    #+#              #
#    Updated: 2018/10/13 14:43:54 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def	capit(string):
	ret = ""
	i = True
	for c in string:
		if i:
			ret += c.upper()
		else:
			ret += c.lower()
		if c.isalpha():
			i = not i
	return ret

#read in the capit string and only turn cap AEIOU into *
def     star(string):
    newstr = str(capit(string))
    vowels = ('A', 'E', 'I', 'O', 'U')
    for c in newstr:
        if c in vowels:
            newstr = newstr.replace(c, "*")
    return newstr
    return 
def	thanos(string):
	open_count = 0
	close_count = 0
	for c in string:
		if c == '(':
			open_count += 1
		elif c == ')':
			close_count += 1
	return open_count == close_count

def	main(argv):
	ac = len(argv)
	if ac == 2:
            print(capit(argv[1]))
            print(star(argv[1]))
            print("Would Thanos be pleased? {}".format(thanos(argv[1])))

main(sys.argv)
