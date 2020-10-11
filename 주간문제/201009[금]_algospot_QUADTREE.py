import sys

def decomp(comp_str, idx):
    if idx >= len(comp_str):
        return ""
    if comp_str[idx] == 'w':
        return 'w'
    elif comp_str[idx] == 'b':
        return 'b'
    
    idx += 1
    left_top_str = decomp(comp_str, idx)
    idx += len(left_top_str)

    right_top_str = decomp(comp_str, idx)
    idx += len(right_top_str)
    
    left_bottom_str = decomp(comp_str, idx)
    idx += len(left_bottom_str)

    right_bottom_str = decomp(comp_str, idx)
    idx += len(right_bottom_str)

    return "x" + left_bottom_str + right_bottom_str \
        + left_top_str + right_top_str
    
C = int(sys.stdin.readline())


for i in range(C):

    comp_str = str(sys.stdin.readline())
    idx = 0
    print(decomp(comp_str, idx))
    # solution_1(N, L, cost)  # 시간초과
    # solution_2(N, L, cost)  # 시간초과