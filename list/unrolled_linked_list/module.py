from math import floor
from math import ceil


class UnrolledLinkedList():
    def __init__(self, max_node_capacity=16):
        self.max_node_capacity = max_node_capacity
        self.nodeList = []
        self.length = 0

    def __delitem__(self, index):
        # check for index out of bounds
        if abs(index) > self.length:
            raise IndexError

        # resolve negative indexes to function as positive indexes
        if index < 0:
            index += self.length

        nodeIndex = 0
        while True:
            if index < len(self.nodeList[nodeIndex]):
                # if the index is within the current node
                del self.nodeList[nodeIndex][index]
                self.length -= 1

                # check if the node slipped below max/2
                if len(self.nodeList[nodeIndex]) <= floor(self.max_node_capacity / 2):
                    # balance nodes
                    if nodeIndex == len(self.nodeList) - 1:
                        # if the node is at the end of the nodeList, stop
                        # if the node is now empty, delete it
                        if len(self.nodeList[nodeIndex]) == 0:
                            del self.nodeList[nodeIndex]
                        break
                    while nodeIndex < len(self.nodeList) - 1:
                        # for every node up until the last node
                        while len(self.nodeList[nodeIndex]) <= floor(self.max_node_capacity / 2):
                            # pull elements from the next node one at a time
                            dummy = self.nodeList[nodeIndex + 1][0]
                            del self.nodeList[nodeIndex + 1][0]
                            if len(self.nodeList[nodeIndex + 1]) == 0:
                                del self.nodeList[nodeIndex + 1]
                            self.nodeList[nodeIndex].append(dummy)
                        nodeIndex += 1
                break
            else:
                index -= len(self.nodeList[nodeIndex])
                nodeIndex += 1

    def __getitem__(self, index):
        # check for index out of bounds
        if abs(index) > self.length:
            raise IndexError

        # resolve negative indexes to function as positive indexes
        if index < 0:
            index += self.length

        nodeIndex = 0
        while True:
            # if the index is within the current node
            if index < len(self.nodeList[nodeIndex]):
                return self.nodeList[nodeIndex][index]
            else:
                index -= len(self.nodeList[nodeIndex])
                nodeIndex += 1

    def __setitem__(self, key, value):
        if key > self.length:
            raise IndexError

        if key < 0:
            key += self.length

        nodeIndex = 0
        while True:
            if key < len(self.nodeList[nodeIndex]):
                self.nodeList[nodeIndex][key] = value
                break
            else:
                key -= len(self.nodeList[nodeIndex])
                nodeIndex += 1

    def __iter__(self):
        count = 0
        local_count = 0
        nodeIndex = 0
        while count < self.length:
            yield self.nodeList[nodeIndex][local_count]
            local_count += 1
            count += 1
            if local_count == len(self.nodeList[nodeIndex]):
                local_count = 0
                nodeIndex += 1

    def __str__(self):
        return_me = []
        return_me.append('{')
        for i in range(0, len(self.nodeList)):
            return_me.append(str(self.nodeList[i]))
            if i != len(self.nodeList) - 1:
                return_me.append(', ')
        return_me.append('}')
        return ''.join(return_me)

    def __len__(self):
        return self.length

    def __reversed__(self):
        count = 0
        nodeIndex = len(self.nodeList) - 1
        local_count = len(self.nodeList[nodeIndex]) - 1
        while count < self.length:
            yield self.nodeList[nodeIndex][local_count]
            local_count -= 1
            count += 1
            if local_count == -1:
                nodeIndex -= 1
                local_count = len(self.nodeList[nodeIndex]) - 1

    def __contains__(self, obj):
        count = 0
        local_count = 0
        nodeIndex = 0
        while count < self.length:
            if self.nodeList[nodeIndex][local_count] == obj:
                return True
            local_count += 1
            count += 1
            if local_count == len(self.nodeList[nodeIndex]):
                local_count = 0
                nodeIndex += 1
        return False

    def append(self, data):
        # get the final node in the nodeList
        if len(self.nodeList) == 0:
            self.nodeList.append([])

        endIndex = len(self.nodeList) - 1
        endLength = len(self.nodeList[endIndex])

        if endLength < self.max_node_capacity:
            # if the tail node is not full, add data to that node
            self.nodeList[endIndex].append(data)
            self.length += 1
        else:
            # if the tail node is full, take half of it and create a new node
            newNode = self.nodeList[endIndex][ceil(endLength / 2):endLength]
            del self.nodeList[endIndex][ceil(endLength / 2):endLength]
            self.nodeList.append(newNode)
            self.nodeList[endIndex + 1].append(data)
            self.length += 1
