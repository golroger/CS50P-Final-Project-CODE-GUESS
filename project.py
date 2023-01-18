import random as rd
from tabulate import tabulate
import pandas as pd

def main():
        print("######################################################################")
        print("#                 Welcome to the Game!                               #")
        print("#     Before you start read the rules below :                        #")
        print("#        1- This is a code guessing game                             #")
        print("#        2- The code is 4 digit number, not starting with 0          #")
        print("#        3- Each time you guess, we give you a little help :         #")
        print("#        B : Right number BUT NOT the right number                   #")
        print("#        M : Right number AND in the Right place                     #")
        print("#        4- Choose the right level :                                 #")
        print("#                  Easy = 30 , Meduim = 20, Hard = 10 tries          #")
        print("#                                                                    #")
        print("#                            Good Luck !                             #")
        print("######################################################################")
        level = input("Choose the level, \ntype the chosen level 'easy', 'meduim' or 'hard' :")
        if level.lower() =="easy" :
            max_try = 30
        elif level.lower() == "meduim" :
            max_try = 20
        elif level.lower()== "hard" :
            max_try =10
        else :
            print("unkonwn level, the default is easy :) !")
            max_try = 30
        n=1 ; mode_game = [1,2,3]
        df = pd.DataFrame()
        code = generate_code()
        x = input("user guess :")
        while x   :
            boo, msg = is_validguess(x)

            if boo  :
                result =  str(injured_number(code, x)) + " B " + str(dead_number(code, x)) + " M"
                df , s = history(n,df ,x , result)
                print(s)
                if n >= max_try :
                    print("You lose :) ! ")
                    break
                x= input("user guess :")
                if dead_number(code, x) == 4 :
                    print("you WIN ! ")
                    break
                n = n+1
            else :
                print(msg)
                x = input("user guess :")



# This function return the secret code that the user will try to guess it
# the code could not start with 0, and the digits can not be redundant
# we will use random module
def generate_code():
    list_numbers = [0,1 , 2 , 3, 4, 5, 6, 7, 8,9]
    code = "" ; i = 0
    while i < 4 :
        chosen = str(rd.choice(list_numbers))
        if i == 0 and chosen == "0" :
            continue
        else :
            code = code + chosen
            list_numbers.remove(int(chosen))
            i=i+1
    return code

# This function check the entery of the user, if it not a valid number, it return False, else return True
# you should not enter a repetitive digit in your guessed number
def is_validguess(user_g) :
    try :
        n = set()
        code = int(user_g)
        if len(user_g) != 4 :
            return False , "Your Guess number is too large !"
        if user_g[0] =="0" :
            return False, "Can't start with 0, enter a valid number !"
        else :
            for i in range(len(user_g)) :
                n.add(user_g[i])
            if len(n) != 4 :
                return False , "Your guess number contain doubles ! "
    except ValueError :
        return False , " Type a valid number !"
    else :
        return True,""


# an injured digit is a guessed digit by the user that is the RIGHT INTEGER but NOT IN THE RIGHT PLACE.
# This function will return the number of the injured number.
def injured_number(code, x):
    inj = 0
    for i in range(len(code)):
        for j in range(len(x)) :
            if i != j and code[i] == x[j] :
                inj = inj +1
    return inj

# a dead guess digit is a guessed digit by the user and it is THE RIGHT INTEGER AND IN THE RIGHT PLACE.
# This function will return the number of the deads guessed digits
def dead_number(code, user_guess):
    d = 0
    for (i,j) in zip(code, user_guess) :
        if i == j :
            d=d+1
    return d

#This function will store the history of the user guesses with the result, and show them to the user before any guess.
# this will help the user the find the secrect code quickly.
# I will use the Tabulate to show this table.
def history(n , df , user_guess , result) :
    l_guess = [] ; l_tries = [] ; l_result =[]
    l_guess.append(user_guess) ; l_tries.append(n) ; l_result.append(result)
    mydict = {"N° " : l_tries , "Guess " :l_guess , "Result :" : l_result}
    df2 = pd.DataFrame(mydict)
    frames = [df,df2]
    result = pd.concat(frames)
    result = result.reset_index(drop = True)
    return result , tabulate(result ,headers = ["N° Try" , "Guess", "Result"], tablefmt ="grid" , showindex=False, numalign = "center")

if __name__ == "__main__":
    main()