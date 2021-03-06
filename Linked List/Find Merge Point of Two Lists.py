#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    count1 = 0
    count2 = 0
    greater = 0
    difference = 0
    # traverse len head1
    curr1 = head1
    while curr1 != None:
        count1 += 1
        curr1 = curr1.next
    # traverse len head2
    curr2 = head2
    while curr2 != None:
        count2 += 1
        curr2 = curr2.next

    # compare
    diff = abs(count1 - count2)
    # iterate greater here
    curr1 = head1
    curr2 = head2
    if count1 > count2:
        # iter node 1
        while diff > 0:
            diff -= 1
            curr1 = curr1.next
    else:
        # iter node 2
        while diff > 0:
            diff -= 1
            curr2 = curr2.next
    # iterate both
    while (curr1 != None and curr2 != None):
        # check found
        if curr1 == curr2:
            return curr1.data
        curr1 = curr1.next
        curr2 = curr2.next

    # if not return -1
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next

        for i in range(llist2_count):
            if i != llist2_count - 1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()