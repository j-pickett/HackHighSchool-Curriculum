# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    04_arrmatey.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/05 17:14:22 by apickett          #+#    #+#              #
#    Updated: 2018/10/05 20:56:01 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

nput = input("")
nput = nput.split()
count = 0
while count < len(nput):
    print("Argv of {} is {}".format(count, nput[count]))
    count += 1
x = sorted(nput, key = len, reverse=True)
for z in range(0, len(x)):
    print(x[z])
