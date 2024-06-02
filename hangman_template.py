import random

class Gallows:
    def __init__(self):
        self.step = 0

    def increment(self):
        self.step += 1

    def show(self):
        gallows_stages = [
            '',
            '  _____\n  |\n  |\n  |\n  |\n /|\\',
            '  _____\n  |/\n  |\n  |\n  |\n /|\\',
            '  _____\n  |/    |\n  |\n  |\n  |\n /|\\',
            '  _____\n  |/    |\n  |     o\n  |\n  |\n /|\\',
            '  _____\n  |/    |\n  |     o\n  |    /|\\\n  |    / \\\n /|\\'
        ]
        print(gallows_stages[self.step])

    def get(self):
        return self.step

class Template:
    def __init__(self, size):
        self.dashes = ['_'] * size

    def show(self):
        print(' '.join(self.dashes))

    def update(self, word, guess):
        found = False
        for i, letter in enumerate(word):
            if guess == letter:
                self.dashes[i] = guess
                found = True
        return found

    def is_complete(self):
        return '_' not in self.dashes

    def exists_in(self, guess):
        return guess in self.dashes

def play_one_round(word_dict):
    word, hint = random.choice(list(word_dict.items()))
    print(f'Here is the hint: {hint}')

    template = Template(len(word))
    hangman = Gallows()
    game_over = False
    incorrect_guesses = []

    while not game_over:
        template.show()
        guess = input('Enter guess: ').lower()

        while guess in incorrect_guesses or template.exists_in(guess):
            guess = input('Enter guess again: ').lower()

        if template.update(word, guess):
            print('Correct!')
        else:
            incorrect_guesses.append(guess)
            hangman.increment()
            print('Incorrect')
            hangman.show()

        game_over = template.is_complete() or hangman.get() == 5

    if template.is_complete():
        print('Well done! You guessed the word!')
    else:
        print('R.I.P. You failed to guess the word.')
    print(f'The word was "{word}".')

def main():
    filename = 'words.txt'
    with open(filename, 'r') as file:
        word_dict = {}
        for line in file:
            word, hint = line.split(',')
            word_dict[word.strip()] = hint.strip()

    play_again = True
    while play_again:
        play_one_round(word_dict)
        reply = input('Play again? (y/n): ').lower()
        play_again = reply == 'y'

if __name__ == '__main__':
    main()