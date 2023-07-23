from Modules.tokens.token import Token
from Modules.tokens.token_type import INIT, EOF, LABEL, INSTRUCTION, OPERAND
from Modules.tokens import token_kind

class Lexer:
    init_token = Token(INIT, None, None)
    eof_token = Token(EOF, None, None)

    def __init__(self, text):
        # Expect this text to be the contents of a file
        self.__text = text
        self.__current_line = 0
        self.__pos = 0
        self.__current_char = self.__text[self.__pos]

        self.__current_token_type = INIT
        self.__current_token_kind = None
        self.__current_token_value = None

        self.__tokens = []

    def run(self):
        """
        The entry function for the Lexer. Returns all the tokens after tokenising the text passed in
        """

        self.__tokens.append(Lexer.init_token)

        for line in self.__text:
            current_line_tokens = self.__tokenise_next_line(line)
            self.__tokens.append(current_line_tokens)

        self.__tokens.append(Lexer.eof_token)
        print(self.__tokens)
        return self.__tokens


    def __tokenise_next_line(self, line):
        line_tokens = []
        line = line.strip().split(" ")

        for value in line:
            current_token = self.__tokenise(value)
            line_tokens.append(current_token)

        return line_tokens

    
    def __tokenise(self, value):
        if value[-1] == ":":
            self.__current_token_value = value[:-1]
            self.__current_token_type = LABEL
            self.__current_token_kind = None

        elif value[0] == "$":
            if value[-1] == ",":
                self.__current_token_value = value[:-1]
            else:
                self.__current_token_value = value

            self.__current_token_type = OPERAND
            self.__current_token_kind = token_kind.OPERAND["REGISTER"]

        elif value.isdigit():
            self.__current_token_value = value
            self.__current_token_type = OPERAND
            self.__current_token_kind = token_kind.OPERAND["NUMBER"]

        else:
            self.__current_token_value = value.upper()
            self.__current_token_type = INSTRUCTION
            self.__current_token_kind = token_kind.INSTRUCTION[self.__current_token_value]

        return Token(self.__current_token_type, self.__current_token_kind, self.__current_token_value)

    
