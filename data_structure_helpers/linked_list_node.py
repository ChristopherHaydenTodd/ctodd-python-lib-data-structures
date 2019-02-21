#!/usr/bin/env python3
"""
    Purpose:
        Linked List Node Class for Link List
        Nodes Supporting the Linked List DataTypes
        in Python

    Examples of Create Object of Class:
        linked_list_node_object = LinkedListNode()
"""

class LinkedListNode(object):
    """
        LinkedListNode Class
    """

    ###
    # Class Lifecycle Methods
    ###

    def __init__(self):
        """
        Purpose:
            Initilize the LinkedListNode Object.
        Args:
            N/A
        """

        self._node_value = None
        self._parent_node = None
        self._child_node = None

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

    #     pass

    ###
    # Property Methods
    ###

    @property
    def node_value(self):
        """
        Purpose:
            Return value of class property _node_value
        Args:
            N/A
        """

        return self._node_value

    @node_value.setter
    def node_value(self, node_value):
        """
        Purpose:
            Set value of class property _node_value
        Args:
            node_value (Anything): Value to set to the
                class property _node_value
        """

        self._node_value = node_value

    @node_value.deleter
    def node_value(self):
        """
        Purpose:
            Delete value of node. This will set the value
            of the node to None instead of deleting the
            node or value property
        Args:
            N/A
        """

        self._node_value = None

    @property
    def parent_node(self):
        """
        Purpose:
            Return value of class property _parent_node
        Args:
            N/A
        """

        return self._parent_node

    @parent_node.setter
    def parent_node(self, parent_node):
        """
        Purpose:
            Set value of class property _node_value
        Args:
            parent_node (LinkedListNode): Node to
                set as parent node
        """

        if not isinstance(parent_node, LinkedListNode):
            raise TypeError(
                'Parent node provide is not a Node object'
            )

        self._parent_node = parent_node

    @parent_node.deleter
    def parent_node(self):
        """
        Purpose:
            Delete parent node connection (not delete the node).
            This will set the value of parent_node to None
            and update the parent_node to have no child_node.

            This essentially splits the linked list into two
            seperate linked lists
        Args:
            N/A
        """

        self._parent_node = None

    @property
    def child_node(self):
        """
        Purpose:
            Return value of class property _child_node
        Args:
            N/A
        """

        return self._child_node

    @child_node.setter
    def child_node(self, child_node):
        """
        Purpose:
            Set value of class property _child_node
        Args:
            child_node (LinkedListNode): Node to
                set as child node
        """

        if not isinstance(child_node, LinkedListNode):
            raise TypeError(
                'Parent Node provide is not a Node object'
            )

        self._child_node = child_node

    @child_node.deleter
    def child_node(self):
        """
        Purpose:
            Delete value of node. This will set the value
            of the node to None instead of deleting the
            node or value property
        Args:
            N/A
        """

        self._child_node = None

    ###
    # Class Methods
    ###

    def is_head_node(self):
        """
        Purpose:
            Returns True if Node is a head node. Returns
            false if the Node is not a head node. Completes
            this task by looking at the _parent_node class
            property.
        Args:
            N/A
        """

        return True if not self.parent_node else False

    def is_tail_node(self):
        """
        Purpose:
            Returns True if Node is a tail/leaf node. Returns
            false if the Node is not a tail/leaf node. Completes
            this task by looking at the _child_node class
            property.
        Args:
            N/A
        """

        return True if not self.children_node else False

    def is_part_of_linked_list(self):
        """
        Purpose:
            Returns True if Node has a parent or child. If
            the node does not have a parent or child, it is
            a stranded node.
        Args:
            N/A
        """

        return True if self.children_node or self.parent_node else False
