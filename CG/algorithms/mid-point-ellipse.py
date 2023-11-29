import pygame
import sys

class MidpointEllipseAlgorithm:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Midpoint Ellipse Algorithm")
        self.clock = pygame.time.Clock()
        self.fps = 15  # Frames per second

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

    def midpoint_ellipse(self, xc, yc, rx, ry):
        x, y = 0, ry
        p1 = ry**2 - rx**2 * ry + 0.25 * rx**2

        self.draw_symmetric_points(xc, yc, x, y)

        while 2 * (ry**2) * x < 2 * (rx**2) * y:
            x += 1

            if p1 < 0:
                p1 = p1 + 2 * (ry**2) * x + (ry**2)
            else:
                y -= 1
                p1 = p1 + 2 * (ry**2) * x - 2 * (rx**2) * y + (ry**2)

            self.draw_symmetric_points(xc, yc, x, y)
            pygame.display.flip()  # Update the display

            pygame.time.Clock().tick(self.fps)  # Control the frame rate

        p2 = (ry**2) * (x + 0.5)**2 + (rx**2) * (y - 1)**2 - (rx**2) * (ry**2)

        while y >= 0:
            y -= 1

            if p2 > 0:
                p2 = p2 - 2 * (rx**2) * y + (rx**2)
            else:
                x += 1
                p2 = p2 + 2 * (ry**2) * x - 2 * (rx**2) * y + (rx**2)

            self.draw_symmetric_points(xc, yc, x, y)
            pygame.display.flip()  # Update the display

            pygame.time.Clock().tick(self.fps)  # Control the frame rate

    def run(self, xc, yc, rx, ry):
        self.draw_axes()
        self.midpoint_ellipse(xc, yc, rx, ry)

        pygame.time.delay(2000)  # Introduce a delay after the ellipse is

if __name__ == "__main__":
    algorithm = MidpointEllipseAlgorithm()
    algorithm.run(0, 0, 100, 50)