# print('''|\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\__|''')

string = '''5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

tc = int(input())

for _ in range(tc):
    st = input()
    cnt = 0
    total = 0
    for i in st:
        if i == 'X':
            cnt = 0
        elif i == 'O':
            cnt += 1
            total += cnt
    print(total)