
from wiki_helper import WikiHelper
import json
from node import Node
import random
from tree import Tree
from csvgen import CsvGen


def main(wikip_helper):
    TREE_BRANCH_NUMBER = 2
    TREE_BRANCH_LENGTH = 10
    inputstr = input()
    root = Node(inputstr)
    curNode = root
    for ind in range(TREE_BRANCH_NUMBER):
        DATA = wikip_helper.get_url(inputstr)
        curNode = root
        for ind2 in range(TREE_BRANCH_LENGTH):
            if(len(list(DATA.links.keys())) == 0):
                break
            else:
                rand = random.randint(0, len(list(DATA.links.keys()))-1)
                link = list(DATA.links.keys())[rand]
                curNode.addChild(Node(link))
                curNode = curNode.children[len(curNode.children)-1]
                DATA = wikip_helper.get_url(link)
    #treeGraph = Tree(root)
    #treeGraph.generate_tree(TREE_BRANCH_NUMBER*200, TREE_BRANCH_LENGTH*70)
    print("Create a new CSV file? Y/N")
    inputstr = input()
    csv = CsvGen(root)
    if inputstr.lower().startswith("y"):
        csv.makecsv(TREE_BRANCH_LENGTH)
    else:
        csv.appendcsv(TREE_BRANCH_LENGTH)


if __name__ == "__main__":
    main(WikiHelper())
