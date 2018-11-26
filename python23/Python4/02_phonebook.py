# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_phonebook.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/17 17:17:49 by apickett          #+#    #+#              #
#    Updated: 2018/10/17 21:57:37 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import collections
import csv

if __name__ == "__main__":
	with open("names.txt") as file:
		first = collections.defaultdict(list)
		last = collections.defaultdict(list)
		reader = csv.DictReader(file)
		for line in reader:
			first[line["first"]].append(line["last"])
			last[line["last"]].append(line["first"])

	print("** Shared First Names! **")
	for key, value in first.items():
		print(f"{key} ({len(value)}): {value}")


	print("** Shared Last Names! **")
	for key, value in last.items():
		print(f"{key} ({len(value)}): {value}")
