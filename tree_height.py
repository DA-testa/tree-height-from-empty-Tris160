# python3

import sys
import threading
5
def compute_height(n, parents):

    tree = {}
    rootIndex = 0
    for k in range(n):
        tree[k]=[]
    for k, par in enumerate(parents):
        par = parents[k]
        if par != -1:
           tree[par].append(k)
        else:
            rootIndex = k
    findBranch = [(rootIndex,1)]
    max_height = 0
    while findBranch:
        node, height = findBranch.pop()
        max_height = max(max_height,height)
        element = tree[node]
        if element:
            for ch in element:
                findBranch.append((ch, height+1))
        else:
            if height>max_height:
                max_height=height
    return max_height
def main():
    letter = input()
    if "F" in letter:
        fileName = input()
        if "a" in fileName:
            return
        with open(f"./test/{fileName}", mode="r") as file:
            number = int(file.readline())
            values = list(map(int, file.readline().split())) 
    if "I" in letter:
        number = int(input())
        values = list(map(int, input().split()))
    print(compute_height(number, values))

