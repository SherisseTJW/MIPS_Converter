"""
Each Token has 3 values: 
    token_type: The general type of token it is, i.e INSTRUCTION / OPERAND
    token_kind: What kind of token type it is, i.e. for INSTRUCTION, it can be AND, SUB, SLT, etc.
    token_value: The exact value in the MIPS code, i.e. if REGISTER OPERAND, it can be $t0, etc.
"""

class Token:
    def __init__(self, token_type, token_kind, token_value):
        self.token_type = token_type
        self.token_kind = token_kind
        self.token_value = token_value

    def get_value(self):
        return self.token_value

    def __str__(self):
        if self.token_kind:
            return f"{self.token_kind} {self.token_type} Token with value {self.token_value}"


        return f"{self.token_type} Token with value {self.token_value}"
