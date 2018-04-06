# https://www.reddit.com/r/dailyprogrammer/comments/87rz8c/20180328_challenge_355_intermediate_possible/


class Pies:
    pumpkinrecipe = [1, 3, 4, 3]
    applerecipe = [1, 4, 3, 2]

    def __init__(self, pumpkin, apple, egg, milk, sugar):
        self.pumpkin = pumpkin
        self.apple = apple
        self.egg = egg
        self.milk = milk
        self.sugar = sugar
        self.pumpkinpies = 0
        self.applepies = 0

    def getremainingpumpkinkspie(self):
        return min(self.pumpkin / self.pumpkinrecipe[0],
                   self.egg / self.pumpkinrecipe[1],
                   self.milk / self.pumpkinrecipe[2],
                   self.sugar / self.pumpkinrecipe[3])

    def getremainingapplespie(self):
        return min(self.apple / self.applerecipe[0],
                   self.egg / self.applerecipe[1],
                   self.milk / self.applerecipe[2],
                   self.sugar / self.applerecipe[3])

    def bakeapumpkinpie(self):
        self.pumpkin -= self.pumpkinrecipe[0]
        self.egg -= self.pumpkinrecipe[1]
        self.milk -= self.pumpkinrecipe[2]
        self.sugar -= self.pumpkinrecipe[3]

    def bakeanapplepie(self):
        self.apple -= self.applerecipe[0]
        self.egg -= self.applerecipe[1]
        self.milk -= self.applerecipe[2]
        self.sugar -= self.applerecipe[3]

    def getmaxpies(self):
        remainingpumpkinspie = self.getremainingpumpkinkspie()
        remainingapplespie = self.getremainingapplespie()
        maxvalue = int(max(remainingapplespie, remainingpumpkinspie))
        while maxvalue > 0:
            if maxvalue == int(remainingpumpkinspie):
                self.pumpkinpies += 1
                self.bakeapumpkinpie()
            else:
                self.applepies += 1
                self.bakeanapplepie()

            remainingpumpkinspie = self.getremainingpumpkinkspie()
            remainingapplespie = self.getremainingapplespie()
            maxvalue = int(max(remainingapplespie, remainingpumpkinspie))

        return self.pumpkinpies, self.applepies


# Insert here the number of ingredients in the order:
# pumpkin, apple, egg, milk, sugar
pies = Pies(12, 14, 20, 42, 24)
pumpkins, apples = pies.getmaxpies()
print(str(pumpkins) + " " + str(apples))
