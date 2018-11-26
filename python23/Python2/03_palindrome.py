# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03_palindrome.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 17:49:23 by apickett          #+#    #+#              #
#    Updated: 2018/10/05 13:38:04 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

s = input("Write your palindrome\n")

def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  
ans = isPalindrome(s) 

if ans == 1: 
    print("Cool") 
else: 
    print("Not Cool")
