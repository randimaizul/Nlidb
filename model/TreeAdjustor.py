from Queue import PriorityQueue
from .ParseTree import ParseTree
from .SyntacticEvaluator import SyntacticEvaluator

class TreeAdjuster:
    MAX_EDIT = 5

    def __init__(self):
        pass

    def find(self, tree, targetNode):
        for node in tree:
            if node.equals(targetNode):
                return node
        return None

    def swap(self, parent, child):
        childInfo = child.info
        childWord = child.word
        childPosTag = child.posTag
        child.info = parent.info
        child.word = parent.word
        child.posTag = parent.posTag
        parent.info = childInfo
        parent.word = childWord
        parent.posTag = childPosTag

    def makeSibling(self, target, child):
        children = target.getChildren()
        target.children = list()
        for anyChild in children:
            if not (anyChild == child):
                target.getChildren().append(anyChild)

                target.parent.children.append(child)
                child.parent = target.parent

    def makeChild(self, target, sibling):
        siblings = target.parent.children
        target.parent.children = list()
        for anySibling in siblings:
            if not (anySibling == sibling):
                target.parent.children.append(anySibling)

        target.children.append(sibling)
        sibling.parent = target

    def adjust(self, tree, target=None):
        if target is None:
            adjusted = list()
            if target.parent is None:
                return adjusted

            for child in target.getChildren():
                tempTree = ParseTree(tree)
                self.swap(self.find(tempTree, target), self.find(tempTree, child))
                adjusted.append(tempTree)

            for child in target.getChildren():
                tempTree = ParseTree(tree)
                self.makeSibling(self.find(tempTree, target), self.find(tempTree, child))
                adjusted.append(tempTree)

            for sibling in target.parent.getChildren():
                if (sibling == target):
                    continue
                tempTree = ParseTree(tree)
                self.makeChild(self.find(tempTree, target), self.find(tempTree, sibling))
                adjusted.append(tempTree);

            if (target.getChildren().size() >= 2):
                children = target.getChildren()
                for i in range(1, children.size()):
                    tempTree = ParseTree(tree)
                    self.swap(self.find(tempTree, children[0]),
                              self.find(tempTree, children[i]));
                    adjusted.append(tempTree);

            return adjusted
        else:
            treeList = list()
            for node in tree:
                treeList.extend(self.adjust(tree, node))
            return list(treeList)


    def  getAdjustedTrees(self, tree):
        results = list()
        queue = PriorityQueue()
        #TODO :check if p queue is working properly
        H = dict()
        queue.put(tree)
        results.append(tree);
        H[tree.hashCode()] = tree
        tree.setEdit(0);

        treeWithON = tree.addON()
        queue.put(treeWithON);
        results.append(treeWithON);
        H[treeWithON.hashCode()]  = treeWithON
        treeWithON.setEdit(0)

        while not queue.empty():
            oriTree = queue.get()
            queue.put(oriTree)

            if (oriTree.getEdit() >= self.MAX_EDIT):
                continue

            treeList = self.adjust(oriTree)

            tmp = SyntacticEvaluator()

            numInvalidNodes = SyntacticEvaluator.numberOfInvalidNodes(oriTree)

            for i in range(0,len(treeList)):
                currentTree = treeList[i]
                hashValue = currentTree.hashCode()
                if not(H.has_key(hashValue) ):
                    H[hashValue] =  currentTree
                    currentTree.setEdit(oriTree.getEdit() + 1);
                    if SyntacticEvaluator.numberOfInvalidNodes(currentTree) <= numInvalidNodes:
                        queue.put(currentTree);
                        results.append(currentTree);


        return results





