import random


class Poker:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 100] * 4
        self.names_cards = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 20: "Walet", 30: "Dama", 40: "King", 100: "Ace"}

    def take_card(self):
        user = []
        bot = []
        random.shuffle(self.deck)
        for i in range(2):
            card = self.deck.pop(random.randint(0, len(self.deck)-1))
            user.append(card)
        print("**"+self.names_cards[user[0]]+"--"+self.names_cards[user[1]]+"**")
        for i in range(2):
            card_bot = self.deck.pop(random.randint(0, len(self.deck)-1))
            bot.append(card_bot)
        self.table(user,bot)

    def table(self,user,bot):
        table_card = []
        random.shuffle(self.deck)
        for i in range(3):
            card = self.deck.pop(random.randint(0, len(self.deck)-1))
            table_card.append(card)
        print("-----------------------")
        print("-------"+self.names_cards[table_card[0]]+"--"+self.names_cards[table_card[1]]+"--"+self.names_cards[table_card[2]]+"-------")
        print("-----------------------")
        self.choise()
        card = self.deck.pop(random.randint(0, len(self.deck)-1))
        table_card.append(card)
        print("-----------------------")
        print("-----"+self.names_cards[table_card[0]]+"--"+self.names_cards[table_card[1]]+"--"+self.names_cards[table_card[2]]+"--"+self.names_cards[table_card[3]]+"-----")
        print("-----------------------")
        self.choise()
        card = self.deck.pop(random.randint(0, len(self.deck)-1))
        table_card.append(card)
        print("-----------------------")
        print("----"+self.names_cards[table_card[0]]+"--"+self.names_cards[table_card[1]]+"--"+self.names_cards[table_card[2]]+"--"+self.names_cards[table_card[3]]+"--"+self.names_cards[table_card[4]]+"----")
        print("-----------------------")
        self.win_lose(table_card,user,bot)


    def choise(self):
        print("What will u do?\ncheck(c)/fold(f)")
        choise = input()
        if choise == "c":
            return
        else:
            self.game()


    def win_lose(self, card_table, user, bot):
        win_comb = []
        win_comb_bot = []
        score = 0
        bot_score = 0
        for i in user:
            for j in card_table:
                if i==j:
                    win_comb.append(j)
        #print(win_comb)
        if len(win_comb)==0:
            for i in user:
                us = max (i, i+1)
            for j in bot:
                bs = max(j, j+1)
            if us>bs:
                print("You have a best card, then bot")
                score = 1
                bot_score = 0
            else:
                score = 0
                bot_score = 1
                print("Bot has a best card, then u")
        elif len(win_comb)==1:
            print("You have a pair")
            score = 1
        elif len(win_comb)==2:        
            if win_comb[0] == win_comb[1]:
                print("You have a set!")
                score = 3
            else:
                print("Ypu have  2 pairs")
                score = 2
        elif len(win_comb)==3:
            if win_comb[0] == win_comb[1]== win_comb[2]:
                print("You have a kare!!!")
                score = 6
            else:
                print("You have a set and a pair")
                score = 4
        elif len(win_comb)==4:
            if win_comb[1] == win_comb[2]:
                print("You have a kare!!!")
                score = 6
            else:
                print("You have 2 sets")
                score = 5



        for i in bot:
            for j in card_table:
                if i==j:
                    win_comb_bot.append(j)
        #print(win_comb_bot)
        if len(win_comb_bot)==0:
            for i in user:
                us = max (i, i+1)
            for j in bot:
                bs = max(j, j+1)
            if us>bs:
                score = 1
                bot_score = 0
            else:
                score = 0
                bot_score = 1
        elif len(win_comb_bot)==1:
            bot_score = 1
            print("Bot have a pair")
        elif len(win_comb_bot)==2:        
            if win_comb_bot[0] == win_comb_bot[1]:
                print("Bot have a set!")
                bot_score = 3
            else:
                print("Bot have  2 pairs")
                bot_score = 2
        elif len(win_comb_bot)==3:
            if win_comb_bot[0] == win_comb_bot[1]== win_comb_bot[2]:
                bot_score = 6
                print("Bot have a kare!!!")
            else:
                bot_score = 4
                print("Bot have a set and a pair")
        elif len(win_comb_bot)==4:
            if win_comb_bot[1] == win_comb_bot[2]:
                bot_score = 6
                print("Bot have a kare!!!")
            else:
                bot_score = 5
                print("Bot have 2 sets")
        print("You: **"+self.names_cards[user[0]]+"--"+self.names_cards[user[1]]+"**")
        print("Bot: **"+self.names_cards[bot[0]]+"--"+self.names_cards[bot[1]]+"**")
        if score>bot_score:
            print("U win bot")
        else:
            print("U lose bot")

    def game(self):
        print("U can play poker with bot, are u ready???\ny/n")
        a = input()
        if a == "y":
            self.take_card()
        else:
            print("Okey, bye!")


game = Poker()
game.game()



