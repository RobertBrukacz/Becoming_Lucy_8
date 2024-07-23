import pygame

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Test4")
        self.screen = pygame.display.set_mode((1050, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.state = "main_menu"
        self.font = pygame.font.SysFont(None, 40)
        self.menu = self.Menu(self)

    class Menu:
        def __init__(self, main):
            self.main = main
            self.buttons = [
                self.Button((400, 300), (250, 50), 'Start Game', 'start_game'),
                self.Button((400, 400), (250, 50), 'Quit', 'quit')
            ]

        def handle_click(self, event):
            for button in self.buttons:
                action = button.handle_click(event)
                if action:
                    self.main.perform_action(action)

        def render(self):
            self.main.screen.fill((0, 0, 0))
            for button in self.buttons:
                button.draw(self.main.screen)
            pygame.display.flip()

        class Button:
            def __init__(self, pos, size, text, action):
                self.pos = pos
                self.size = size
                self.text = text
                self.action = action
                self.rect = pygame.Rect(pos, size)
                self.font = pygame.font.SysFont(None, 40)
                self.color = (128, 128, 128)
                self.text_color = (255, 255, 255)

            def draw(self, screen):
                pygame.draw.rect(screen, self.color, self.rect)
                text_surface = self.font.render(self.text, True, self.text_color)
                screen.blit(text_surface, (
                    self.rect.centerx - text_surface.get_width() // 2,
                    self.rect.centery - text_surface.get_height() // 2
                ))

            def handle_click(self, event):
                if self.rect.collidepoint(event.pos):
                    return self.action
                return None

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.menu.handle_click(event)
            self.update()
            self.render()
            self.clock.tick(self.fps)
        pygame.quit()

    def update(self):
        pass  # Aktualisiere hier die Spiel- oder Menülogik, falls nötig

    def render(self):
        if self.state == "main_menu":
            self.menu.render()

    def perform_action(self, action):
        if action == 'start_game':
            self.state = 'start_game'
            print(self.state)
        elif action == 'quit':
            self.running = False

if __name__ == "__main__":
    main = Main()
    main.run()
