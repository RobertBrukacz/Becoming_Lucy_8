import pygame

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
        
class Menu:
    def __init__(self, buttons):
        self.buttons = buttons
        # self.main_menu_buttons = self.create_main_menu_buttons()
        # self.start_game_buttons = self.create_start_game_buttons()
        # self.options_buttons = self.create_options_buttons()
        
    def create_main_menu_buttons(self):
        if self.buttons <= 6:
            button = []
            for i in range(self.buttons):
                #button[i]("Button " +i, (400, 200), (250, 50), (0, 128, 0), (0, 255, 0))
                button.append(Button((400, 200 + i * 60), (250, 50), f'Button {i+1}', f'action_{i+1}'))
            return button
        else:
            print("Too many buttons")
    
    def 

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Test3")
        self.screen = pygame.display.set_mode((1050, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.state = "main_menu"

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(
                        f"Mouse position: {pygame.mouse.get_pos()}"
                    )
                    self.handle_mouse()
            self.update()
            self.render()
            self.clock.tick(self.fps)
        pygame.quit()

    def update(self):
        menu_states = {
            "main_menu",
            "start_game",
            "options",
            "quit"
        }
        menu_state = "..."
        # print(menu_state)
        # print(self.state)
        menu1 = Menu(6)
        menu1.create_main_menu_buttons()
        
        # for state in menu_states:
        #     if self.state == state:
        #         menu_states[state]()

    def render(self):
        
        pygame.display.flip()
        
    def handle_mouse(self):
        pass

if __name__ == "__main__":
    main = Main()
    main.run()
