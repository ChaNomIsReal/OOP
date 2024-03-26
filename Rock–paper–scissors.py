import pygame
import random
import sys
# กำหนดสี
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0 ,0)

# กำหนดขนาดหน้าจอ
WIDTH, HEIGHT = 800, 600

# กำหนดเลขความเร็วของเกม
FPS = 30

# กำหนดค่าต่าง ๆ ของเกม
CHOICES = ['rock', 'paper', 'scissors']
WINNING_CONDITIONS = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Rock Paper Scissors")
        self.clock = pygame.time.Clock()
        self.player_choice = None
        self.computer_choice = None
        self.rock_image = pygame.image.load("images/rock.png")
        self.paper_image = pygame.image.load("images/paper.png")
        self.scissors_image = pygame.image.load("images/scissors.png")

    def draw_text(self, text, font_size, x, y, color=WHITE):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
    def draw_images(self, player_choice, computer_choice):
        # กำหนดตำแหน่งที่ต้องการแสดงรูปภาพ
        player_x, player_y = WIDTH // 6, HEIGHT // 5
        computer_x, computer_y = WIDTH * 4 // 6, HEIGHT // 5
        image_size = (150, 150)  # 
        if player_choice == 'rock':
            self.screen.blit(pygame.transform.scale(self.rock_image, image_size), (player_x, player_y))
        elif player_choice == 'paper':
            self.screen.blit(pygame.transform.scale(self.paper_image, image_size), (player_x, player_y))
        elif player_choice == 'scissors':
            self.screen.blit(pygame.transform.scale(self.scissors_image, image_size), (player_x, player_y))

        # วาดรูปภาพของคอมพิวเตอร์
        if computer_choice == 'rock':
            self.screen.blit(pygame.transform.scale(self.rock_image, image_size), (computer_x, computer_y))
        elif computer_choice == 'paper':
            self.screen.blit(pygame.transform.scale(self.paper_image, image_size), (computer_x, computer_y))
        elif computer_choice == 'scissors':
            self.screen.blit(pygame.transform.scale(self.scissors_image, image_size), (computer_x, computer_y))
    def run(self):
        running = True
        while running:
            self.screen.fill(BLACK)
            self.draw_text("Choose: Rock(R), Paper(P), or Scissors(S)", 30, WIDTH // 2, 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.player_choice = 'rock'
                    elif event.key == pygame.K_p:
                        self.player_choice = 'paper'
                    elif event.key == pygame.K_s:
                        self.player_choice = 'scissors'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # ตรวจสอบปุ่มซ้ายของเมาส์
                        mouse_pos = pygame.mouse.get_pos()
                        if exit_button.collidepoint(mouse_pos):
                            running = False

            if self.player_choice:
                self.computer_choice = random.choice(CHOICES)
                result = self.determine_winner()
                self.draw_images(self.player_choice, self.computer_choice)
                self.draw_text(f"Player: {self.player_choice}", 30, WIDTH // 4, HEIGHT // 2)
                self.draw_text(f"Computer: {self.computer_choice}", 30, WIDTH * 3 // 4, HEIGHT // 2)
                self.draw_text(result, 40, WIDTH // 2, HEIGHT * 3 // 4)
                self.player_choice = None
                self.draw_text("Resetting game...", 30, WIDTH // 2, HEIGHT - 50, color=RED)
                pygame.display.flip()
                pygame.time.wait(3000)
            exit_button = pygame.draw.rect(self.screen, BLUE, (WIDTH - 100, 20, 80, 40))
            self.draw_text("Exit", 30, WIDTH - 60, 40, color=WHITE)
            pygame.display.update()
            self.clock.tick(FPS)
    
    def determine_winner(self):
        if self.player_choice == self.computer_choice:
            return "It's a tie!"
        elif WINNING_CONDITIONS[self.player_choice] == self.computer_choice:
            return "You win!"
        else:
            return "Computer wins!"

if __name__ == "__main__":
    game = Game()
    game.run()
