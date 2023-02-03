# MIPS_Converter

This is just a quick MIPS to Binary and Hex Converter that I created to test my knowledge of the conversions (and also help me with my Labs, Quizzes, etc. since the online ones I found don't really help with beq, bne operations, as well as those with -ve immediate values)

I may or may not add more operations, but no guarantees.

## Features:

**Supports:**
- R-Format Operations: add, addu, sub, subu, sll, srl
- L-Format Operations: addi, addiu, beq, bne, lw, sw
- -ve immediate values for L-Format Operations
- Multiline operations for beq and bne

## How to use:
1. Git clone the repo to your local machine
2. Create an input file with the MIPS instruction you want to convert
3. Run `python3 main.py`

### Input
You will have to create an input file (`input`) in the root directory. Then, just write the MIPS Instruction that you want to convert into that file.

Sample Input Files can be found [here](./samples/).

## Disclaimer
This program may not be 100% accurate, so make sure you double check the calculations. I am not responsible for lost marks :D