#!/usr/bin/env python3
"""
    Purpose:
        Generate Tree for testing and traversal
"""

# Python Library Imports
import logging
import random
from anytree import Node, RenderTree


def generate_tree(node_count, max_depth, max_children):
    """
    Purpose:
        Generate A Random Tree
    Args:
        node_count (Int): Count of nodes in generated tree
        max_depth (Int): Max depth of tree
        max_children (Int): Max children per node
    Returns:
        root_node (Node Obj): Root node of the tree
        nodes (Dict of Node Obj): Nodes in the tree
    """

    nodes = {
        '1': {
            'node': Node('1'),
            'depth': 1,
            'children': 0,
        },
    }

    for i in range(2, node_count + 1):

        available_parents = []
        for node_name, node_metadata in nodes.items():
            if ((node_metadata['children'] < max_children) and
                (node_metadata['depth'] != max_depth)):
                available_parents.append(node_name)

        if not available_parents:
            error_message = 'Invalid Tree Configuration'
            logging.error(error_message)
            raise Exception(error_message)

        parent_node_name = random.choice(available_parents)
        parent_node = nodes.get(parent_node_name).get('node')

        nodes[str(i)] = {
            'node': Node(str(i), parent=parent_node),
            'depth': nodes.get(parent_node_name).get('depth') + 1,
            'children': 0,
        }

        nodes.get(parent_node_name)['children'] += 1

    return nodes['1']['node'], nodes
