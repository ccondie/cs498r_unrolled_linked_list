from list.unrolled_linked_list.module import UnrolledLinkedList


def main():
    l = UnrolledLinkedList()
    l.max_node_capacity = 4

    for i in range(1, 9):
        l.append(i)

    for i in range(0, l.length):
        del l[0]
        print(str(l))

if __name__ == '__main__':
    main()