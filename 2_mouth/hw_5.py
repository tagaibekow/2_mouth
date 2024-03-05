import random

MAZE_WIDTH = 10
MAZE_HEIGHT = 10

maze = [[0] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
maze[1][1] = 1
maze[1][2] = 1
maze[1][3] = 1
maze[2][3] = 1
maze[3][3] = 1
maze[3][4] = 1
maze[3][5] = 1
maze[3][6] = 1
maze[4][6] = 1
maze[5][6] = 1

player_x = 0
player_y = 0

def draw_maze():
    for row in maze:
        for cell in row:
            if cell == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

while True:
    draw_maze()
    print("Введите направление (вверх, вниз, влево, вправо) или 'выход' для завершения игры:")
    direction = input().lower()
    
    if direction == "выход":
        print("Игра завершена.")
        break
    elif direction == "вверх" and player_y > 0 and maze[player_y - 1][player_x] == 0:
        player_y -= 1
    elif direction == "вниз" and player_y < MAZE_HEIGHT - 1 and maze[player_y + 1][player_x] == 0:
        player_y += 1
    elif direction == "влево" and player_x > 0 and maze[player_y][player_x - 1] == 0:
        player_x -= 1
    elif direction == "вправо" and player_x < MAZE_WIDTH - 1 and maze[player_y][player_x + 1] == 0:
        player_x += 1
    else:
        print("Вы не можете двигаться в этом направлении.")

    if player_x == MAZE_WIDTH - 1 and player_y == MAZE_HEIGHT - 1:
        print("Поздравляем! Вы достигли выхода!")
        break
