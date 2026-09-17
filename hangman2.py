from hangman_words import words
import random

r = "\033[31;1m"
g = "\033[32;1m"

rh = "\033[30;1;41m"
gh = "\033[30;1;42m"

re = "\033[0m"


hangman = {0: 
           ("   ",
            "   ",
            "   "),
           1:(" o ",
              "   ",
              "   "), 
           2:(" o ",
              " | ",
              "   "), 
           3:(" o ",
              "/| ",
              "   "), 
           4:(" o ",
              "/|\\",
              "   "), 
           5:(" o ",
              "/|\\",
              "/  "), 
           6:(" o ",
              "/|\\",
              "/ \\")}


def show_hint(d):
    print(" ".join(d))

def hangman_art(x):
    print("********")
    for h in hangman[x]:
        print(f"{r}{h}{re}")        
    print("********")

def main():
    play_again = True
    
    while play_again:
        randWord = random.choice(words)
        display = ["_"] * len(randWord)  
        running = True
        inc = 0
        
        while running:
            hangman_art(inc)
            show_hint(display)
            guess = input("Guess the hidden word: ").upper()
            if len(guess) != 1:
                print("Enter 1 letter only")
                continue
            elif not guess.isalpha():
                print("Letters only")
                continue

            if guess in randWord:
                for i, letter in enumerate(randWord):
                    if guess == letter:
                        display[i] = guess
            else:
                inc += 1

            if inc == 6:
                hangman_art(inc)
                show_hint(display)
                print("You lost")
                print(randWord)
                running = False

            elif "_" not in display:
                print("You won!")
                show_hint(display)
                running = False

        ask = input("(Enter 'y' to play again, otherwise Enter 'x')\n-> ")
        if ask != "y":
            play_again = False
            

if __name__ == "__main__":
    main()

     
