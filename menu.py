import pygame


import pygame


class Button:
    def __init__(self, pos, size, idle_image, active_image):
        self.pos = pos
        self.size = size
        self.idle_image = pygame.transform.scale(idle_image, size)
        self.active_image = pygame.transform.scale(active_image, size)
        self.current_image = self.idle_image
        self.rect = pygame.Rect(pos, size)

    def draw(self, screen):
        screen.blit(self.current_image, self.pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.current_image = self.active_image
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.current_image = self.idle_image
        return False


class CreateButton:
    @staticmethod
    def create_main_menu_buttons():
        return [
            Button((400, 200), (250, 50), pygame.image.load("assets/Neues Spiel OFF.png"), pygame.image.load("assets/Neues Spiel ON.png")),
            Button((400, 300), (250, 50), pygame.image.load("assets/Einstellungen OFF.png"), pygame.image.load("assets/Einstellungen ON.png")),
            Button((400, 400), (250, 50), pygame.image.load("assets/Beenden OFF.png"), pygame.image.load("assets/Beenden ON.png"))
        ]

    @staticmethod
    def create_start_game_buttons():
        return [
            Button((400, 400), (250, 50), pygame.image.load("assets/Hauptmenü OFF.png"), pygame.image.load("assets/Hauptmenü ON.png"))
        ]

    @staticmethod
    def create_options_buttons():
        return [
            Button((400, 400), (250, 50), pygame.image.load("assets/Hauptmenü OFF.png"), pygame.image.load("assets/Hauptmenü ON.png"))
        ]

class Menu:
    def __init__(self, menu):
        self.menu = menu

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menu.running = False
            if self.menu.state == "main_menu":
                self.handle_menu_events(self.menu.main_menu_buttons, event)
            elif self.menu.state == "start_game":
                self.handle_menu_events(self.menu.start_game_buttons, event)
            elif self.menu.state == "options":
                self.handle_menu_events(self.menu.options_buttons, event)

    def handle_menu_events(self, buttons, event):
        for button in buttons:
            if button.handle_event(event):
                self.on_button_click(button)

    def on_button_click(self, button):
        if button == self.menu.main_menu_buttons[0]:  # Start Game
            self.menu.state = "start_game"
        elif button == self.menu.main_menu_buttons[1]:  # Options
            self.menu.state = "options"
        elif button == self.menu.main_menu_buttons[2]:  # Quit
            self.menu.running = False
        elif button in self.menu.start_game_buttons or button in self.menu.options_buttons:  # Back to Main Menu
            self.menu.state = "main_menu"

    def draw_buttons(self, buttons):
        for button in buttons:
            button.draw(self.menu.screen)