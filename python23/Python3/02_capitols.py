# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_capitols.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/16 16:14:57 by apickett          #+#    #+#              #
#    Updated: 2018/10/16 16:14:58 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv

def dict_data(csv_file):
    data = {
            "state": {},
            "capital": {}
            }
    with open("capitols.csv") as cap:
        read = csv.DictReader(cap)
        for row in read:
                state = row["State"].lower()
                capital = row["Capital"].lower()
                data["state"][state] = capital
                data["capital"][capital] = state
    return data

if __name__ == "__main__":
	data = dict_data("capitols.csv")
	loop = None
	while loop != "done":
		loop = input("Ready: ").strip().lower()
		print(data["state"].get(loop,data["capital"].get(loop, "nil")))
