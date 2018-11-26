# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_rainbow.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/16 17:28:15 by apickett          #+#    #+#              #
#    Updated: 2018/10/29 14:34:27 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_colorful_text(string, style, fg, bg):
    format = ';'.join([str(style), str(fg), str(bg)])
    s = '\x1b[%sm%s\x1b[0m' % (format, string)
    print(s, end = "")

print_colorful_text("RAINBOW", 1, 31, 40)
print("\n")
print_colorful_text("AINBOW", 1, 33, 40)
print("\n")
print_colorful_text("INBOW", 1, 32, 40)
print("\n")
print_colorful_text("NBOW", 1, 36, 40)
print("\n")
print_colorful_text("BOW", 1, 34, 40)
print("\n")
print_colorful_text("OW", 1, 35, 40)
print("\n")
print_colorful_text("W", 1, 37, 40)
print("\n")
