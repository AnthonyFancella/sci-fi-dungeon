import random

rooms = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

level = 1

num_rooms = 1
req_rooms = int(random.uniform(0, 1) + 5 + level * 2.6)
while num_rooms < req_rooms:
    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            try:
                if rooms[i][j] == 1:
                    if rooms[i - 1][j] == 1:
                        pass
                    else:
                        c = (i - 1, j)
                        counter = 0
                        for k in range(4):
                            if rooms[c[0] - 1][c[1]] == 1:
                                counter += 1
                            if rooms[c[0]][c[1] - 1] == 1:
                                counter += 1
                            if rooms[c[0]][c[1] + 1] == 1:
                                counter += 1
                        if counter > 2:
                            pass
                        else:
                            if num_rooms == req_rooms:
                                pass
                            else:
                                if random.randint(0, 100) > 50:
                                    pass
                                else:
                                    rooms[i - 1][j] = 1
                                    num_rooms += 1
                    if rooms[i + 1][j] == 1:
                        pass
                    else:
                        c = (i + 1, j)
                        counter = 0
                        for k in range(4):
                            if rooms[c[0] + 1][c[1]] == 1:
                                counter += 1
                            if rooms[c[0]][c[1] - 1] == 1:
                                counter += 1
                            if rooms[c[0]][c[1] + 1] == 1:
                                counter += 1
                        if counter > 2:
                            pass
                        else:
                            if num_rooms == req_rooms:
                                pass
                            else:
                                if random.randint(0, 100) > 50:
                                    pass
                                else:
                                    rooms[i + 1][j] = 1
                                    num_rooms += 1
                    if rooms[i][j - 1] == 1:
                        pass
                    else:
                        c = (i, j - 1)
                        counter = 0
                        for k in range(4):
                            if rooms[c[0] - 1][c[1]] == 1:
                                counter += 1
                            if rooms[c[0]][c[1] - 1] == 1:
                                counter += 1
                            if rooms[c[0 + 1]][c[1]] == 1:
                                counter += 1
                        if counter > 2:
                            pass
                        else:
                            if num_rooms == req_rooms:
                                pass
                            else:
                                if random.randint(0, 100) > 50:
                                    pass
                                else:
                                    rooms[i][j - 1] = 1
                                    num_rooms += 1
                    if rooms[i][j + 1] == 1:
                        pass
                    else:
                        c = (i, j + 1)
                        counter = 0
                        for k in range(4):
                            if rooms[c[0] - 1][c[1]] == 1:
                                counter += 1
                            if rooms[c[0] + 1][c[1]] == 1:
                                counter += 1
                            if rooms[c[0]][c[1] + 1] == 1:
                                counter += 1
                        if counter > 2:
                            pass
                        else:
                            if num_rooms == req_rooms:
                                pass
                            else:
                                if random.randint(0, 100) > 50:
                                    pass
                                else:
                                    rooms[i][j + 1] = 1
                                    num_rooms += 1
            except:
                pass

print(num_rooms)
for row in rooms:
    print(''.join(['#' if cell == 1 else ' ' for cell in row]))
            