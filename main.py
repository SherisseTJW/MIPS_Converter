from sys import argv
from Modules.compiler.lexer import Lexer


if __name__ == "__main__":
    #NOTE: argv[0] is the name of the file being run
    mips_code_filename = argv[1]

    with open(mips_code_filename, "r") as f:
        lines = f.readlines()
        f.close()

    lexer = Lexer(lines)
    lexer.run()
