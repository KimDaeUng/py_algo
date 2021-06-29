# https://programmers.co.kr/learn/courses/30/lessons/72410
# 01:50-02:28

# My Solution 1
def solution(new_id):
    new_id = list(new_id)
    to_keep = set(['-', '_', '.'])
    stack = []

    for i in range(len(new_id)):
        # step 1
        if new_id[i].isalpha():
            new_id[i] = new_id[i].lower()
        # step 2
        if not(new_id[i].islower() or new_id[i].isdigit() or \
           new_id[i] in to_keep):
            continue
        # step 3
        if len(stack) > 1:
            if stack[-2] == '.' and stack[-1] == '.':
                del stack[-1]
        stack.append(new_id[i])
    
    new_id = ''.join(stack)

    # step 4
    while new_id.startswith('.') or new_id.endswith('.'):
        if new_id.startswith('.'):
            new_id = new_id[1:]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
        
    # step 5    
    if len(new_id) == 0:
        new_id = 'a'

    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id.endswith('.'):
            new_id = new_id[:-1]

    # step 7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
        
    return new_id


# Solution: Regular Expression

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + ''.join([st[-1] for i in range(3 - len(st))])
    return st