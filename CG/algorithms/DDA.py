import pygame
import sys

class algo:
    width, height = 1000, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("DDA Algorithm")
    clock = pygame.time.Clock()
    def __init__(self):
        pygame.init()
    def draw_axes(self, screen, width, height):
        pygame.draw.line(self.screen, (255, 255, 255), (0, height // 2), (width, height // 2)) 
        pygame.draw.line(self.screen, (255, 255, 255), (width // 2, 0), (width // 2, height))

        for i in range(-width // 2, width // 2, 50):
            pygame.draw.line(self.screen, (255, 255, 255), (width // 2 + i, height // 2 - 5),
                            (width // 2 + i, height // 2 + 5))
            font = pygame.font.Font(None, 25)
            text = font.render(str(i), True, (255, 255, 255))
            self.screen.blit(text, (width // 2 + i - 10, height // 2 + 10))

        for i in range(-height // 2, height // 2, 50):
            pygame.draw.line(self.screen, (255, 255, 255), (width // 2 - 5, height // 2 - i),
                            (width // 2 + 5, height // 2 - i))
            if i != 0: 
                font = pygame.font.Font(None, 25)
                text = font.render(str(-i), True, (255, 255, 255))
                self.screen.blit(text, (width // 2 - 30, height // 2 - i - 10))

    def DDA_line(self, screen, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1

        # Determine the number of steps
        steps = max(abs(dx), abs(dy))

        # Calculate increments
        x_increment = dx / steps
        y_increment = dy / steps

        # Initial point
        x = x1
        y = y1

        # Draw the initial point
        screen.set_at((int(x) + self.width // 2, self.height // 2 - int(y)), (255, 255, 255))

        for _ in range(int(steps)):
            pygame.display.flip()
            self.clock.tick(30)
            x += x_increment
            y += y_increment

            # Draw the next point
            screen.set_at((int(x) + self.width // 2, self.height // 2 - int(y)), (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def run(self, x1, y1, x2, y2):
        self.draw_axes(self.screen, self.width, self.height)
        self.DDA_line(self.screen, x1, y1, x2, y2)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False

if __name__=="__main__":
    algo = algo()
    x1 = int(input("Enter the number: "))
    algo.run(x1, 100, 0, 0)