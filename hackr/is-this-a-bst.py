#!/bin/python

class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def check_binary_search_tree_(root):
    return check_node(root, 10001, -1)

def check_node(node, max_data, min_data):
    if node is None:
        return True
    if node.data > max_data or node.data < min_data:
        return False

    # new_min = max(node.data, min_data)
    # new_max = min(node.data, max_data)

    return check_node(node.left, node.data - 1, min_data) \
        and check_node(node.right, max_data, node.data + 1)
