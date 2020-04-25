#пьяница

from random import shuffle

class Card:
    masts = ["пики", "черви",
             "буби", "крести"]
    cifrs = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "валет", "дама", "король","туз"]

    def __init__(self, c, m):
        self.mast = m
        self.cifr = c

    def __lt__(self, other):
        if self.cifr < other.cifr:
            return True
        if self.cifr == other.cifr:
            if self.mast < other.mast:
                return True
            else:
                return False
        #непонятно зачем еще один False
        return False

    def __gt__(self, other):
        if self.cifr > other.cifr:
            return True
        if self.cifr == other.cifr:
            if self.mast > other.mast:
                return True
            else:
                return False
        #непонятно зачем еще один False
        return False

    def __repr__(self):
        #не уверен что взял правильную переменную, обязательно ли брать с или можно k
        #как это он тут так названия возвращает?
        k = self.cifrs[self.cifr] + " " + self.masts[self.mast]
        return k

class Deck:
    def __init__(self):
        #почему это не переменная класса дек?
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def shetchik(self):
        if len(self.cards) == 0:
            #ретурн что??? почему там ничего нет?? почему не фолс например
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        #почему только одна переменная кроме селф в __инит__
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        #почему они без self?
        name1 = input("имя игрока 1:")
        name2 = input("имя игрока 2:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        
    def wins(self, winner):
        #блять а где winner что за хуйня
        w = "{} забирает карты"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p2n, p1c, p2c):
        #как и в предыдущем
        d = "{} кладет {}, а {} кладет {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        #че бля
        cards = self.deck.cards
        print("Поехали!")
        while len(cards) >= 2:
            m = "Нажмите Х для выхода. Нажмите любую клавишу для начала игры."
            response = input(m)
            if response == "X":
                break
            p1c = self.deck.shetchik()
            p2c = self.deck.shetchik()
            #почему ОБД.ОБД.ОБД не понимаю
            p1n = self.p1.name
            p2n = self.p2.name
            #тут вывод (см. выше)
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("Игра окончена. {} выиграл.".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Ничья"
            
gg = Game()
gg.play_game()
