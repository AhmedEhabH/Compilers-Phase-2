from .Rule import Rule
from .TokenWithValue import TokenWithValue
from .GrammarSpliter import GrammarSpliter
from .TheLIST import TheLIST
from .Pointer import Pointer
from anytree import Node, RenderTree
from anytree.exporter import DotExporter


class Parser():
    def __init__(self, rules_file, tokens_file):
        Parser.__parse_grammar(rules_file, tokens_file)

    @staticmethod
    def __parse_grammar(rules_file, tokens_file):
        Parser.__parse_rules(rules_file)
        Parser.__parse_tokens(tokens_file)

    @staticmethod
    def __parse_rules(rules_file):
        """Parse rules in grammar file and put them in `code_objs`."""
        
        grammar = []
        with open(rules_file) as file:
            grammar = file.readlines()
            file.close()
        lhs, rhs, rules = GrammarSpliter.process(grammar)
        TheLIST.the_list = rules

    @staticmethod
    def __parse_tokens(tokens_file):
        prevent = ['MULTI_COMMENT', 'SINGLE_COMMENT', "ERROR - ID can’t start with num"]
        with open(tokens_file) as file:
            for line in file.readlines():
                token_name = line.strip()
                if token_name in prevent: continue
                # print(token_name)
                TheLIST.the_list[token_name] = TokenWithValue(token_name)
            file.close()

    def generate_parse_tree(self, tokens):
        Pointer.tokens[:] = tokens
        Pointer.pointer = 0
        tree_root = Node('program')
        success = TheLIST.the_list['decl_list'].check(tree_root)
        print(success)
        # print(RenderTree(tree_root))
        DotExporter(tree_root).to_picture('Tree.png')
        if success:
            print("OPEN IMAGE Tree.png")
