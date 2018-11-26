# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_bool.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/03 19:38:58 by apickett          #+#    #+#              #
#    Updated: 2018/10/05 21:33:07 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

i = 0
l1 = [False,True,True,None,True,None,None,False,False,None,True,False]
l2 = ["or","or","or","==","!=","==","and","==","!=","and","==","or"]
l3 = [False,False,None,None,True,True,False,True,None,False,True,None]

while i < len(l1) and i < len(l2) and i < len(l3):
    if l2[i] == "or":
        print(l1[i], l2[i], l3[i], "=>", l1[i] or l3[i])
        i += 1
    elif l2[i] == "==":
        print(l1[i], l2[i], l3[i], "=>",l1[i])
        i += 1
    elif l2[i] == "!=":
        print(l1[i], l2[i], l3[i], "=>", l1[i])
        i += 1
    else:
        print(l1[i], l2[i], l3[i], "=>", l3[i])
        i += 1
