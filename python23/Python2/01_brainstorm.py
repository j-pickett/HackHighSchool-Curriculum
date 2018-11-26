# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_brainstorm.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/02 18:16:15 by apickett          #+#    #+#              #
#    Updated: 2018/10/05 21:07:47 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

i = 0
category = ['cereal', 'villains', 'video games', 'pizza toppings', 'music']
lst1 = []
print(random.choice(category))
for i in range(10):
    nput = input()
    lst1.append(nput)
print('\t''\t''\t', lst1)
