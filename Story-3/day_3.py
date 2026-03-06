from aoc import *
from dataclasses import dataclass
from typing import Optional



@dataclass
class Node:
    id: int
    plug: str
    plugbond: int
    leftsocket: str
    rightsocket: str
    left: Optional["Node"]
    right: Optional["Node"]
    data: str

def parse_line(line):
    parts = line.split(", ")
    id = int(parts[0].split("=")[1])
    plug = parts[1].split("=")[1]
    leftsocket = parts[2].split("=")[1]
    rightsocket = parts[3].split("=")[1]
    data = parts[4].split("=")[1]
    return Node(id, plug, 0, leftsocket, rightsocket, None, None, data)


def find_plug_1(node, tree, plug):
    if tree.left:
        if find_plug_1(node, tree.left, plug):
            return True
    elif tree.leftsocket == plug:
        tree.left = node
        return True
    if tree.right:
        if find_plug_1(node, tree.right, plug):
            return True
    elif tree.rightsocket == plug:
        tree.right = node
        return True
    return False


def find_plug_2(node, tree, plug):
    if tree.left:
        if find_plug_2(node, tree.left, plug):
            return True
    elif weak_bond(tree.leftsocket, plug):
        tree.left = node
        return True
    if tree.right:
        if find_plug_2(node, tree.right, plug):
            return True
    elif weak_bond(tree.rightsocket, plug):
        tree.right = node
        return True
    return False


def find_plug_3(node, tree, plug):
    if tree.left:
        if tree.left.plugbond < weak_bond(tree.leftsocket, plug):
            newnode = tree.left
            tree.left = node
            node.plugbond = weak_bond(tree.leftsocket, plug)
            node = newnode
            plug = node.plug
        elif nn := find_plug_3(node, tree.left, plug):
            node = nn
            plug = node.plug
        else:
            return None
    elif weak_bond(tree.leftsocket, plug):
        tree.left = node
        tree.left.plugbond = weak_bond(tree.leftsocket, plug)
        return None
    if tree.right:
        if tree.right.plugbond < weak_bond(tree.rightsocket, plug):
            newnode = tree.right
            tree.right = node
            node.plugbond = weak_bond(tree.rightsocket, plug)
            node = newnode
            plug = node.plug
        elif nn := find_plug_3(node, tree.right, plug):
            node = nn
            plug = node.plug
        else:
            return None
    elif weak_bond(tree.rightsocket, plug):
        tree.right = node
        tree.right.plugbond = weak_bond(tree.rightsocket, plug)
        return None
    return node


@functools.cache
def weak_bond(plug1, plug2):
    c1, s1 = plug1.split()
    c2, s2 = plug2.split()
    return (c1 == c2) + (s1 == s2)


checked = 0
total = 0
def dfs(node):
    global checked, total
    if node.left:
        dfs(node.left)
    checked += 1
    total += checked * node.id
    if node.right:
        dfs(node.right)


def part_1(data):
    tree = parse_line(data.splitlines()[0])
    nodes = [parse_line(line) for line in data.splitlines()[1:]]

    while nodes:
        node = nodes.pop(0)
        success = find_plug_1(node, tree, node.plug)
        if not success:
            nodes.insert(0, node)

    dfs(tree)
    print(total)


def part_2(data):
    tree = parse_line(data.splitlines()[0])
    nodes = [parse_line(line) for line in data.splitlines()[1:]]

    while nodes:
        node = nodes.pop(0)
        success = find_plug_2(node, tree, node.plug)
        if not success:
            nodes.insert(0, node)

    dfs(tree)
    print(total)


def part_3(data):
    tree = parse_line(data.splitlines()[0])
    nodes = [parse_line(line) for line in data.splitlines()[1:]]

    while nodes:
        node = nodes.pop(0)
        returned_node = find_plug_3(node, tree, node.plug)
        if returned_node:
            nodes.insert(0, returned_node)

    dfs(tree)
    print(total)
    

"""feeding in node.plug seperately into the function was stupid"""


if __name__ == "__main__":
    data = import_input(3)
    # part_1(data)
    # part_2(data)
    # part_3(data)
