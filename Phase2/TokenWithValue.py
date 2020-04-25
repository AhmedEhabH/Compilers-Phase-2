from .TheLIST import TheLIST
from .Pointer import Pointer

from anytree import Node


class TokenWithValue():
    
    def __init__(self, name, value=""):
        self.name = name
        self.value = value

    def check(self, parent_node):
        if self.name == 'NULL':
            return True
        if not Pointer.is_in_range():
            return False
        if Pointer.tokens[Pointer.pointer].name == self.name:
            self.value = Pointer.tokens[Pointer.pointer].value
            Pointer.pointer += 1
            node = Node('%s_%s' % (self.name, Pointer.pointer), parent=parent_node)
            Node("< %s ><%s>" %(self.value, Pointer.pointer), parent=node)
            return True
        return False
