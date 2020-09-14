import random
import string
import json
from os import path
from random import shuffle
from itertools import permutations
from datetime import datetime

"""
Τα γράμματα μαζί με τις αξίες του καθενός.
"""
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
    """
    Η κλάση SakClass αναπαριστά το σακίδιο του παιχνιδιού και αποτελείται από τις εξής συναρτήσεις:
        1)__init__(self) -> αυτή φροντίζει για την αρχικοποίηση της κλάσης και αρχικά δημιουργεί μία
        κενή λίστα στην οποία θα αποθηκεύονται τα τουβλάκια. Επίσης καλείται η initialize_bag() η οποία
        αρχικοποιεί το σακίδιο και για την οποία θα γίνει ανάλυση παρακάτω.
        2)add_to_bag(self, tile, quantity) -> η οποία είναι υπεύθυνη για να προσθέσει το τουβλάκι tile
        στο σακίδιο τόσες φορές όσες είναι το quantity. Όλα τα τουβλάκια εισάγωνται στο self.sak.
        3)initialize_bag(self) ->η οποία εισάγει τα τουβλάκια στο σακίδιο τόσες φορές όσες λένε οι κανόνες.
        4)putbackletters(self, letters) -> η οποία φροντίζει να επιστρέψει τα γράμματα του letters στο σακίδιο.
        5)randomize_sak(self) -> η οποία καλεί την initialize_bag για την αρχικοποίηση του σακιδίου.
        6)getletters(self, num) -> η οποία δέχεται τον αριθμό από τα τουβλάκια που λείπουν απο το χρήστη
        που την καλεί και επιστρέφει από το σακίδιο τόσα όσα είναι ο αριθμός num. Επίσης καλείται στην αρχή
        η shuffle για να γίνει ανακάτεμα των πλακιδίων και στη συνέχεια ακολουθεί η προηγούμενη διαδικασία.
        7)removeFromSak(self, pos) -> η οποία διαγράφει το στοιχείο pos από το σακίδιο.
        8)__repr__(self) -> η οποία εκτυπώνει το self.sak.
    """

    def __init__(self):
        self.sak = []
        self.initialize_bag()

    def __repr__(self):
        print("sak ", self.sak)

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

    def putbackletters(self, letters):
        for k, v in letters:
            SakClass.add_to_bag(self, k, 1)

    def randomize_sak(self):
        SakClass.initialize_bag(self)

    def getletters(self, num):
        shuffle(self.sak)
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
    """
    Η κλάση αυτή αναπαριστά τον παίκτη και αποτείται από τις εξής συναρτήσεις:
        1)__init__(self) -> η οποία όταν δημιουργηθούν αντικείμενα αυτής της κλάσης θα κληρονομήσουν αυτόματα
        τις ιδιότητες με το score και τα letters άρα όταν δημιουργηθούν ο χρήστης και ο υπολογιστής σαν παίκτες
        του παιχνιδιού θα αρχικοποιηθούν αυτά στο 0 και αντίστοιχα τα γράμματά τους σε κενή λίστα μέχρι να πάρουν.
        2)__repr__(self) -> η οποία εκτυπώνει το τρέχον score και τα γράμματα.
    """

    def __init__(self):
        self.score = 0
        self.letters = []

    def __repr__(self):
        print("Score", self.score)
        print("Letters", self.letters)


