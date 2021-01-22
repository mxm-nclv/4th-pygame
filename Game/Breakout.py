import pygame

from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants

class Breakout:

    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level()
        self.__level.load(0)

    def start(self):
        pass

    def changeScene(self, scene):
        pass

    def getLevel(self):
        pass

    def getScore(self):
        pass

    def increaseScore(self, score):
        pass

    def getLives(self):
        pass

    def getBalls(self):
        pass

    def getPad(self):
        pass

    def playSound(self, soundClip):
        pass

    def reduceLives(self):
        pass

    def increaseLives(self):
        pass

    def reset(self):
        pass


Breakout().start()
