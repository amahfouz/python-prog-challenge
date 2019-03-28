#!/bin/python

class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def check_binary_search_tree_(root):
    if node is None:
        return True
    return check_node(root)

def check_node(node):
    if node is None:
        return True
    return check_left(node.left, node.data) \
        and check_right(node.right, node.data)

def check_left(node, data):
    return node.data < data and check_node(node)              

def check_right(node, data):
    return node.data > data and check_node(node)              
