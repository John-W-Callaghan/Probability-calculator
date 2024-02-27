import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents += [color] * count

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            return self.contents
        
        for _ in range(num_balls):
            drawn_ball = random.choice(self.contents)
            self.contents.remove(drawn_ball)
            drawn_balls.append(drawn_ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        
        success = True
        for color, count in expected_balls.items():
            if color not in drawn_dict or drawn_dict[color] < count:
                success = False
                break
        
        if success:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability

