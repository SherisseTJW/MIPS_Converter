from Modules.tokens.token import Token
from Modules.tokens.token_type import INIT, EOF, LABEL, INSTRUCTION, OPERAND
from Modules.tokens import token_kind

class Lexer:
    init_token = Token(INIT, None, None)

    def __init__(self, text):
        # Expect this text to be the contents of a file
        self.__text = text
        self.__current_line = 0
        self.__pos = 0
        self.__current_char = self.__text[self.__pos]

        self.__current_token_type = INIT
        self.__current_token_kind = None
        self.__current_token_value = None

    def run(self):
        """
        The entry function for the Lexer. Returns all the tokens after tokenising the text passed in
        """

        current_token = Lexer.init_token
        tokens = [current_token]

        while True:
            current_token = self.__get_next_token()
            tokens.append(current_token)

            if current_token.token_type == EOF:
                break

        return tokens


    def __get_next_token(self):
        print(self.__text)

        return Token(EOF, None, None)

    def __advance(self):
        pass

    def __peek(self):
        pass
