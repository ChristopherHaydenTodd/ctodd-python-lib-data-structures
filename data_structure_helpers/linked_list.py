#!/usr/bin/env python3
"""
    Purpose:
        Linked List Class for Link List DataTypes in Python

    Examples of Create Object of Class:
        linked_list_object = LinkedList()
"""

# Python Library Imports
import sys
import os

# Custom Python Library Imports
from data_structures.linked_list_node import LinkedListNode


class LinkedList(object):
    """
        LinkedList Class
    """

    ###
    # Class Lifecycle Methods
    ###

    def __init__(self):
        """
        Purpose:
            Initilize the LinkedList Class.
        Args:
            N/A
        """

        self._head_node = None
        self._tail_node = None

        pass

    # def __del__(self):
    #     """
    #     Purpose:
    #         Delete the LinkedListNode Object. This requires
    #         making the current node's child node link to the
    #         current node's parent node if this node is not
    #         the tail.
    #     Args:
    #         N/A
    #     """

    #     raise Exception(
    #         'Cannot Delete Linked List Yet!'
    #     )

    ###
    # Property Methods
    ###

    @property
    def head_node(self):
        """
        Purpose:
            Return value of class property _head_node, which
            stores the first node in the linked list
        Args:
            N/A
        """

        return self._head_node

    @head_node.setter
    def head_node(self, head_node):
        """
        Purpose:
            Set value of class property _head_node, which
            stores the first node in the linked list
        Args:
            head_node (LinkedListNode): Node to
                set as head node
        """

        if not isinstance(head_node, LinkedListNode):
            raise TypeError(
                'Head Node provide is not a Node object'
            )

        self._head_node = head_node

    @head_node.deleter
    def head_node(self):
        """
        Purpose:
            Delete the head node of the linked list. This
            should not occur, so raise exception
        Args:
            N/A
        """

        raise Exception('Cannot Delete Head Node Yet!')

    @property
    def tail_node(self):
        """
        Purpose:
            Return value of class property _tail_node, which
            stores the last node in the linked list
        Args:
            N/A
        """

        return self._tail_node

    @tail_node.setter
    def tail_node(self, tail_node):
        """
        Purpose:
            Set value of class property _tail_node, which
            stores the last node in the linked list
        Args:
            tail_node (LinkedListNode): Node to
                set as tail node
        """

        if not isinstance(tail_node, LinkedListNode):
            raise TypeError(
                'Tail Node provide is not a Node object'
            )

        self._tail_node = tail_node

    @tail_node.deleter
    def tail_node(self):
        """
        Purpose:
            Delete the tail node of the linked list. This
            should not occur, so raise exception
        Args:
            N/A
        """

        raise Exception('Cannot Delete Tail Node Yet!')

    ###
    # Class Methods
    ###

    def traverse_linked_list(self):
        """
        Purpose:
            Traverse the node from head to tail printing
            the value and the position of the node
        Args:
            N/A
        Returns:
            N/A
        """

        if not self.head_node:
            print('No List to Traverse')
            return

        current_node = self.head_node
        node_iterator = 0
        while True:
            print(
                'Current Node Value (position {0}): {1}'.format(
                    node_iterator, current_node.node_value
                )
            )
            node_iterator += 1
            current_node = current_node.child_node
            if not current_node:
                return

    def find_node_by_value(self, value):
        """
        Purpose:
            Find first instance of a node with the
            value specified. Will start at the head
            and traverse the linked list until the value is
            found. If the value is not in the linked list,
            None, None will be returned. This returns
            the node itself and the position of the node
        Args:
            value (Any): Value to search the linked list
                for
        Returns:
            node (LinkedListNode): First node object with
                a manching value
            position (int): Position of the node in the linked
                list
        """

        if not self.head_node:
            return None, None

        current_node = self.head_node
        node_iterator = 0
        while True:
            if value == current_node.node_value:
                return current_node, node_iterator

            node_iterator += 1
            current_node = current_node.child_node

            if not current_node:
                return None, None

    def delete_node_by_value(self, value, method='first'):
        """
        Purpose:
            Delete all/first node with specified value. If
            no method is passed, only the first node is deleted.
            If all is passed in as the method, then all nodes
            with the value are deleted
        Args:
            value (Any): Value to search the linked list
                for
            method (String): Method to delete node. Must be
                either 'all' or 'first'. Defaults to first
        Returns:
            N/A
        """

        import pdb; pdb.set_trace()

    def delete_node_at_position(self, position):
        """
        Purpose:
            Delete node to specified position in linked list.

            Note: head_node == position 0
        Args:
            position (Int): Position in which to delete the
                node in the linked list. If the position is
                greater than the legnth, no operation is taken
        Returns:
            N/A
        """

        if not self.head_node:
            return
        if position == 0:
            self.head_node = self.head_node.child_node
            del self.head_node.parent_node
            return

        current_node = self.head_node
        node_iterator = 0
        while node_iterator <= position:

            if node_iterator == position:
                current_node.parent_node.child_node =\
                    current_node.child_node
                current_node.child_node.parent_node =\
                    current_node.parent_node

            node_iterator += 1
            current_node = current_node.child_node

        return


    def add_node_to_beginning(self, node):
        """
        Purpose:
            Add node to beginning of linked list
        Args:
            node (LinkedListNode): Node to append
                to the beginning of the linked list
        Returns:
            N/A
        """

        # Set head and tail if first node in list
        if not self.head_node:
            self.head_node = node
            self.tail_node = node
        else:
            self.head_node.parent_node = node
            node.child_node = self.head_node
            self.head_node = node

        return

    def add_node_to_end(self, node):
        """
        Purpose:
            Add node to end of linked list
        Args:
            node (LinkedListNode): Node to append
                to the end of the linked list
        Returns:
            N/A
        """

        # Set head and tail if first node in list
        if not self.head_node:
            self.head_node = node
            self.tail_node = node
        else:
            self.tail_node.child_node = node
            node.parent_node = self.tail_node
            self.tail_node = node

        return

    def add_node_at_position(self, node, position):
        """
        Purpose:
            Add node to specified position in linked list.

            Note: head_node == position 0
        Args:
            node (LinkedListNode): Node to append
                to the end of the linked list
            position (Int): Position in which to insert the
                node in the linked list. If the position is
                greater than the legnth, defaults to the end
                of the list
        Returns:
            N/A
        """

        if not self.head_node:
            self.tail_node.child_node = node
            node.parent_node = self.tail_node
            self.tail_node = node
            return

        current_node = self.head_node
        node_iterator = 0
        while node_iterator <= position - 1:

            node_iterator += 1
            current_node = current_node.child_node

            if not current_node:
                self.tail_node.child_node = node
                node.parent_node = self.tail_node
                self.tail_node = node
                return

        node.child_node = current_node
        node.parent_node = current_node.parent_node
        node.parent_node.child_node = node
        node.child_node.parent_node = node

        return
