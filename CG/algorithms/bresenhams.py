import pygame
import sys

class BresenhamAlgorithm:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bresenham Algorithm")
        self.clock = pygame.time.Clock()

    def draw_axes(self):
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.height // 2), (self.width, self.height // 2))
        pygame.draw.line(self.screen, (255, 255, 255), (self.width // 2, 0), (self.width // 2, self.height))

    def bresenham_line(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        err = dx - dy

        x, y = x1, y1

        while True:
            self.screen.set_at((x + self.width // 2, self.height // 2 - y), (255, 255, 255))
            pygame.display.flip()  # Update the display

            pygame.time.delay(50)  # Introduce a delay of 50 milliseconds

            if x == x2 and y == y2:
                break

            e2 = 2 * err

            if e2 > -dy:
                err -= dy
                x += sx

            if e2 < dx:
                err += dx
                y += sy

    def run(self, x1, y1, x2, y2):
        self.draw_axes()
        self.bresenham_line(x1, y1, x2, y2)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

# Example usage
if __name__ == "__main__":
    algorithm = BresenhamAlgorithm()
    algorithm.run(-300, -300, 200, 200)
