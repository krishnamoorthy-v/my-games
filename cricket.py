import random
import time
import copy


class Cricket:

    def __init__(self):                                      # Get the attribute of the match from the user
        matchtype_dict = {'S': 'SINGLE PLAYER', 'M': 'MULTI PLAYER'}
        self.name = input("Enter the name of the team:")
        self.over = int(input("Enter the number of over:"))
        self.wicket = 0
        self.total_score = 0
        match_type = str(input("Enter the match type 'SINGLE PLAYER' for 'S' or 'MULTI PLAYER' for 'M':")).upper()
        self.matchtype = matchtype_dict[match_type]

    def getdata(self):
        self.name = input("Enter the name of the team:")

    def batting_engine(self, opt, score_list):                  # score generator

        attack = [6, 4, 4, 'w', 'w', 6, 4, ]                    # Three mode of player is declared
        defence = ['w', 0, 0, 1, 1, 2]
        play = ['w', 1, 1, 2, 3, 2]
        dct = {'A': attack, 'D': defence, 'P': play}
        for x in range(1, 7):                                   # converting over into ball
            score = random.choice(dct[opt])                    # main generator
            if score == 'w':
                self.wicket += 1                                # wicket management
            # score_list.append(score)                            # storing the score in list
            if self.wicket > 11:
                score = '-'
            score_list.append(score)

    def score_cal(self, score_list, total_score_in_over, i):

        total = 0
        for j in score_list:                                    # adding total score in the over list
            if j == 'w' or j == '-':
                j = 0
                total += j
            else:
                total += j
        if i <= self.over:
            print(f"{i} over score {score_list} total = {total}")
            del score_list[:]                                      # deleting the score list element after calculation
        total_score_in_over.append(total)                              # store the over total for total score of one team
        if i == self.over or self.wicket == 11:
            # self.total_score = 0
            for k in total_score_in_over:                              # total score calculation of team score
                self.total_score += k
            print()
            print(f"\t\tTotal wicket {self.wicket}     Total score {self.total_score}")
            print()

    def toss(self, self2):

        toss_dict = {"H": "Head", "T": "Tail"}
        toss_input = str(input("Choose 'Head' by 'H' or 'Tail' by 'T':")).upper()
        Toss = ['Head', 'Tail']
        Toss_results = random.choice(Toss)        # toss generator
        if toss_dict[toss_input] == Toss_results:
            print("\t\tyou won")
            side_choosing_dict = {'B': 'BATTING', 'F': 'FIELDING'}
            side_choosing = str(input("Choose 'BATTING' by 'B' or 'FIELDING' by 'F':")).upper()
            self.toss_result = side_choosing_dict[side_choosing]
            if side_choosing == 'B':
                self2.toss_result = "FIELDING"
            else:
                self2.toss_result = "BATTING"
            print(f"\t{self.name} choose {self.toss_result}")
        else:
            print("\t\tyou loss toss")
            side_choosing_dict = {'B': 'BATTING', 'F': 'FIELDING'}
            side_choosing_list = ['B', 'F']
            toss_result_choosing = random.choice(side_choosing_list)
            self2.toss_result = side_choosing_dict[toss_result_choosing]
            if self2.toss_result == 'BATTING':
                self.toss_result = "FIELDING"
            else:
                self.toss_result = "BATTING"
            print(f"\t{self2.name} choose {self2.toss_result}")

    def match_winning_dicision(self, self2):
        if self.total_score > self2.total_score:
            print("\t\t***************************************")
            print(f"\t\t{self.name} won the match in {self.total_score - self2.total_score} run difference")
            print("\t\t***************************************")
        elif self.total_score < self2.total_score:
            print("\t\t***************************************")
            print(f"\t\t{self2.name} won the match in {self2.total_score - self.total_score} run difference")
            print("\t\t***************************************")
        elif self.total_score == self2.total_score:
            print("\t\t************************************")
            print('\t\t\t\tmatch draw')
            print("\t\t************************************")

    def mainloop(self, control):
        score_list = []
        total_score_in_over = []
        if control == 'auto':
            for i in range(1, self.over + 1):            # over generator
                if self.wicket < 11:
                    print()
                    control_lst = ['A', 'D', 'P']
                    control_auto_choice = random.choice(control_lst)
                    print("Enter the mode of play 'A' for ATTACK, 'D' for DEFENCE, 'P' for PLAY:", control_auto_choice)  # choosing mode of playing
                    opt = control_auto_choice                                                                           # checking wicket state in this line
                    self.batting_engine(opt, score_list)                                        # assessing the batting engine
                    print("PROCESSING", end='')                                 # printing the processing in slow mode is done in this line
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.')
                    self.score_cal(score_list, total_score_in_over, i)              # calling the score_cal()
                else:
                    print()
                    print('\t\tAll wicket')
                    print()
                    break
        else:
            for i in range(1, self.over + 1):  # over generator
                if self.wicket <= 11:  # checking wicket state in this line
                    print()
                    opt = str(input("Enter the mode of play 'A' for ATTACK, 'D' for DEFENCE, 'P' for PLAY:")).upper()  # choosing mode of playing
                    self.batting_engine(opt, score_list)  # assessing the batting engine
                    print("PROCESSING", end='')  # printing the processing in slow mode is done in this line
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.')
                    self.score_cal(score_list, total_score_in_over, i)  # calling the score_cal()
                else:
                    print()
                    print('\t\tAll wicket')
                    print()
                    break


    def matchtype_dicision_making(self, self2):
        if self.matchtype == 'SINGLE PLAYER':
            c.toss(self2)
            if self.toss_result == 'BATTING' and self2.toss_result == 'FIELDING':
                print(f"************* {self.name} Batting *****************")
                c.mainloop(control='manual')
                print(f"************* {self2.name} Batting *****************")
                self2.mainloop(control='auto')
            elif self2.toss_result == 'BATTING' and self.toss_result == 'FIELDING':
                print(f"************* {self2.name} Batting *****************")
                self2.mainloop(control='auto')
                print(f"************* {self.name} Batting *****************")
                c.mainloop(control='manual')
            self.match_winning_dicision(self2)
        elif self.matchtype == "MULTI PLAYER":
            toss_asking = ['first', 'second']
            random_toss_asking = random.choice(toss_asking)
            if random_toss_asking == toss_asking[0]:
                print()
                print(f"\t{c.name} have a chance to ask the toss")
                c.toss(self2)
                if self.toss_result == 'BATTING' and self2.toss_result == 'FIELDING':
                    print(f"************* {self.name} Batting *****************")
                    c.mainloop(control='manual')
                    print(f"************* {self2.name} Batting *****************")
                    self2.mainloop(control='manual')
                elif self2.toss_result == 'BATTING' and self.toss_result == 'FIELDING':
                    print(f"************* {self2.name} Batting *****************")
                    self2.mainloop(control='manual')
                    print(f"************* {self.name} Batting *****************")
                    c.mainloop(control='manual')
            elif random_toss_asking == toss_asking[1]:
                print()
                print(f"\t{self2.name} have a chance to ask the toss")
                self2.toss(c)
                if self.toss_result == 'BATTING' and self2.toss_result == 'FIELDING':
                    print(f"************* {self.name} Batting *****************")
                    c.mainloop(control='manual')
                    print(f"************* {self2.name} Batting *****************")
                    self2.mainloop(control='manual')
                elif self2.toss_result == 'BATTING' and self.toss_result == 'FIELDING':
                    print(f"************* {self2.name} Batting *****************")
                    self2.mainloop(control='manual')
                    print(f"************* {self.name} Batting *****************")
                    c.mainloop(control='manual')
            self.match_winning_dicision(self2)


c = Cricket()
if c.matchtype == "SINGLE PLAYER":
    # computer = Cricket()
    computer = copy.deepcopy(c)
    computer.name = 'prime'
    c.matchtype_dicision_making(computer)
    print(c.__dict__)
    print(computer.__dict__)

elif c.matchtype == "MULTI PLAYER":
    # player2 = Cricket()
    player2 = copy.deepcopy(c)
    player2.getdata()
    c.matchtype_dicision_making(player2)
    print(c.__dict__)
    print(player2.__dict__)