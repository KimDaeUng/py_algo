# 21:04-21:18

# My Solution
n = input()

dic = {v:k+1 for k, v in enumerate("abcdefgh")}

#     DL, DR, RD, RU, UR, UL, LU, LR 
dy = [ 2,  2,  1, -1, -2, -2, -1,  1]
dx = [-1,  1,  2,  2,  1, -1, -2, -2] 


start_y = int(n[1])
start_x = dic[n[0]]
count = 0
for i in range(8):
    ny, nx = start_y + dy[i], start_x + dx[i]
    if ny > 8 or ny < 1 or nx > 8 or nx < 1:
        continue
    count += 1

print(count)

# Solution

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# define the Moving directions
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# Check whether it can move to each directions
result = 0
for step in steps:
    # Check the position we want to move
    next_row = row + step[0]
    next_col = col + step[1]
    
    # If we can move then, add 1 to result variable
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)