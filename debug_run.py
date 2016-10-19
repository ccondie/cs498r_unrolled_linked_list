from list.unrolled_linked_list.module import UnrolledLinkedList


def main():
    l = UnrolledLinkedList()
    l.max_node_capacity = 4

    for i in range(0, 8):
        l.append(i)

    for el in reversed(l):
        print(el)

if __name__ == '__main__':
    main()
