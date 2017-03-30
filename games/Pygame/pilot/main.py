import pygame
from pygame.locals import *


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 760, 480
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.K_w:
            print 'Ha presionao w'

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self.clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        print 'Presionaste w'
                    if event.key == pygame.K_RIGHT:
                        print 'Presionaste ->'
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
