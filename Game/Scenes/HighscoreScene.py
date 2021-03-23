import pygame
from Game.Scenes.Scene import Scene


class HighscoreScene(Scene):

    def __init__(self, game):
        super(HighscoreScene, self).__init__(game)

    def handleEvents(self, events):
        super(HighscoreScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
