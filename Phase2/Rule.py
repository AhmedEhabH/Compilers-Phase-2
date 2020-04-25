from .TheLIST import TheLIST
from .Pointer import Pointer

from anytree import Node


class Rule():
    def __init__(self, name):
        self.RHS = []
        self.name = name
        self.log = {}

    def check(self, parent_node):
        org_cursor = Pointer.pointer
        if org_cursor in self.log:
            Pointer.pointer = self.log[org_cursor][1]
            if self.log[org_cursor][0]:
                self.log[org_cursor][2].parent = parent_node
            return self.log[org_cursor][0]
        
        for choice in self.RHS:
            success = True
            cur_node = Node('%s_%s' % (self.name, Pointer.pointer))
            for code_obj in choice:
                if not (code_obj == 'NULL' or TheLIST.the_list[code_obj].check(cur_node)):
                    success = False
                    break
            if success:
                cur_node.parent = parent_node
                self.log[org_cursor] = [True, Pointer.pointer, cur_node]
                return True
            Pointer.pointer = org_cursor
        
        self.log[org_cursor] = [False, org_cursor]
        return False
