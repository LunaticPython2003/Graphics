import pygame
import sys
import math

class TranslationAlgorithm:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2D Line Translation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 20)
        self.scaling_factor = 20  # Increase the scaling factor for more spacing

    def draw_axes(self, initial_point, translated_point, distance):
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.height // 2), (self.width, self.height // 2))
        pygame.draw.line(self.screen, (255, 255, 255), (self.width // 2, 0), (self.width // 2, self.height))

        font = pygame.font.Font(None, 36)
        text_x = font.render('X', True, (255, 255, 255))
        text_y = font.render('Y', True, (255, 255, 255))
        self.screen.blit(text_x, (self.width - 30, self.height // 2 - 30))
        self.screen.blit(text_y, (self.width // 2 + 10, 10))

        # Draw the initial point
        self.draw_point(initial_point, (255, 0, 0), 'Initial Point')

        # Draw the translated point
        self.draw_point(translated_point, (0, 255, 0), 'Translated Point')

        # Draw the line between initial and translated points
        pygame.draw.line(self.screen, (255, 255, 255),
                         (initial_point[0] * self.scaling_factor + self.width // 2, self.height // 2 - initial_point[1] * self.scaling_factor),
                         (translated_point[0] * self.scaling_factor + self.width // 2, self.height // 2 - translated_point[1] * self.scaling_factor))

        # Draw the coordinate points and their labels
        self.draw_coordinate_points()

        # Calculate and draw the distance label
        mid_point = ((initial_point[0] + translated_point[0]) / 2, (initial_point[1] + translated_point[1]) / 2)
        distance_label = self.font.render(f'T = {distance}', True, (255, 255, 255))
        self.screen.blit(distance_label, (mid_point[0] * self.scaling_factor + self.width // 2, self.height // 2 - mid_point[1] * self.scaling_factor))

        pygame.display.flip()  # Update the display

    def draw_point(self, point, color, label):
        pygame.draw.circle(self.screen, color, (point[0] * self.scaling_factor + self.width // 2, self.height // 2 - point[1] * self.scaling_factor), 5)
        text = self.font.render(f'{label}: ({point[0]}, {point[1]})', True, color)
        self.screen.blit(text, (point[0] * self.scaling_factor + self.width // 2 + 10, self.height // 2 - point[1] * self.scaling_factor - 15))

    def draw_coordinate_points(self):
        for i in range(-self.width // (2 * self.scaling_factor), self.width // (2 * self.scaling_factor) + 1):
            x_text = self.font.render(str(i), True, (255, 255, 255))
            self.screen.blit(x_text, (i * self.scaling_factor + self.width // 2, self.height // 2 - 20))

        for j in range(-self.height // (2 * self.scaling_factor), self.height // (2 * self.scaling_factor) + 1):
            y_text = self.font.render(str(-j), True, (255, 255, 255))
            self.screen.blit(y_text, (self.width // 2 + 10, j * self.scaling_factor + self.height // 2 - 10))

            pygame.draw.circle(self.screen, (128, 128, 128),
                               (self.width // 2, j * self.scaling_factor + self.height // 2), 2)

    def translate_point(self, point, translation):
        return [point[0] + translation[0], point[1] + translation[1]]

    def run(self):
        initial_point = [int(input('Enter initial X coordinate: ')), int(input('Enter initial Y coordinate: '))]
        translation = [int(input('Enter X translation: ')), int(input('Enter Y translation: '))]

        # Calculate translated point
        translated_point = self.translate_point(initial_point, translation)

        # Calculate distance between initial and translated points
        distance = math.sqrt((translated_point[0] - initial_point[0]) ** 2 + (translated_point[1] - initial_point[1]) ** 2)

        self.draw_axes(initial_point, translated_point, distance)

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
    algorithm = TranslationAlgorithm()
    algorithm.run()
