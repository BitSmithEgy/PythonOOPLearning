class Game:
    def __init__(self):
        print('Welcome to BitSmith OOP game')
        print('Choose your game from our collection')
        print('[1] EvenSquared')
        print('[2] PrimeChecker')
        print('[3] Palindrome')
        print('[4] WordCount')
        print('[5] FibonacciSequence')
        print('[6] To stop the main game')
        self.games = {1: self.EvenSquared, 2: self.PrimeChecker, 3: self.Palindrome, 4: self.WordCount, 5: self.FibonacciSequence}
        self.choices()

    def choices(self):
        while True:
            choice = input('Enter your choice: ')
            try:
                choice = int(choice)
                if choice in range(1, 7):
                    if choice == 6:
                        print('Exiting the game see you soon!')
                        break
                    self.games[choice]()
                else:
                    print('Please choose a valid number')
                print('******************************************')
            except ValueError:
                print("Invalid input, please enter a number")

    def EvenSquared(self):
        print('Game: EvenSquared')
        print('Enter \'x\' to exit the game')
        print('This game takes a list of numbers and prints the squares of even numbers.')
        while True:
            num_list = input('Enter the list of numbers separated with space (\' \'): ')
            if num_list == 'x':
                break
            num_list = num_list.split()
            num_list = [int(num) for num in num_list]
            print([num ** 2 for num in num_list if num % 2 == 0])
            print('******************************************')

    def PrimeChecker(self):
        print('Game: PrimeChecker')
        print('Enter \'x\' to exit the game')
        print('This game checks if a given number is prime.')
        while True:
            num = input('Enter the number: ')
            if num == 'x':
                break
            else:
                try:
                    num = int(num)
                    if num < 2:
                        print(False)
                    else:
                        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
                        print(is_prime)
                    print('******************************************')
                except ValueError:
                    print('Enter an integer number')

    def Palindrome(self):
        print('Game: Palindrome')
        print('Enter \'x\' to exit the game')
        print('This game checks if a given word is a palindrome.')
        while True:
            word = input('Enter a word: ')
            if word == 'x':
                break
            else:
                ignored = ['!', '@', '.', ' ', '?' '\'', ]
                word = [litter for litter in word if litter not in ignored]
                word = ''.join(word).lower()
                reversed_word = word[::-1].lower()
                print(word == reversed_word)
                print('******************************************')

    def WordCount(self):
        print('Game: WordCount')
        print('Enter \'x\' to exit the game')
        print('This game counts the occurrences of each word in a given sentence.')
        while True:
            sentence = input('Enter a sentence: ')
            if sentence == 'x':
                break
            else:
                input_string = sentence.lower()

                words = input_string.split()

                word_counts = {}

                for word in words:
                    word = word.strip('.,!?')

                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

                print(word_counts)
                print('******************************************')

    def FibonacciSequence(self):
        print('Game: FibonacciSequence')
        print('Enter \'x\' to exit the game')
        print('This game generates the Fibonacci sequence up to a given number of terms.')
        while True:
            n = input('Enter the number of terms for the Fibonacci sequence: ')
            if n == 'x':
                break
            else:
                try:
                    n = int(n)
                    fibonacci_list = [0, 1]

                    while n > len(fibonacci_list):
                        fibonacci_list.append((lambda x: x[-1] + x[-2])(fibonacci_list))

                    print(fibonacci_list)
                    print('******************************************')
                except ValueError:
                    print('Enter an integer number')

game = Game()