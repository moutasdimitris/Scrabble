import random
import string
from random import shuffle
from itertools import permutations

LETTERS = {"Α": 1,
           "Β": 8,
           "Γ": 4,
           "Δ": 4,
           "Ε": 1,
           "Ζ": 10,
           "Η": 1,
           "Θ": 10,
           "Ι": 1,
           "Κ": 2,
           "Λ": 3,
           "Μ": 3,
           "Ν": 1,
           "Ξ": 10,
           "Ο": 1,
           "Π": 2,
           "Ρ": 2,
           "Σ": 1,
           "Τ": 1,
           "Υ": 2,
           "Φ": 8,
           "Χ": 8,
           "Ψ": 10,
           "Ω": 3,
           " ": 0}


class SakClass:
    def __init__(self):
        self.sak = []
        self.initialize_bag()

    def add_to_bag(self, tile, quantity):
        for i in range(quantity):
            self.sak.append(tile)

    def initialize_bag(self):
        self.add_to_bag("Α", 12)
        self.add_to_bag("Β", 1)
        self.add_to_bag("Γ", 2)
        self.add_to_bag("Δ", 2)
        self.add_to_bag("Ε", 8)
        self.add_to_bag("Ζ", 1)
        self.add_to_bag("Η", 7)
        self.add_to_bag("Θ", 1)
        self.add_to_bag("Ι", 8)
        self.add_to_bag("Κ", 4)
        self.add_to_bag("Λ", 3)
        self.add_to_bag("Μ", 3)
        self.add_to_bag("Ν", 6)
        self.add_to_bag("Ξ", 1)
        self.add_to_bag("Ο", 9)
        self.add_to_bag("Π", 4)
        self.add_to_bag("Ρ", 5)
        self.add_to_bag("Σ", 7)
        self.add_to_bag("Τ", 8)
        self.add_to_bag("Υ", 4)
        self.add_to_bag("Φ", 1)
        self.add_to_bag("Χ", 1)
        self.add_to_bag("Ψ", 1)
        self.add_to_bag("Ω", 3)
        self.add_to_bag(" ", 2)
        shuffle(self.sak)

    def putbackletters(self, letters):
        for k, v in letters:
            SakClass.add_to_bag(self, k, 1)
        shuffle(self.sak)

    def randomize_sak(self):
        SakClass.initialize_bag(self)

    def getletters(self, num):
        letters = []
        if num <= len(self.sak):
            for i in range(0, num):
                pos = random.randint(0, len(self.sak) - 1)
                letters.append((self.sak[pos], LETTERS.get(self.sak[pos])))
                SakClass.removeFromSak(self, pos)
            return letters
        else:
            return 102

    def removeFromSak(self, pos):
        self.sak.pop(pos)


class Player:
    def __init__(self):
        self.score = 0
        self.letters = []

    def __repr__(self):
        print("player repr")


class Human(Player):
    def __init__(self, sak):
        super().__init__()
        self.letters = SakClass.getletters(sak, 7)


    def __repr__(self):
        print("human repr")

    def play(self, wordcount, sk):
        print("Στο σακουλάκι:", len(sk.sak), "- Παίζεις:")
        print("Διαθέσιμα Γράμματα:", self.letters)
        word = input("Λέξη:")
        if word != "p" and word != "q":
            itsOK = Game.checkTheWord(self, word, self.letters)
            if itsOK == 0:
                while True:
                    print("Διαθέσιμα Γράμματα:", self.letters)
                    word = input("Τα γράμματα δεν ταιριάζουν με αυτά που έχεις δώσε ξανά:")
                    if word != "p" and word != "q":
                        itsOK = Game.checkTheWord(self, word, self.letters)
                        if itsOK == 1:
                            found = 0
                            for k, v in wordcount.items():
                                if word == k:
                                    found = 1
                                    self.score += v
                                    print("Αποδεκτή λέξη - Βαθμοί:", v, "- Σκορ:", self.score)
                                    self.letters = Game.removeUsedLetters(self, word, self.letters, sk)
                                    print(self.letters)
                                    while True:
                                        enter = input("Enter για Συνέχεια")
                                        print("---------------------------------------")
                                        if enter == "":
                                            break
                            if found == 0:
                                print("Δεν υπάρχει τέτοια λέξη ξαναπροσπάθησε:")
                                Human.play(self, wordcount, sk)
                            break
                    elif word == "p":
                        tempLetters = self.letters
                        s = sk.getletters(7)
                        if s != 102:
                            self.letters = s
                        else:
                            return 101
                        sk.putbackletters(tempLetters)
                        print("Διαθέσιμα Γράμματα:", self.letters)
                    elif word == "q":
                        return 101
            else:
                found = 0
                for k, v in wordcount.items():
                    if word == k:
                        found = 1
                        self.score += v
                        print("Αποδεκτή λέξη - Βαθμοί:", v, "- Σκορ:", self.score)
                        self.letters = Game.removeUsedLetters(self, word, self.letters, sk)
                        print(self.letters)
                        while True:
                            enter = input("Enter για Συνέχεια")
                            print("---------------------------------------")
                            if enter == "":
                                break
                if found == 0:
                    print("Δεν υπάρχει τέτοια λέξη ξαναπροσπάθησε:")
                    Human.play(self, wordcount, sk)

        elif word == "p":
            tempLetters = self.letters
            s = sk.getletters(7)
            if s != 102:
                self.letters = s
            else:
                return 101
            sk.putbackletters(tempLetters)
            print("Διαθέσιμα Γράμματα:", self.letters)
            print("---------------------------------------")
        elif word == "q":
            return 101


