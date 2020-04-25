class Pointer:
    pointer = 0
    tokens = []

    def __init__(self):
        super().__init__()
        self.pointer = 0
        self.tokens = []
    
    @staticmethod
    def is_in_range():
        return Pointer.pointer < len(Pointer.tokens)
    
    @staticmethod
    def print_tokens():
        print("=== Tokens ===")
        for token in Pointer.tokens:
            print(token)
        print("==============")