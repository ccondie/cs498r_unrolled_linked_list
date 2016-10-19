from list.unrolled_linked_list.module import UnrolledLinkedList


def main():
    l = UnrolledLinkedList()
    l.max_node_capacity = 4

    for i in range(0, 8):
        l.append(i)

    l[3] = 4
    l[0] = 100
    l[7] = 13
    print(str(l))


if __name__ == '__main__':
    main()