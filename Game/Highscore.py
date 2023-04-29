import hashlib
import fileinput
import operator
import os


class Highscore:

    def __init__(self):
        self.__highscore = self.load()

    def getScores(self):
        return self.__highscore

    def load(self):
        highscore = self.buildHighscoreArray()

        highscore.sort(key=operator.itemgetter(1), reverse=True)
        highscore = highscore[0:11]

        return highscore

    def add(self, name, score):
        if self.nameShouldBeAdded(name, score):
            hash = hashlib.md5((str(name + str(score) + "pygame")).encode('utf-8'))
            self.__highscore.append([name, str(score), hash.hexdigest()])

            f = open(os.path.join("Game", "highscore.dat"), 'w')
            for name, score, md5 in self.__highscore:
                f.write(str(name) + "[::]" + str(score) + "[::]" + str(md5) + "\n")

            f.close()

    def buildHighscoreArray(self):
        highscore = []
        for line in fileinput.input(os.path.join("Game", "highscore.dat")):
            name, score, md5 = line.split('[::]')
            md5 = md5.replace('\n', '')

            if str(hashlib.md5(str.encode(str(name + score + "pygame"))).hexdigest()) == str(md5):
                highscore.append([str(name), int(score), str(md5)])

        return highscore

    def nameShouldBeAdded(self, name, score):
        highscore = self.buildHighscoreArray()
        lineToDelete = -1
        for i, x in enumerate(highscore):
            if x[0] == name:
                if x[1] < score:
                    lineToDelete = i
                else:
                    return False

        if lineToDelete > -1:
            self.deleteLine(lineToDelete)
        return True

    def deleteLine(self, lineNumber):
        lines = []
        with open(os.path.join("Game", "highscore.dat"), 'r') as fp:
            lines = fp.readlines()

        with open(os.path.join("Game", "highscore.dat"), 'w') as fp:
            for number, line in enumerate(lines):
                if number not in [lineNumber]:
                    fp.write(line)
        fp.close()
