import pygame

class Button:
    def bxndi(self, button_name):
        pygame.image.load("assets/" + button_name + ".png")


def main():
    pygame.init()
    pygame.display.set_mode((1050, 600))
    pygame.display.set_caption("Test2")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     # for symbol in symbols:
            #     #     action = symbol.handle_click(event)
        
        asd = Button()
        asd.bxndi("Beenden OFF")
                    
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()