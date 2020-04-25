from .Rule import Rule


class GrammarSpliter:
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def process(grammar):
        GrammarSpliter.LHS, GrammarSpliter.RHS = GrammarSpliter.__get_LHS_RHS(grammar)
        GrammarSpliter.RHS, GrammarSpliter.rules = GrammarSpliter.__parse_RHS(GrammarSpliter.LHS, GrammarSpliter.RHS)
        return GrammarSpliter.LHS, GrammarSpliter.RHS, GrammarSpliter.rules
    
    @staticmethod
    def __get_LHS_RHS(grammar):
        LHS = []
        RHS = []
        for rule in grammar:
            rule = rule.split("=>")
            lhs = rule[0].strip()
            rhs = rule[1].strip()
            LHS.append(lhs)
            RHS.append(rhs)
        return LHS, RHS
    
    @staticmethod
    def __parse_RHS(LHS, RHS):
        new_RHS = {}
        rules = {}
        for index, rule in enumerate(RHS):
            rule = rule.split("|")
            rule = [token.strip().split()for token in rule]
            rule_name = LHS[index]
            new_RHS[rule_name] = rule
            rule_obj = Rule(rule_name)
            rule_obj.RHS = rule
            rules[rule_name] = rule_obj
        return new_RHS, rules

