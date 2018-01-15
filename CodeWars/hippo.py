def maze_runner(maze, directions):
    rows = len(maze)

    for index in range(rows):
        if 2 in maze[index]:
            row = index
            col = maze[row].index(2)
            break

    for pos in directions:
        if pos == "N": row -= 1
        elif pos == "S": row += 1
        elif pos == "E": col += 1
        elif pos == "W": col -= 1

        if row < 0 or col < 0 or row == rows or col == rows or maze[row][col] == 1:
            return "Dead"
        elif maze[row][col] == 3:
            return "Finish"

    return "Lost"
maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

directions = ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]
print('F', maze_runner(maze, directions))
directions = ["N", "N", "N", "W", "W"]
print('D', maze_runner(maze, directions))
directions = ["N","E","E","E","E"]


#codewars
directions
print('DD', maze_runner([[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 3, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 2, 0],
                        [0, 0, 0, 0, 0, 0]]
                        , ['S', 'E', 'N', 'S', 'W', 'N', 'S',
                        'S', 'S', 'E', 'E', 'E', 'N', 'E', 'E', 'E', 'W',
                        'N', 'W', 'E', 'E', 'N', 'W', 'W', 'E', 'W', 'W', 'S',
                        'E', 'N', 'W', 'S']))