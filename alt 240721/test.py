import pygame

class ClickableSymbol:
    def __init__(self, pos, size, text, action):
        self.pos = pos
        self.size = size
        self.text = text
        self.action = action
        self.rect = pygame.Rect(pos, size)
        self.font = pygame.font.SysFont(None, 40)

    def draw(self, screen):
        pygame.draw.rect(screen, (228, 28, 128), self.rect, 3, 50, 5, 5, 50)
        text_surface = self.font.render(self.text, True, (190, 150, 190))
        screen.blit(text_surface, (
            self.rect.centerx - text_surface.get_width() // 2,
            self.rect.centery - text_surface.get_height() // 2
        ))

    def handle_click(self, event):
        if self.rect.collidepoint(event.pos):
            return self.action
        return None

class ValueManager:
    def __init__(self):
        self.value = 1
        self.font = pygame.font.SysFont(None, 60)

    def draw(self, screen, pos):
        value_surface = self.font.render(str(self.value), True, (215, 205, 105))
        screen.blit(value_surface, pos)

    def apply_action(self, action):
        if action == '+':
            self.value += 1
        elif action == '-':
            self.value -= 1
        elif action == 'x2':
            self.value *= 2
        elif action == 'x5':
            self.value *= 5
        elif action == 'x10':
            self.value *= 10
        elif action == '/2':
            self.value //= 2
        elif action == '/5':
            self.value //= 5
        elif action == '/10':
            self.value //= 10

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Value Manager")
    clock = pygame.time.Clock()
    running = True

    # Initialer Wert
    value_manager = ValueManager()

    # Symbole
    symbols = [
        ClickableSymbol((100, 100), (50, 50), '+', '+'),
        ClickableSymbol((160, 100), (50, 50), '-', '-'),
        ClickableSymbol((220, 100), (50, 50), 'x2', 'x2'),
        ClickableSymbol((280, 100), (50, 50), 'x5', 'x5'),
        ClickableSymbol((340, 100), (50, 50), 'x10', 'x10'),
        ClickableSymbol((400, 100), (50, 50), '/2', '/2'),
        ClickableSymbol((460, 100), (50, 50), '/5', '/5'),
        ClickableSymbol((520, 100), (50, 50), '/10', '/10')
    ]

    idiotic_value = 1  # Startwert für idiotic_value
    click_count = 0    # Zähler für die Anzahl der Klicks

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for symbol in symbols:
                    action = symbol.handle_click(event)
                    if action:
                        value_manager.apply_action(action)
                        click_count += 1  # Erhöhe den Klick-Zähler

        screen.fill((30, 10, 50))  # Bildschirm schwarz füllen

        # Zeichnen der Symbole
        for symbol in symbols:
            symbol.draw(screen)

        # Zeichnen des Werts
        value_manager.draw(screen, (100, 200))

        # Ausgabe des idiotic_value und des Klick-Zählers in der Konsole
        print(f"Idiotic Value: {idiotic_value}, Click Count: {click_count}")

        # Erhöhen des idiotic_value um 1
        idiotic_value += 1

        # Zeichnen des Klick-Zählers auf dem Bildschirm
        click_count_surface = pygame.font.SysFont(None, 40).render(f"Click Count: {click_count}", True, (255, 255, 255))
        screen.blit(click_count_surface, (100, 300))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
