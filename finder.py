import os

def clear():
    os.system("cls")
maze = [
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]]
    
total_col = len(maze[0])
total_row = len(maze)
def check_index(row,col):
    if row >= 0 and row <= (total_row - 1) and col >= 0 and col <= (total_col - 1):
        return True
    else:
        return False

def print_maze(maze):
    for row in maze:
        for col in row:
            if col == 1:
                print("[-]",end = "")
            elif col == 3:
                print(" * ",end = "")
            elif col == 2:
                print(" o ",end = "")
            else:
                print("   ",end = "")
        print("\n")
boundary = []
if maze[total_row - 1][total_col - 1] == 0 and maze[0][0] == 0:
    boundary.append({"row":0,"col":0})
    #print(boundary)
    while True:
        new_boundary = []
        for point in boundary:
            clear()
            print_maze(maze)
            if check_index(point["row"],point["col"] + 1) and maze[point["row"]][point["col"] + 1] == 0:
                if {"row": point["row"],"col": point["col"] + 1} not in boundary and {"row": point["row"],"col": point["col"] + 1} not in new_boundary:
                    maze[point["row"]][point["col"]] = 2
                    maze[point["row"]][point["col"] + 1] = 3
                    new_boundary.append({"row": point["row"],"col": point["col"] + 1})
            
            if check_index(point["row"] + 1,point["col"]) and maze[point["row"] + 1][point["col"]] == 0:
                if {"row": point["row"] + 1,"col": point["col"]} not in boundary and {"row": point["row"] + 1,"col": point["col"]} not in new_boundary:
                    maze[point["row"]][point["col"]] = 2
                    maze[point["row"] + 1][point["col"]] = 3
                    new_boundary.append({"row": point["row"] + 1,"col": point["col"]})
            
            if check_index(point["row"],point["col"] - 1) and maze[point["row"]][point["col"] - 1] == 0:
                if {"row": point["row"],"col": point["col"] - 1} not in boundary and {"row": point["row"],"col": point["col"] - 1} not in new_boundary:
                    maze[point["row"]][point["col"]] = 2
                    maze[point["row"]][point["col"] - 1] = 3
                    new_boundary.append({"row": point["row"],"col": point["col"] - 1})
            
            if check_index(point["row"] - 1,point["col"]) and maze[point["row"] - 1][point["col"]] == 0:
                if {"row": point["row"] - 1,"col": point["col"]} not in boundary and {"row": point["row"] - 1,"col": point["col"]} not in new_boundary:
                    maze[point["row"]][point["col"]] = 2
                    maze[point["row"] - 1][point["col"]] = 3
                    new_boundary.append({"row": point["row"] - 1,"col": point["col"]})
        if new_boundary == boundary:
            print("NO")
            break
        elif {"row":total_row - 1,"col":total_col - 1} in new_boundary:
            print("YES")
            break
        else:
            #print(new_boundary)
            boundary = new_boundary
else:
    print("NO")