import pygame
from menu import Menu, CreateButton

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Menu with Buttons")
        self.screen = pygame.display.set_mode((1050, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.state = "main_menu"
        self.main_menu_buttons = CreateButton.create_main_menu_buttons()
        self.start_game_buttons = CreateButton.create_start_game_buttons()
        self.options_buttons = CreateButton.create_options_buttons()
        self.handler = Menu(self)

    def run(self):
        while self.running:
            self.handler.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
        pygame.quit()

    def update(self):
        # Hier wird die Menü-Logik aktualisiert, falls nötig
        pass

    def render(self):
        self.screen.fill((0, 0, 0))  # Bildschirm schwarz füllen
        if self.state == "main_menu":
            self.handler.draw_buttons(self.main_menu_buttons)
        elif self.state == "start_game":
            self.handler.draw_buttons(self.start_game_buttons)
        elif self.state == "options":
            self.handler.draw_buttons(self.options_buttons)
        pygame.display.flip()

if __name__ == "__main__":
    main = Main()
    main.run()
