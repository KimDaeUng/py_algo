# https://www.acmicpc.net/problem/11720
import sys
input = sys.stdin.readline
n = int(input())
print(sum(map(int, list(input().rstrip()))))