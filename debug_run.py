from list.unrolled_linked_list.module import UnrolledLinkedList


def main():
    l = UnrolledLinkedList()
    l.max_node_capacity = 4

    for i in range(0, 8):
        l.append(i)

    if -1 in l:
        print("true")
    else:
        print("false")


if __name__ == '__main__':
    main()
