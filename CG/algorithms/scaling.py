import pygame
import sys

class ScalingAlgorithm:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2D Scaling")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 20)
        self.scaling_factor = 20  # Increase the scaling factor for more spacing

    def draw_axes(self, initial_points, scaled_points, scaling_factors):
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.height // 2), (self.width, self.height // 2))
        pygame.draw.line(self.screen, (255, 255, 255), (self.width // 2, 0), (self.width // 2, self.height))

        font = pygame.font.Font(None, 36)
        text_x = font.render('X', True, (255, 255, 255))
        text_y = font.render('Y', True, (255, 255, 255))
        self.screen.blit(text_x, (self.width - 30, self.height // 2 - 30))
        self.screen.blit(text_y, (self.width // 2 + 10, 10))

        # Draw the initial points
        self.draw_point(initial_points[0], (0, 255, 0), 'Initial Point 1')
        self.draw_point(initial_points[1], (0, 255, 0), 'Initial Point 2')

        # Draw line connecting initial points
        pygame.draw.line(self.screen, (0, 255, 0),
                         (initial_points[0][0] * self.scaling_factor + self.width // 2,
                          self.height // 2 - initial_points[0][1] * self.scaling_factor),
                         (initial_points[1][0] * self.scaling_factor + self.width // 2,
                          self.height // 2 - initial_points[1][1] * self.scaling_factor), 2)

        # Draw the scaled points
        self.draw_point(scaled_points[0], (255, 0, 0), 'Scaled Point 1')
        self.draw_point(scaled_points[1], (255, 0, 0), 'Scaled Point 2')

        # Draw line connecting scaled points
        pygame.draw.line(self.screen, (255, 0, 0),
                         (scaled_points[0][0] * self.scaling_factor + self.width // 2,
                          self.height // 2 - scaled_points[0][1] * self.scaling_factor),
                         (scaled_points[1][0] * self.scaling_factor + self.width // 2,
                          self.height // 2 - scaled_points[1][1] * self.scaling_factor), 2)

        # Display scaling factors
        scaling_label = self.font.render(f'Scaling Factors: Sx={scaling_factors[0]}, Sy={scaling_factors[1]}', True, (255, 255, 255))
        self.screen.blit(scaling_label, (self.width // 2 - 200, self.height // 2 - 30))

        # Draw the coordinate points and their labels
        self.draw_coordinate_points()

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

    def scale_point(self, point, scaling_factors):
        return [point[0] * scaling_factors[0], point[1] * scaling_factors[1]]

    def run(self):
        x1 = int(input('Enter initial X coordinate for Point 1: '))
        y1 = int(input('Enter initial Y coordinate for Point 1: '))
        x2 = int(input('Enter initial X coordinate for Point 2: '))
        y2 = int(input('Enter initial Y coordinate for Point 2: '))
        sx = float(input('Enter scaling factor Sx: '))
        sy = float(input('Enter scaling factor Sy: '))

        initial_points = [[x1, y1], [x2, y2]]
        scaling_factors = [sx, sy]

        # Calculate scaled points
        scaled_points = [self.scale_point(initial_points[0], scaling_factors),
                         self.scale_point(initial_points[1], scaling_factors)]

        self.draw_axes(initial_points, scaled_points, scaling_factors)

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
    algorithm = ScalingAlgorithm()
    algorithm.run()
