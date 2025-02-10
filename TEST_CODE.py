##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def test_sequence(PDB, forw_sequ):
    h = PDB.header
    t = PDB.trailer
    try:
        walk = h
        for el in forw_sequ:
            if el != walk.value:
                return False

            walk = walk.next

        rev_sequ = forw_sequ[::-1]
        walk = t
        for el in rev_sequ:
            if el != walk.value:
                return False

            walk = walk.prev

        return True

    except:
        return False


def TEST_new_PDB(PDB, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: PDB initialization{W}\n")

    temp_node = class_ref().DoublyNode("temp")
    h = PDB.header
    t = PDB.trailer

    test = type(h) == type(temp_node)
    print(f"Header sentinel is type DoublyNode: {result(test)}")

    test = type(t) == type(temp_node)
    print(f"Trailer sentinel is type DoublyNode: {result(test)}\n")

    test = h.next == t
    print(f"Header next is Trailer: {result(test)}")

    test = t.prev == h
    print(f"Trailer prev is Header: {result(test)}\n")

    test = PDB._PositionalDoublyBase__size == 0
    print(f"Size attribute initialized to zero: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_doubly_node(class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The DoublyNode Class{W}\n")

    try:
        node1 = class_ref().DoublyNode("A")
        print(f"{B}A temporary test node was created: {node1}{W}\n")
        print(f"DoublyNode class is nested within PositionalDoublyBase: {result(True)}")
    except:
        print(f"DoublyNode class is nested within PositionalDoublyBase: {result(False)}")

    test = node1.value == "A"
    print(f"DoublyNode value is set properly: {result(test)}")

    test = node1.prev == None
    print(f"New DoublyNode prev is set to None: {result(test)}")

    test = node1.next == None
    print(f"New DoublyNode next is set to None: {result(test)}\n")

    try:
        node1.set_prev("B")
        print(f"set_prev() raises exception if prev is not type DoublyNode: {result(False)}")
    except:
        print(f"set_prev() raises exception if prev is not type DoublyNode: {result(True)}")

    node2 = class_ref().DoublyNode("B")
    node1.set_prev(node2)
    test = node1.prev == node2 and node1.prev.value == "B"
    print(f"DoublyNode set_prev updates self.prev: {result(test)}")

    test = node2.next == node2.prev == None
    print(f"DoublyNode set_prev does not change other node: {result(test)}")

    try:
        node1.set_next("B")
        print(f"\nset_next() raises exception if next is not type DoublyNode: {result(False)}")
    except:
        print(f"\nset_next() raises exception if next is not type DoublyNode: {result(True)}")

    node3 = class_ref().DoublyNode("C")
    node1.set_next(node3)
    test = node1.next == node3 and node1.next.value == "C"
    print(f"DoublyNode set_next updates self.next: {result(test)}")

    test = node3.prev == node3.next == None
    print(f"DoublyNode set_next does not change other node: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_insert_between(PDB, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: insert_between{W}\n")

    print(f"{B}The PDB is currently empty: {PDB}{W}\n")

    h = PDB.header
    t = PDB.trailer

    try:
        n1 = PDB._PositionalDoublyBase__insert_between("A")
        print(f"pred & succ parameters are optional: {result(True)}")
    except:
        print(f"pred & succ parameters are optional: {result(False)}")

    print(f"\n{B}One node was added to the PDB: {PDB}{W}\n")

    test = type(n1) == type(h)
    print(f"New node inserted is type DoublyNode: {result(test)}")

    test = n1.prev == h
    print(f"pred parameter defaults to header when no argument provided: {result(test)}")

    test = n1.next == t
    print(f"succ parameter defaults to trailer when no argument provided: {result(test)}")

    test = len(PDB) == 1
    print(f"insert_between increases size attribute: {result(test)}")

    test = test_sequence(PDB, [None, "A", None])
    print(f"Pointers are correct after insertion: {result(test)}")

    n2 = PDB._PositionalDoublyBase__insert_between("B", succ=n1)
    print(f"\n{B}A new node was added to the PDB: {PDB}{W}")

    test = test_sequence(PDB, [None, "B", "A", None])
    print(f"When only a successor is given, insert_between works like head_insert: {result(test)}")

    n3 = PDB._PositionalDoublyBase__insert_between("C", pred=n1)
    print(f"\n{B}A new node was added to the PDB: {PDB}{W}")

    test = test_sequence(PDB, [None, "B", "A", "C", None])
    print(f"When only a predecessor is given, insert_between works like tail_insert: {result(test)}")

    n4 = PDB._PositionalDoublyBase__insert_between("D", n2, n1)
    print(f"\n{B}A new node was added to the PDB: {PDB}{W}")

    test = test_sequence(PDB, [None, "B", "D", "A", "C", None])
    print(f"New node can be inserted between two sequential nodes: {result(test)}\n")

    try:
        PDB._PositionalDoublyBase__insert_between("X", n1, n4)
        print(f"pred & succ are not interchangeable: {result(False)}")
    except:
        print(f"pred & succ are not interchangeable: {result(True)}")

    test = len(PDB) == 4
    print(f"PDB size increases for every insertion: {result(test)}")

    print("~" * 50, "\n\n")

    return (n1, n2, n3, n4)


def TEST_delete_node(PDB, class_ref, nodes):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: delete_node{W}\n")

    print(f"{B}Current state of the PDB: {PDB}")
    print(f"These nodes are currently in the PDB: ", end="")
    for n in nodes:
        print(n, end=" ")
    print(W, "\n")

    h = PDB.header
    t = PDB.trailer

    val = PDB._PositionalDoublyBase__delete_node(nodes[0])
    print(f"{B}Node |A| was removed: {PDB}{W}\n")

    test = val == "A"
    print(f"Correct node value was returned: {result(test)}")

    test = len(PDB) == 3
    print(f"delete_node decreases size attribute: {result(test)}")

    test = nodes[0].value == nodes[0].prev == nodes[0].next == None
    print(f"Removed node's attributes are all set to None: {result(test)}")

    try:
        val = PDB._PositionalDoublyBase__delete_node(nodes[0])
        print(f"A node with value None (such as sentinel or already deleted node) cannot be removed: {result(False)}")
    except:
        print(f"A node with value None (such as sentinel or already deleted node) cannot be removed: {result(True)}")

    try:
        val = PDB._PositionalDoublyBase__delete_node("C")
        print(f"Cannot delete non-node object from list: {result(False)}")
    except:
        print(f"Cannot delete non-node object from list: {result(True)}")

    for n in nodes[1:]:
        val = PDB._PositionalDoublyBase__delete_node(n)

    print(f"\n{B}PDB was emptied: {PDB}{W}\n")

    test = h.next == t and t.prev == h
    print(f"Emptied PBD connects header and trailer sentinels: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_docs(PDB, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    print("DoublyNode Class Docstrings:\n")
    doc = class_ref.DoublyNode.set_prev.__doc__
    if doc != None:
        print(f"{B}set_prev() Documentation:{W} {doc}\n")
    else:
        print(f"{R}set_prev() Documentation Missing{W}\n")

    doc = class_ref.DoublyNode.set_next.__doc__
    if doc != None:
        print(f"{B}set_next() Documentation:{W} {doc}\n")
    else:
        print(f"{R}set_next() Documentation Missing{W}\n")

    doc = class_ref.DoublyNode.__str__.__doc__
    if doc != None:
        print(f"{B}str() Documentation:{W} {doc}\n")
    else:
        print(f"{R}str() Documentation Missing{W}\n")

    print("\n\nPositionalDoublyBase Class Docstrings:\n")
    doc = PDB._PositionalDoublyBase__insert_between.__doc__
    if doc != None:
        print(f"{B}insert_between() Documentation:{W} {doc}\n")
    else:
        print(f"{R}insert_between() Documentation Missing{W}\n")

    doc = PDB._PositionalDoublyBase__delete_node.__doc__
    if doc != None:
        print(f"{B}delete_node() Documentation:{W} {doc}\n")
    else:
        print(f"{R}delete_node() Documentation Missing{W}\n")

    doc = PDB._PositionalDoublyBase__is_empty.__doc__
    if doc != None:
        print(f"{B}is_empty() Documentation:{W} {doc}\n")
    else:
        print(f"{R}is_empty() Documentation Missing{W}\n")

    doc = PDB.__len__.__doc__
    if doc != None:
        print(f"{B}len() Documentation:{W} {doc}\n")
    else:
        print(f"{R}len() Documentation Missing{W}\n")

    doc = PDB.__str__.__doc__
    if doc != None:
        print(f"{B}str() Documentation:{W} {doc}\n")
    else:
        print(f"{R}str() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")
