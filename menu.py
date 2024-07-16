import pygame


class Button:
    def __init__(self, text, pos, size, idle_color, active_color):
        self.text = text
        self.pos = pos
        self.size = size
        self.idle_color = idle_color
        self.active_color = active_color
        self.current_color = idle_color
        self.rect = pygame.Rect(pos, size)
        self.font = pygame.font.SysFont(None, 40)

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (
            self.rect.centerx - text_surface.get_width() // 2,
            self.rect.centery - text_surface.get_height() // 2
        ))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.current_color = self.active_color
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.current_color = self.idle_color
        return False

class CreateButton:
    @staticmethod
    def create_main_menu_buttons():
        return [
            Button("Start Game", (400, 200), (250, 50), (0, 128, 0), (0, 255, 0)),
            Button("Options", (400, 300), (250, 50), (0, 0, 128), (0, 0, 255)),
            Button("Quit", (400, 400), (250, 50), (128, 0, 0), (255, 0, 0))
        ]

    @staticmethod
    def create_start_game_buttons():
        return [
            Button("Back to Main Menu", (400, 400), (250, 50), (128, 0, 0), (255, 0, 0))
        ]

    @staticmethod
    def create_options_buttons():
        return [
            Button("Back to Main Menu", (400, 400), (250, 50), (128, 0, 0), (255, 0, 0))
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
                self.on_button_click(button.text)

    def on_button_click(self, button_text):
        if button_text == "Start Game":
            self.menu.state = "start_game"
        elif button_text == "Options":
            self.menu.state = "options"
        elif button_text == "Quit":
            self.menu.running = False
        elif button_text == "Back to Main Menu":
            self.menu.state = "main_menu"

    def draw_buttons(self, buttons):
        for button in buttons:
            button.draw(self.menu.screen)