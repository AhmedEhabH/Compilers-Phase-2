import  Phase1.LexicalAnalyzer as LexicalAnalyzer
from Phase2.Parser import Parser
from Phase2.TokenWithValue import TokenWithValue
from files import files_path

def create_token_obj(tokens_name, tokens_value):
    tokens_without_prevents = []
    for name, value in zip(tokens_name, tokens_value):
        prevent = ['MULTI_COMMENT', 'SINGLE_COMMENT', "ERROR - ID can’t start with num"]
        if name in prevent: continue
        token_with_value = TokenWithValue(name, value)
        tokens_without_prevents.append(token_with_value)
    return tokens_without_prevents

def main():
    input_file = files_path['input']
    rules_file = files_path['grammar']
    tokens_file = files_path['tokens']
    print("PHSAE 1")
    tokens_name, tokens_value = LexicalAnalyzer.process(input_file)
    print("="*50)
    print("PHSAE2")
    tokens_without_prevents = create_token_obj(tokens_name, tokens_value)
    parser = Parser(rules_file, tokens_file)
    parser.generate_parse_tree(tokens_without_prevents)


if __name__ == "__main__":
    main()
