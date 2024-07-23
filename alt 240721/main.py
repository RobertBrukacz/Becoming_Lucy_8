import pygame
from menu import Menu, ButtonFactory

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Menu with Buttons")
        self.screen = pygame.display.set_mode((1050, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.state = "main_menu"
        self.main_menu_buttons = ButtonFactory.create_main_menu_buttons()
        self.start_game_buttons = ButtonFactory.create_start_game_buttons()
        self.options_buttons = ButtonFactory.create_options_buttons()
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
        Menu.button_render(self)
        pygame.display.flip()

if __name__ == "__main__":
    main = Main()
    main.run()
