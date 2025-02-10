# Dylan Stitt
# Unit 5 Lab 4
# Positional Doubly Base Class

# Implementation & testing of the PositionalDoublyBase class

from PositionalDoublyBase import PositionalDoublyBase
from TEST_CODE import *
import os

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''


def main():
    PDB = PositionalDoublyBase()

    # TEST 1 - Test PDB Creation
    # BEFORE TESTING: implement PBD __init__
    TEST_new_PDB(PDB, PositionalDoublyBase)

    # TEST 2 - Test DoublyNode
    # BEFORE TESTING: implement DoublyNode class
    TEST_doubly_node(PositionalDoublyBase)

    # TEST 3 - Test insert_between
    # BEFORE TESTING: implement PBD insert_between, len, is_empty
    nodes = TEST_insert_between(PDB, PositionalDoublyBase)

    # TEST 4 - Test delete_node
    # BEFORE TESTING: implement PBD delete_node
    TEST_delete_node(PDB, PositionalDoublyBase, nodes)

    # TEST 5 - Test docstrings
    # BEFORE TESTING: implement method docstrings
    TEST_docs(PDB, PositionalDoublyBase)


if __name__ == "__main__":
    os.system("cls")
    main()