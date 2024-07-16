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
        elif event.type == pygame.MOUSEBUTTONUP:
            self.current_color = self.idle_color