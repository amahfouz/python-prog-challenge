#!/bin/python

class Node(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word, index):
        if index == len(word):
            self.is_word = True
            return

        char = word[index]
        if char in self.children:
            child = self.children[char]
        else:
            child = Node()
            self.children[char] = child

        if index < len(word):
            child.insert(word, index + 1)


    # traverses the tree in a 
    def pair_up(self):
        if not len(self.children):
            return 0, 1
        total_paired = 0
        total_remain = 0
        for _,child in self.children.iteritems():
            paired, remain = child.pair_up()
            total_paired += paired
            total_remain += remain

        if self.is_word:
            total_remain += 1

        if total_remain >= 2:
            total_paired += 2 
            total_remain -= 2
        
        return total_paired, total_remain 

###############################
class Solution(object):

    def __init__(self, words):
        self.trees = {}
        for word in words:
            rev = word[::-1]
            first = rev[0]
            if first in self.trees:
                tree = self.trees[first]
            else:
                tree = Node()
                self.trees[first] = tree
            
            tree.insert(rev, 1)  # reverse the word

    def solve(self):
        total_paired = 0
        for _, tree in self.trees.iteritems():
            paired, _ = tree.pair_up()
            total_paired += paired
        return total_paired

###############################

if __name__ == '__main__':        

    n = int(raw_input())
    for i in range(n):    
        num_words = int(raw_input())
        words = []
        for w in range(num_words):
            words.append(raw_input())

        sol = Solution(words)
        print "Case #" + str(i+1) + ":", sol.solve()
    