class Computer(Player):
    def __init__(self, sak):
        super().__init__()
        self.letters = SakClass.getletters(sak, 7)

    def __repr__(self):
        print("comp repr")

    def play(self, wordcount, sk, level):
        print(sk.sak)
        print("Στο σακουλάκι:", len(sk.sak), "- Παίζει Ο Η/Υ:")
        print("Γράμματα Η/Υ:", self.letters)
        if level == "1":
            p = Computer.minLettersAlg(self, wordcount, 2, 8, 1, False)
        elif level == "2":
            p = Computer.minLettersAlg(self, wordcount, 8, 2, -1, False)
        else:
            p = Computer.minLettersAlg(self, wordcount, 2, 8, 1, True)
        if p == 101:
            return 101
        for k, v in p:
            Game.removeUsedLetters(self, k, self.letters, sk)
            self.score += v
            print("Λέξη Η/Υ:", k, ",", "Βαθμοί:", v, "Σκορ Η/Υ:", self.score)
            print("---------------------------------------")

    def minLettersAlg(self, wordcount, start, stop, step, isSmart):
        wordArray = []
        permut = []
        let = []
        maxVal = []
        for k, v in self.letters:
            let.append(k)

        for i in range(start, stop, step):
            perm = permutations(let, i)
            for j in perm:
                word = ''.join(str(elem) for elem in j)
                permut.append((word, Game.calcPoints(self, word)))
        found = 0
        for k, v in permut:
            for k1, v1 in wordcount.items():
                if k == k1:
                    found = 1
                    wordArray.append((k, v))
                    if not isSmart:
                        return wordArray
        if found == 0:
            return 101
        maxV = Computer.findMax(self, wordArray)
        for k, v in wordArray:
            if v == maxV:
                maxVal.append((k, v))
                return maxVal

    def findMax(self, words):
        s = max(x[1] for x in words)
        return s


class Game:
    def __init__(self):
        self.wordcount = {}
        self.sak = SakClass()
        self.player = Player()
        self.human = Human(self.sak)
        self.computer = Computer(self.sak)
        self.level = "1"

    def __repr__(self):
        print("game repr")

    def setup(self):
        with open('greek7.txt', 'r', encoding='utf-8') as f:
            for line in f:
                for word in line.split():
                    line = line.lower()
                    word = word.strip(string.punctuation + string.digits)
                    if word:
                        points = Game.calcPoints(self, word)
                        self.wordcount[word] = points
        choice = Game.printMenu(self)
        if choice == "1":
            print("1")
        elif choice == "2":
            print("ΔΙΑΛΕΞΕ ΑΛΓΟΡΙΘΜΟ:")
            print("1: Min Letters")
            print("2: Μax Letters")
            print("3: Smart")
            while True:
                self.level = input(">>")
                if self.level == "1" or self.level == "2" or self.level == "3":
                    break
            Game.setup(self)
        elif choice == "3":
            Game.run(self, self.wordcount)
        else:
            print("q")
            Game.end(self)

    def printMenu(self):
        print("***** SCRABBLE *****")
        print("--------------------")
        print("1: Σκορ")
        print("2: Ρυθμίσεις")
        print("3: Παιχνίδι")
        print("q: Έξοδος")
        while True:
            choice = input(">>")
            if choice == "1" or choice == "2" or choice == "3" or choice == "q":
                break
        return choice

    def run(self, wordcount):
        while True:
            codeH = self.human.play(wordcount, self.sak)
            codeC = self.computer.play(wordcount, self.sak, self.level)

            if codeH == 101 or codeC == 101:
                break

    def removeUsedLetters(self, word, letters, sak):
        x = list(word)
        for i in x:
            p = 0
            for k, v in letters:
                if i == k:
                    del letters[p]
                    break
                p += 1
        if len(letters) < 7:
            letters += sak.getletters(7 - len(letters))
        return letters

    def end(self):
        print("ending the game")

    def calcPoints(self, word):
        count = 0
        x = list(word)
        for w in x:
            for d in LETTERS:
                if d == w:
                    count += LETTERS.get(w)
        return count

    def checkTheWord(self, word, letters):
        x = list(word)
        ok = 0
        for c in x:
            for k, v in letters:
                if c == k:
                    ok = 1
                    break
                else:
                    ok = 0
            if ok == 0:
                return ok
        return ok