class Human(Player):
    """
    Η κλάση αυτή αφορά το χρήστη καθώς και όλες τις συναρτήσεις που χρειάζονται για αυτόν
    και οι οποίες είναι οι εξής:
        1)__init__(self, sak) -> η οποία κληρονομεί την init της υπερκλάσης Player και λόγο αυτού αρχικοποιεί
        score του χρήστη στο 0 και τα γράμματά του αρχικά σε κενή λίστα ενώ στη συνέχεια ζητούνται 7 γράμματα.
        2)__repr__(self) -> εκτυπώνει τα στιγμιότυπα του score και των γραμμάτων του χρήστη.
        3)play(self, wordcount, sk) -> η οποία υλοποιεί τον τρόπο που παίζει ο χρήστης όταν έρθει η σειρά του.
        Αρχικά εκτυπώνονται τα διαθέσιμα στο χρήστη γράμματα και δέχεται είσοδο από το πληκτρολόγιο τη λέξη του χρήστη
        και για την οποία γίνονται οι έλεγχοι εάν αυτή είναι p η κενή άρα ο χρήστης πηγαίνει πάσο και του δίνονται
        νέα γράμματα επιστρέφοντας τα παλία στο σακίδιο. Εάν η λέξη είναι q τότε ο χρήστης εγκαταλείπει το παιχνίδι
        και επιστρέφεται στην κλάση Game ο κωδικός 101 που σημαίνει λήξη του παιχνιδιού. Σε αντίθετη περίπτωση γίνονται
        πρώτα ο έλεγχος έαν ο χρήστης έχει όντως τα γράμματα από τα οποία αποτελείται η λέξη καλώντας την checkTheWord
        και η οποία επιστρέφει 0 εάν δεν τα έχει και 1 εάν υπάρχουν όντως τα γράμματα στο σακίδιό του. Στη συνέχεια
        γίνεται έλεγχος εάν η λέξη που έδωσε υπάρχει στο αρχείο greek7.txt και για το οποίο έχει γίνει με τη δομή
        του λεξικού η καταχώρηση των εγγραφών στο πρόγραμμα καθώς και η βαθμολογία αυτών. Εάν υπάρχει πιστώνονται
        στο χρήστη οι βαθμοί σε αντίθετη περίπτωση ξαναδίνει λέξη και ακολουθεί η παραπάνω διαδικασία.
        4)calcPoints(self, word) -> η οποία δέχεται μία λέξη και υπολογίζει τους βαθμούς της.
    """

    def __init__(self, sak):
        super().__init__()
        self.letters = SakClass.getletters(sak, 7)

    def __repr__(self):
        print("Score", self.score)
        print("Letters", self.letters)

    def play(self, wordcount, sk):
        print("Στο σακουλάκι:", len(sk.sak), "- Παίζεις:")
        print("Διαθέσιμα Γράμματα:", self.letters)
        word = input("Λέξη:")
        if word != "p" and word != "q":
            itsOK = Game.checkTheWord(self, word, self.letters)
            if itsOK == 0:
                while True:
                    print("Διαθέσιμα Γράμματα:", self.letters)
                    word1 = input("Τα γράμματα δεν ταιριάζουν με αυτά που έχεις δώσε ξανά:")
                    if word1 != "p" and word1 != "q":
                        print("im in 1")
                        itsOK = Game.checkTheWord(self, word1, self.letters)
                        if itsOK == 1:
                            found = 0
                            for k, v in wordcount.items():
                                if word1 == k:
                                    found = 1
                                    self.score += v
                                    print("Αποδεκτή λέξη - Βαθμοί:", v, "- Σκορ:", self.score)
                                    self.letters = Game.removeUsedLetters(self, word1, self.letters, sk)
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
                    elif word1 == "p":
                        print("im in", word1)
                        tempLetters = self.letters
                        s = sk.getletters(7)
                        if s != 102:
                            self.letters = s
                        else:
                            return 101
                        sk.putbackletters(tempLetters)
                        print("Διαθέσιμα Γράμματα:", self.letters)
                        print("---------------------------------------")
                        break
                    elif word1 == "q":
                        print("im in 3 ", word1)
                        return 101
            else:
                found = 0
                for k, v in wordcount.items():
                    if word == k:
                        found = 1
                        score = Human.calcPoints(self, word)
                        self.score += score
                        print("Αποδεκτή λέξη - Βαθμοί:", score, "- Σκορ:", self.score)
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

        elif word == "p" or word == "":
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

    def calcPoints(self, word):
        count = 0
        c = self.letters.copy()
        x = list(word)
        for w in x:
            p = 0
            for d, l in c:
                if d == w:
                    c.pop(p)
                    count += LETTERS.get(w)
                    break
                p += 1
        return count


