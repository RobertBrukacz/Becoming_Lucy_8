import pygame

class Handler:
    def __init__(self, main):
        self.main = main
        
    def handling_events(self, running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return self.running
                #return self.current_state == "quit"
class Assets:
    def __init__(self):
        self.background = pygame.image.load("assets/Beenden OFF.png")
        self.button = pygame.image.load("assets/Beenden ON.png")

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Becoming Lucy")
        self.screen = pygame.display.set_mode((1050, 600))
        self.running = True
        self.current_state = "main_menu"
        self.assets = Assets()

    def run(self):
        handler = Handler(self)
        while self.running:
            handler.handling_events(self.running)
            if self.current_state == "main_menu":
                print(self.current_state)
                # print(handler.handling_events())
                # print(self.running)
                while self.current_state == "main_menu":
                    #handler = Handler(self)
                    handler.handling_events(self.running)
                    print(self.current_state)
                    print(self.running)
            if self.current_state == "quit":
                self.running = False
                pygame.quit()

            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    main = Main()
    main.run()