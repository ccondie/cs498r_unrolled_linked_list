class UnrolledLinkedList():
    """This is the class name you should use. You should also have a
    max_node_capacity. Also, you should remove this comment and possibly
    replace it with your own
    """

    def __init__(self, max_node_capacity=16):
        self.max_node_capacity = max_node_capacity
        self.nodeList = []
        self.length = 0

    def __delitem__(self, index):
        # check for index out of bounds
        if abs(index) > self.length:
            raise IndexError
        else:
            # resolve negative indexes to function as positive indexes
            if index < 0:
                index += self.length

            nodeIndex = 0
            while True:
                # if the index is within the current node
                if index < len(self.nodeList[nodeIndex]):
                    self.length -= 1
                    del self.nodeList[nodeIndex][index]
                    break
                else:
                    index += len(self.nodeList[nodeIndex])
                    nodeIndex += 1

    def __getitem__(self, index):
        # check for index out of bounds
        if abs(index) > self.length:
            raise IndexError
        else:
            # resolve negative indexes to function as positive indexes
            if index < 0:
                index += self.length

            nodeIndex = 0
            while True:
                # if the index is within the current node
                if index < len(self.nodeList[nodeIndex]):
                    return self.nodeList[nodeIndex][index]
                else:
                    index += len(self.nodeList[nodeIndex])
                    nodeIndex += 1

    def __setitem__(self, key, value):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        return_me = []
        for node in self.nodeList:
            return_me.append(str(node))
            return_me.append('\n')
        return ''.join(return_me)

    def __len__(self):
        return self.length

    def __reversed__(self):
        pass

    def __contains__(self, obj):
        pass

    def append(self, data):
        # get the final node in the nodeList
        if len(self.nodeList) == 0:
            self.nodeList.append([])

        self.nodeList[len(self.nodeList) - 1].append(data)
        self.length += 1
