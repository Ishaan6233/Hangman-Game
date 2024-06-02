import random

from hangman_template import Gallows, Template


def play_one_round(word_dict):
    # words.txt is a file that contains a list of word and hint

    # Choose a random entry
    random_entry = random.choice(list(word_dict.items()))

    # Separate the word and the hint
    word, hint = random_entry[0], random_entry[1]

    # Display the hint
    print(f'here is the hint: {hint}')

    # Initialization
    template = Template(len(word))
    hangman = Gallows()
    gameOver = False
    incorrect = []

    # Start  one round of the game
    while not gameOver:
        template.show()
        guess = input('Enter guess: ')
        # check if guess is valid or not
        while guess in incorrect or template.existsIn(guess):
            guess = input('Enter guess again: ')
        result = template.update(word, guess)
        if not result:
            incorrect.append(guess)
            hangman.increment()
            print('incorrect')
            hangman.show()
        gameOver = template.isComplete() or hangman.get() == 5
    if template.isComplete():
        print('Well Done')
    else:
        print('R.I.P')
    print(f'The word was {word}')


def main():
    filename = 'words.txt'
    with open(filename, 'r') as file:
        alist = file.read().splitlines()
        word_dict = {}
        for i in alist:
            word_dict[i.split(',')[0]] = i.split(',')[1]
    play_again = True
    while play_again:
        play_one_round(word_dict)
        reply = input('Play again? y/n: ').lower()
        play_again = reply == 'y'


main()