class Computer(Player):
    """
    Η κλάση αυτή αφορά τον υπολογιστή καθώς και όλες τις συναρτήσεις που χρειάζονται για αυτόν
    και οι οποίες είναι οι εξής:
        1)__init__(self, sak) -> η οποία κληρονομεί την init της υπερκλάσης Player και λόγο αυτού αρχικοποιεί
        score του υπολογιστή στο 0 και τα γράμματά του αρχικά σε κενή λίστα ενώ στη συνέχεια ζητούνται 7 γράμματα.
        2)__repr__(self) -> εκτυπώνει τα στιγμιότυπα του score και των γραμμάτων του υπολογιστή.
        3)play(self, wordcount, sk, level) -> η οποία υλοποιεί τον αλγόριθμο που παίζει ο υπολογιστής. Στην αρχή
        εκτυπώνει τις πληροφορίες του υπολογιστή και ανάλογα με τον αλγόριθμο που θέλει ο χρήστης να παίξει ο υπολογιστή
        δίνει τα κατάλληλα ορίσματα στην computerAlg η οποία εκτελεί την κίνηση του υπολογιστή. Αυτή επιστρέφει
        κατάλληλο code το οποίο εάν είναι 101 σημαίνει ότι δεν βρήκε λέξη αλλιώς επιστρέφει τη λέξη μαζί με το σκορ
        αυτής. Τέλος εκτυπώνει τη βαθμολογία υπολογιστή.
        4)computerAlg(self, wordcount, start, stop, step, isSmart) -> η οποία δέχεται σαν ορίσματα το wordcount που
        είναι το λεξικό με τις λέξεις απο το greek7.txt για να κάνει τον έλεγχο εάν υπάρχει η λέξη του υπολογιστή,
        το start, το stop και το step τα οποία χρησιμοποιούνται για τις μεταθέσεις των γραμμάτων ανάλογα με το επίπεδο
        που επιλέγει ο χρήστης και το  isSmart που είναι τύπου bool και καθορίζει το σκέλος smart του αλγορίθμου
        min-max-smart. Για λόγους αποδοτικότητας όταν ο υπολογιστής τύχει το πλακίδιο (" ") τότε επιστρέφει τα γράμματά
        του και παίρνει άλλα ξανατρέχοντας τον αλγόριθμο αυτό για τα νέα γράμματα αλλιώς προσθέτει τα γράμματα στο
        let και στη συνέχεια υπολογίζει όλες τις μεταθέσεις και επιλέγει ανάλογα για κάθε αλγόριθμο. Τέλος επιστρέφει
        αυτή με το μεγαλύτερο σκορ στην περίπτωση του smart ενώ σε κάθε άλλη περίπτωση την πρώτη αποδεκτή λέξη.
        5)findMax(self, words) -> η οποία από τη λίστα με τις λέξεις βρίσκει τη θέση αυτής με το μεγαλύτερο σκορ και
        την επιστρέφει.
    """

    def __init__(self, sak):
        super().__init__()
        self.letters = SakClass.getletters(sak, 7)
        self.sak = sak

    def __repr__(self):
        print("Score", self.score)
        print("Letters", self.letters)

    def play(self, wordcount, sk, level):
        print("Στο σακουλάκι:", len(sk.sak), "- Παίζει Ο Η/Υ:")
        print("Γράμματα Η/Υ:", self.letters)
        if level == "1":
            p = Computer.computerAlg(self, wordcount, 2, 8, 1, False)
        elif level == "2":
            p = Computer.computerAlg(self, wordcount, 8, 2, -1, False)
        else:
            p = Computer.computerAlg(self, wordcount, 2, 8, 1, True)
        if p == 101:
            return 101
        for k, v in p:
            Game.removeUsedLetters(self, k, self.letters, sk)
            self.score += v
            print("Λέξη Η/Υ:", k, ",", "Βαθμοί:", v, "Σκορ Η/Υ:", self.score)
            print("---------------------------------------")

    def computerAlg(self, wordcount, start, stop, step, isSmart):
        wordArray = []
        permut = []
        let = []
        maxVal = []
        con = True
        for k, v in self.letters:
            if k == " ":
                SakClass.putbackletters(self.sak, self.letters)
                self.letters = SakClass.getletters(self.sak, 7)
                print("Νέα Γράμματα Η/Υ:", self.letters)
                con = False
                break
            else:
                let.append(k)
        if not con:
            Computer.computerAlg(self, wordcount, start, stop, step, isSmart)
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
    """
    Η κλάση αυτή αφορά την οργάνωση του παιχνιδιού και η οποία περιλαμβάνει τις εξής συναρτήσεις:
        1)__init__(self) -> η οποία αρχικοποιεί το κενό λεξικό για τις λέξεις του greek7.txt, δημιουργεί αντικείμενα
        τύπου SakClass, Player, Human και Computer ενώ από προεπιλογή σε περίπτωση που δεν επιλέξει ο χρήστης
        το επίπεδο του υπολογιστή από τις ρυθμίσεις τότε επιλέγει αυτόματα να παίξει με το min letters.
        2)__repr__(self) -> η οποία εκτυπώνει τις ίδιες πληροφορίες με παραπάνω
        3)setup(self) -> η οποία φροντίζει να γίνουν οι απαραίτητες ενέργειες για την έναρξη του παιχνιδιού όπως τη
        δημιουργία του λεξικού, την εκτύπωση του μενού και τη διαχείρηση ανάλογα με την επιλογή. Εάν επιλέξει το 1 τότε
        διαβάζει το αρχείο με τα προηγούμενα σκορ (history.json) και ενημερώνει κατάλληλα με τα προηγούμενα σκορ και την
        ημερομηνία που αυτά έγιναν καθώς και την ώρα. Εάν επιλέξει το 2 τότε επιλέγει με ποιόν αλγόριθμο θα παίξει ο
        υπολογιστής. Με το 3 ξεκινάει το παιχνίδι ενώ με το 4 τερματίζει το παιχνίδι.
        4)printPrevious(self) -> η οποία διαβάζει το αρχείο με τα προηγούμενα αποτελέσματα και τα εκτυπώνει ενώ εάν
        δεν υπάρχει το αρχείο τότε εημερώνει κατάλληλα το χρήστη.
        5)printMenu(self) -> φροντίζει να εκτυπώσει το μενού και δέχεται την επιλογή μέχρι να είναι αυτή έγκυρη.
        6)run(self, wordcount) -> η οποία καλεί τους αλγορίθμους των human και computer και οι οποίοι παίζουν την κίνησή
        τους εναλλάξ. Εάν αυτοί επιστρέψουν 101 τερματίζει το παιχνίδι και εκτυπώνει το τρέχον σκορ και ανακοινώνει το
        νικητή ενώ γράφει αυτά στο αρχείο που κρατάει τα σκορ.
        7)removeUsedLetters(self, word, letters, sak) -> διαγράφει τα γράμματα που περιέχει η λέξη (word) από το
        (letters) και αναπληρώνει το πλήθος των στοιχείων που αφαιρέθηκαν έτσι ώστε να έχει ο χρήστης ή ο υπολογιστής
        σύνολο 7 γράμματα.
        8)writeInfosToFile(self) -> συνάρτηση η οποία φροντίζει να γράψει τα αποτελέσματα στο αρχείο με τα σκορ ενώ εάν
        έχει ήδη περιεχόμενο το αρχείο το προσθέτει χωρίς να αντικαθιστά το περιεχόμενο.
        9)writeJSON(self, data, filename="history.json") -> βοηθητική συνάρτηση η οποία αποθηκεύει τα data στο filename.
        10)end(self) -> τερματίζει το παιχνίδι.
        11)calcPoints(self, word) -> υπολογίζει τους πόντους της λέξης word.
        12)checkTheWord(self, word, letters) -> τσεκάρει εάν η λέξη που έδωσε ο χρήστης αποτελείται από γράμματα που έχει
        ο ίδιος στο letters.

    """
    def __init__(self):
        self.wordcount = {}
        self.sak = SakClass()
        self.player = Player()
        self.human = Human(self.sak)
        self.computer = Computer(self.sak)
        self.level = "1"

    def __repr__(self):
        print("Score Human", self.human.score)
        print("Score Computer", self.computer.score)
        print("Σακίδιο", self.sak.sak)

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
            Game.printPrevious(self)
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
            Game.end(self)

    def printPrevious(self):
        try:
            with open('history.json') as json_file:
                data = json.load(json_file)
                for p in data['matches']:
                    print('Your score: ', p['You'])
                    print('Computer score: ', p['Computer'])
                    print('Date/Time: ', p['Date/Time'])
                    print('--------------------------------')
        except FileNotFoundError:
            print("Δεν υπάρχει ιστορικό. Παίξτε παιχνίδια και αυτά θα καταγραφούν αυτόματα στο ιστορικό. Καλή "
                  "διασκέδαση!")

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
        global codeC
        while True:
            codeH = self.human.play(wordcount, self.sak)
            if codeH != 101:
                codeC = self.computer.play(wordcount, self.sak, self.level)
            if codeH == 101 or codeC == 101:
                print("Τελικό Αποτέλεσμα:")
                print("Εσύ:", self.human.score, " Η/Υ:", self.computer.score)
                if self.human.score > self.computer.score:
                    print("Νίκησες!!!")
                elif self.human.score < self.computer.score:
                    print("Έχασες.")
                else:
                    print("Ισοπαλία.")
                Game.writeInfosToFile(self)
                break

    def removeUsedLetters(self, word, letters, sak):
        x = list(word)
        counter = 0
        t = len(x)
        for i in x:
            p = 0
            for k, v in letters:
                if i == k:
                    letters.pop(p)
                    t -= 1
                    break
                p += 1

        for k1, v1 in letters:
            if k1 == " " and t == 1:
                letters.pop(counter)
                break
            elif k1 == " " and t == 2:
                letters.pop(counter)
                t -= 1
            counter += 1
        if len(letters) < 7:
            letters += sak.getletters(7 - len(letters))

        return letters

    def writeInfosToFile(self):
        try:
            now = datetime.now()
            if path.exists("history.json"):
                with open("history.json") as outfile:
                    data = {
                        'You': self.human.score,
                        'Computer': self.computer.score,
                        'Date/Time': now.strftime("%d/%m/%Y %H:%M:%S")
                    }
                    previousData = json.load(outfile)
                    temp = previousData['matches']
                    temp.append(data)
                    Game.writeJSON(self, previousData)
            else:
                data = {}
                data['matches'] = []
                data['matches'].append({
                    'You': self.human.score,
                    'Computer': self.computer.score,
                    'Date/Time': now.strftime("%d/%m/%Y %H:%M:%S")
                })
                Game.writeJSON(self, data)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))

    def writeJSON(self, data, filename="history.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
            f.close()

    def end(self):
        print("Αντίο!")
        quit()

    def calcPoints(self, word):
        count = 0
        x = list(word)
        for w in x:
            for d in LETTERS:
                if d == w:
                    count += LETTERS.get(w)
                    break
        return count

    def checkTheWord(self, word, letters):
        x = list(word)
        let = letters.copy()
        ok = 0
        z = len(x)
        for c in x:
            i = -1
            for k, v in let:
                i += 1
                if c == k:
                    ok = 1
                    del let[i]
                    z -= 1
                    break
        if z != 0:
            if " " in let[1]:
                ok = 1
        return ok
