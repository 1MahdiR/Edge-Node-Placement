import networkx as nx
from random import randint, random

from component.fog import Fog
from component.network import Network
from component.node import Node
from config.base_station import *


def main():
    x = 4
    y = 4
    z = 4

    t = 1
    for i in range(1, x+1):
        for j in range(1, y+1):
            n = Node(t, i, j, randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 4),
                     random() > 0.5, randint(1, 3), randint(1, 3), randint(1, 3))
            t += 1

    t = 1
    for i in range(1, z+1):
        n = Fog(t, random() > 0.5, randint(4, 6))
        t += 1

    n = Network(Node.NODES, Fog.FOG_NODES)

    n.draw_graph()


if __name__ == '__main__':
    main()
