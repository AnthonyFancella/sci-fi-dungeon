import random

class Level:
    def __init__(self, level):
        self.level = level
        self.num_rooms = 1
        self.req_rooms = int(random.uniform(0, 1) + 5 + level * 2.6)
        self.rooms = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                      
    def build(self):
        while self.num_rooms < self.req_rooms:
            for i in range(len(self.rooms)):
                for j in range(len(self.rooms[i])):
                    try:
                        if self.rooms[i][j] == 1:
                            if self.rooms[i - 1][j] == 1:
                                pass
                            else:
                                c = (i - 1, j)
                                counter = 0
                                for k in range(4):
                                    if self.rooms[c[0] - 1][c[1]] == 1:
                                        counter += 1
                                    if self.rooms[c[0]][c[1] - 1] == 1:
                                        counter += 1
                                    if self.rooms[c[0]][c[1] + 1] == 1:
                                        counter += 1
                                if counter > 2:
                                    pass
                                else:
                                    if self.num_rooms == self.req_rooms:
                                        pass
                                    else:
                                        if random.randint(0, 100) > 50:
                                            pass
                                        else:
                                            self.rooms[i - 1][j] = 1
                                            self.num_rooms += 1
                            if self.rooms[i + 1][j] == 1:
                                pass
                            else:
                                c = (i + 1, j)
                                counter = 0
                                for k in range(4):
                                    if self.rooms[c[0] + 1][c[1]] == 1:
                                        counter += 1
                                    if self.rooms[c[0]][c[1] - 1] == 1:
                                        counter += 1
                                    if self.rooms[c[0]][c[1] + 1] == 1:
                                        counter += 1
                                if counter > 2:
                                    pass
                                else:
                                    if self.num_rooms == self.req_rooms:
                                        pass
                                    else:
                                        if random.randint(0, 100) > 50:
                                            pass
                                        else:
                                            self.rooms[i + 1][j] = 1
                                            self.num_rooms += 1
                            if self.rooms[i][j - 1] == 1:
                                pass
                            else:
                                c = (i, j - 1)
                                counter = 0
                                for k in range(4):
                                    if self.rooms[c[0] - 1][c[1]] == 1:
                                        counter += 1
                                    if self.rooms[c[0]][c[1] - 1] == 1:
                                        counter += 1
                                    if self.rooms[c[0 + 1]][c[1]] == 1:
                                        counter += 1
                                if counter > 2:
                                    pass
                                else:
                                    if self.num_rooms == self.req_rooms:
                                        pass
                                    else:
                                        if random.randint(0, 100) > 50:
                                            pass
                                        else:
                                            self.rooms[i][j - 1] = 1
                                            self.num_rooms += 1
                            if self.rooms[i][j + 1] == 1:
                                pass
                            else:
                                c = (i, j + 1)
                                counter = 0
                                for k in range(4):
                                    if self.rooms[c[0] - 1][c[1]] == 1:
                                        counter += 1
                                    if self.rooms[c[0] + 1][c[1]] == 1:
                                        counter += 1
                                    if self.rooms[c[0]][c[1] + 1] == 1:
                                        counter += 1
                                if counter > 2:
                                    pass
                                else:
                                    if self.num_rooms == self.req_rooms:
                                        pass
                                    else:
                                        if random.randint(0, 100) > 50:
                                            pass
                                        else:
                                            self.rooms[i][j + 1] = 1
                                            self.num_rooms += 1
                    except:
                        pass
                        