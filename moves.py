class Moves: 
    def __init__(self):
        self.POWER_PER_MOVE = 10

    def get_power_spent(self, relative_dx, relative_dy):
        return self.POWER_PER_MOVE * (abs(relative_dx) + abs(relative_dy))