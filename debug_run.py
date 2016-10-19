from list.unrolled_linked_list.module import UnrolledLinkedList


def main():
    l = UnrolledLinkedList()
    l.append(4)
    l.append(5)
    l.append(7)
    l.append(8)
    l.append(14)
    l.append(17)

    print(l[-6])
    print(str(l))

if __name__ == '__main__':
    main()