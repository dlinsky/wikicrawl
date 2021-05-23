import pandas as pd
import node


class CsvGen:
    def __init__(self, head_node):
        self.head = head_node

    def makeDataFrame(self, branch_length, paths, columns):
        for x in self.head.children:
            curNode = x
            templist = ['']*(branch_length+1)
            templist[0] = self.head.data
            curInd = 1
            while len(curNode.children) != 0:
                templist[curInd] = curNode.data
                curNode = curNode.children[0]
                curInd += 1
            templist[curInd] = curNode.data
            toAppend = pd.DataFrame(
                [templist], columns=columns)
            paths = paths.append(toAppend)
        return paths

    def makecsv(self, branch_length):
        columns = self.makeCol(branch_length)
        paths = pd.DataFrame(columns=columns)
        paths = self.makeDataFrame(branch_length, paths, columns)
        paths.to_csv("paths.csv", index=0)

    def makeCol(self, branch_length):
        columns = ['']*(branch_length+1)
        for ind in range(branch_length+1):
            columns[ind] = "step " + str(ind)
        return columns

    def appendcsv(self, branch_length):
        columns = self.makeCol(branch_length)
        paths = pd.read_csv("paths.csv")
        paths = self.makeDataFrame(branch_length, paths, columns)
        paths.to_csv("paths.csv", index=0)
