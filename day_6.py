class Guard:
    dir_to_vec = {
        '^': [-1, 0],
        '>': [0, 1],
        'v': [1, 0],
        '<': [0, -1]
    }

    def __init__(self, start_x, start_y, start_dir):
        self.x = start_x
        self.y = start_y
        self.dir = start_dir
        self.positions_visited = 1
        self.is_off_map = False

    def patrol_map(self, map):
        while True:
            self.move(map)
            if self.is_off_map:
                break
    
    def move(self, map):
        y_dir, x_dir = self.dir_to_vec[self.dir]
        new_x = self.x + x_dir
        new_y = self.y + y_dir
        if new_x < 0 or new_y < 0:
            self.is_off_map = True 
            return

        try: 
            new_pos = map[new_y][new_x]
        except IndexError: 
            self.is_off_map = True 
            return
        
        if new_pos == '.' or new_pos == 'X':
            map[self.y][self.x] = 'X'
            map[new_y][new_x] = self.dir
            self.x += x_dir 
            self.y += y_dir
            if new_pos == '.':
                self.positions_visited += 1
        elif new_pos == '#':
            self.rotate_clockwise()

    def rotate_clockwise(self):
        temp = list(self.dir_to_vec) 
        try: 
            new_dir = temp[temp.index(self.dir) + 1] 
        except IndexError: 
            new_dir = '^'
        self.dir = new_dir

def parse_input():
    map = []
    guard = None

    with open('day_6_in.txt') as f:
        for y, row in enumerate(f):
            row = row.strip()
            map_row = []
            for x, col in enumerate(list(row)):
                map_row.append(col)
                if col != '.' and col != '#':
                    guard = Guard(x, y, col)
            map.append(map_row)
                
    return map, guard

def write_out(map):
    with open('day_6_out.txt', 'w+') as f:
        for row in map:
            for col in row:
                f.write(col)
            f.write('\n')

if __name__ == '__main__':
    map, guard = parse_input()
    guard.patrol_map(map)
    print(guard.positions_visited)
    write_out(map)