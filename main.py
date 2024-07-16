import pygame
from menu import Button

class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Menu with Buttons")
        self.screen = pygame.display.set_mode((1050, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.buttons = [
            Button("Start Game", (400, 200), (250, 50), (0, 128, 0), (0, 255, 0)),
            Button("Options", (400, 300), (250, 50), (0, 0, 128), (0, 0, 255)),
            Button("Quit", (400, 400), (250, 50), (128, 0, 0), (255, 0, 0))
        ]

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            for button in self.buttons:
                button.handle_event(event)

    def update(self):
        # Hier wird die Menü-Logik aktualisiert, falls nötig
        pass

    def render(self):
        self.screen.fill((0, 0, 0))  # Bildschirm schwarz füllen
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    menu = Menu()
    menu.run()
