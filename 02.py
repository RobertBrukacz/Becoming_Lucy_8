import pygame

class State:
    def __init__(self, screen):
        self.screen = screen
        
    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

class MainMenu(State):
    def __init__(self, main, screen):
        super().__init__(screen)
        self.button1 = Button(main, self.screen, (400, 200), (250, 50), "Neues Spiel OFF", "new_game")
        self.button2 = Button(main, self.screen, (400, 500), (250, 50), "Beenden OFF", "quit")

    def enter(self):
        print("Entering Main Menu")

    def exit(self):
        print("Exiting Main Menu")

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.button1.handle_click(event.pos)
                self.button2.handle_click(event.pos)

    def render(self, screen):
        self.button1.create()
        self.button2.create()

class Game(State):
    def __init__(self, screen):
        super().__init__(screen)
        self.size = (1050, 600)
        self.pos = (0, 0)
        
    def enter(self):
        print("Starting Game")
        self.screen.fill((10, 60, 40))
        self.game_background = pygame.image.load("assets/images/gameworld/Spielwelt.png")

    def exit(self):
        print("Exiting Game")

    def create(self):
        game_background_resized = pygame.transform.scale(self.game_background, self.size)
        #print("1: ", self.action)
        self.screen.blit(game_background_resized, self.pos)

    def update(self, events):
        pass  # Add logic for updating game

    def render(self, screen):
        self.create()  # Add logic for rendering game

class PauseMenu(State):
    def update(self, events):
        pass  # Placeholder for pause menu logic

    def render(self, screen):
        pass  # Placeholder for rendering pause menu

class StateManager:
    def __init__(self):
        self.current_state = None

    def change_state(self, new_state):
        if self.current_state is not None:
            self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()

    def update(self, events):
        if self.current_state is not None:
            self.current_state.update(events)

    def render(self, screen):
        if self.current_state is not None:
            self.current_state.render(screen)

class Handler:
    def __init__(self, main):
        self.main = main
        self.running = True  # Define running here for clarity

    def handling_events(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        return self.running  # Return the running status to be checked by the Main class

class Button:
    def __init__(self, main, screen, pos, size, name, action):
        self.main = main
        self.screen = screen
        self.pos = pos
        self.size = size
        self.name = name
        self.action = action
        self.rect = pygame.Rect(pos, size)
        
    def create(self):
        button = pygame.image.load("assets/buttons/" + self.name + ".png")
        button_resized = pygame.transform.scale(button, self.size)
        #print("1: ", self.action)
        self.screen.blit(button_resized, self.pos)
        #print("2: ", self.action)

    def handle_click(self, event_pos):
        if self.rect.collidepoint(event_pos):  # Überprüft, ob der Klick innerhalb des Buttons erfolgte
            self.perform_action()
            print(event_pos)
            print("3: ", self.action)

    def perform_action(self):
        #print("4: ", self.action)
        # Hier können Sie definieren, was passieren soll, wenn der Button angeklickt wird
        if self.action == "quit":
            #pygame.quit()
            #print("5: ", self.action)
            #print(self.running)
            #print(self.main.current_state)
            #self.main.current_state = "quit"
            self.main.running = False
        elif self.action == "new_game":
            self.main.start_new_game()

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Becoming Lucy")
        self.screen = pygame.display.set_mode((1050, 600))
        self.running = True
        self.state_manager = StateManager()
        self.state_manager.change_state(MainMenu(self, self.screen))  # Start with main menu

    def run(self):
        handler = Handler(self)
        #print("1: ", self.running)
        while self.running:
            #print("2: ", self.running)
            events = pygame.event.get()
            #print("3: ", self.running)
            self.running = handler.handling_events(events)
            #print("4: ", self.running)
            self.state_manager.update(events)
            self.state_manager.render(self.screen)
            #print("5: ", self.running)
            pygame.display.flip()
        pygame.quit()

    def start_new_game(self):
        self.state_manager.change_state(Game(self.screen))
        
if __name__ == "__main__":
    main = Main()
    main.run()