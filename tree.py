import igraph as ig
from igraph import Graph, EdgeSeq
import plotly.graph_objects as go
import node


class Tree(object):
    def __init__(self, head_node):
        self.head = head_node
        self.g = Graph()

    def num_of_nodes(self):
        if not self.non_empty():
            return -1
        count = 1
        for x in self.head.children:
            curNode = x
            while len(curNode.children) != 0:
                if len(curNode.data) > 0:
                    count += 1
                curNode = curNode.children[0]
            count += 1
        return count

    def print_node_data(self):
        if not self.non_empty():
            return -1
        for x in self.head.children:
            curNode = x
            while len(curNode.children) != 0:
                print(curNode.data)
                curNode = curNode.children[0]
            print(curNode.data)

    def non_empty(self):
        if len(self.head.children) == 0:
            return 0
        else:
            return 1

    def generate_tree(self, dim1, dim2):
        if not self.non_empty():
            return -1
        self.g.add_vertices(self.num_of_nodes())
        curInd = 1
        for x in self.head.children:
            curNode = x
            self.g.add_edge(0, curInd)
            while len(curNode.children) != 0:
                self.g.add_edge(curInd, curInd+1)
                curNode = curNode.children[0]
                curInd += 1
            curInd += 1
        curInd = 1
        self.g.vs[0]["name"] = self.head.data
        for x in self.head.children:
            curNode = x
            while len(curNode.children) != 0:
                if curNode.data.startswith("Category"):
                    curNode.data = curNode.data[9:len(curNode.data)]
                self.len_check(curNode, curInd)
                curNode = curNode.children[0]
                curInd += 1
            self.len_check(curNode, curInd)
            curInd += 1
        layout = self.g.layout_reingold_tilford(mode="in", root=[0])
        self.g.vs["label"] = self.g.vs["name"]
        ig.plot(self.g, layout=layout, bbox=(dim1, dim2), margin=70)

    def len_check(self, curNode, curInd):
        if len(curNode.data) > 15:
            self.g.vs[curInd]["name"] = curNode.data[0:15]+"..."
        else:
            self.g.vs[curInd]["name"] = curNode.data
