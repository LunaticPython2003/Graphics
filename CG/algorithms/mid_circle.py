import pygame
import sys

class MidpointCircleAlgorithm:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Midpoint Circle Algorithm")
        self.clock = pygame.time.Clock()
        self.fps = 30  # Frames per second

    def draw_axes(self):
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.height // 2), (self.width, self.height // 2))
        pygame.draw.line(self.screen, (255, 255, 255), (self.width // 2, 0), (self.width // 2, self.height))

        font = pygame.font.Font(None, 36)
        text_x = font.render('X', True, (255, 255, 255))
        text_y = font.render('Y', True, (255, 255, 255))
        self.screen.blit(text_x, (self.width - 30, self.height // 2 - 30))
        self.screen.blit(text_y, (self.width // 2 + 10, 10))

        for i in range(-self.width // 2, self.width // 2, 50):
            pygame.draw.line(self.screen, (255, 255, 255), (self.width // 2 + i, self.height // 2 - 5),
                            (self.width // 2 + i, self.height // 2 + 5))
            font = pygame.font.Font(None, 25)
            text = font.render(str(i), True, (255, 255, 255))
            self.screen.blit(text, (self.width // 2 + i - 10, self.height // 2 + 10))

        for i in range(-self.height // 2, self.height // 2, 50):
            pygame.draw.line(self.screen, (255, 255, 255), (self.width // 2 - 5, self.height // 2 - i),
                            (self.width // 2 + 5, self.height // 2 - i))
            if i != 0:
                font = pygame.font.Font(None, 25)
                text = font.render(str(-i), True, (255, 255, 255))
                self.screen.blit(text, (self.width // 2 - 30, self.height // 2 - i - 10))

    def draw_symmetric_points(self, xc, yc, x, y):
        self.screen.set_at((xc + x + self.width // 2, yc - y + self.height // 2), (255, 255, 255))
        self.screen.set_at((xc - x + self.width // 2, yc - y + self.height // 2), (255, 255, 255))
        self.screen.set_at((xc + x + self.width // 2, yc + y + self.height // 2), (255, 255, 255))
        self.screen.set_at((xc - x + self.width // 2, yc + y + self.height // 2), (255, 255, 255))

        self.screen.set_at((xc + y + self.width // 2, yc - x + self.height // 2), (255, 255, 255))
        self.screen.set_at((xc - y + self.width // 2, yc - x + self.height // 2), (255, 255, 255))
        self.screen.set_at((xc + y + self.width // 2, yc + x + self.height // 2), (255, 255, 255))
        self.screen.set_at((xc - y + self.width // 2, yc + x + self.height // 2), (255, 255, 255))

    def midpoint_circle(self, xc, yc, radius):
        x, y = radius, 0
        p = 1 - radius

        self.draw_symmetric_points(xc, yc, x, y)

        while x > y:
            y += 1

            if p <= 0:
                p = p + 2 * y + 1
            else:
                x -= 1
                p = p + 2 * y - 2 * x + 1

            self.draw_symmetric_points(xc, yc, x, y)
            pygame.display.flip()  # Update the display

            pygame.time.Clock().tick(self.fps)  # Control the frame rate

    def run(self, xc, yc, radius):
        self.draw_axes()
        self.midpoint_circle(xc, yc, radius)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.clock.tick(30)

        pygame.quit()
        sys.exit()

# Example usage
if __name__ == "__main__":
    algorithm = MidpointCircleAlgorithm()
    algorithm.run(0, 0, 100)
