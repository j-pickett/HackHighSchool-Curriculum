# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_guess.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/16 16:15:28 by apickett          #+#    #+#              #
#    Updated: 2018/10/16 16:15:29 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import random
import string

def main(args):
    arr = ["alexa", "tacos", "milky", "pizza", "jocks", "ramps", "guild", "loser"]
    word = random.choice(arr)
    print(f"the secret word begins with a {word[0]}")
    guess = None
    guesses_left = 10
    while guess != word and guesses_left > 0:
        guess = input("GUESS: ").strip().lower()
        if guess == "":
            print("lmao you wasted a guess")
            guesses_left -= 1
        elif len(guess) != 5:
            print("Go watch some sesame street, thats not 5")
            guesses_left -= 1
        elif guess[0] != word[0]:
            print(f"your word starts with {word[0]} not {guess[0]}")
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif guess[0] == word[0] and not guess == word:
            guesses_left -= 1
            print(f"Guesses Left: {guesses_left}")
        else:
            print(":telephone_receiver: :gaetan: someone cheated, they got the answer")
if __name__ == "__main__":
   main(sys.argv)
