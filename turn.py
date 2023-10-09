class Turns:
    def __init__(self):
        self.POWER_PER_TURN = 5
        self.directions = ["N", "E", "S", "W"]

    def get_optimal_turns(self, dir, dir_des_x = None, dir_des_y = None):
        turns = 0

        if dir_des_x is None or dir_des_y is None:
            turn += 0
        
        index_of_curr_dir = self.directions.index(dir)

        index_of_x_dir = -1
        index_of_y_dir = -1

        x_relative_dir = -1
        y_relative_dir = -1

        if dir_des_x is not None: 
            index_of_x_dir = self.directions.index(dir_des_x)
            x_relative_dir = abs(index_of_x_dir - index_of_curr_dir) % 3
            
        if dir_des_y is not None:
            index_of_y_dir = self.directions.index(dir_des_y)
            y_relative_dir = abs(index_of_y_dir - index_of_curr_dir) % 3

        return min(x_relative_dir, y_relative_dir)
        
    