from InvalidInputException import InvalidInputException
from constants import L_FORMAT_ADD_OPERATIONS, L_FORMAT_OPERATIONS, L_FORMAT_WORD_OPERATIONS
from utils import convertToBinaryStr

'''
L-Format Operations: 
3 types: add immediates, lw / sw, beq / bne

add immediates:
- similar to R-Format Operations with diff operands

lw / sw:
i.e. opcode $x, y($z)
- x == rt
- y == immediate
- z == rs

beq / bne:
i.e. opcode $x, $y, z
- x == rs
- y == rt
- immediate == number of instructions to add to, or subtract from, the PC

'''
def convertLMIPSToBinary(MIPS_Instruction):
   if MIPS_Instruction[0] in L_FORMAT_ADD_OPERATIONS:
      return convertAddOperationsToBinary(MIPS_Instruction)
   elif MIPS_Instruction[0] in L_FORMAT_WORD_OPERATIONS:
      return convertWordOperationsToBinary(MIPS_Instruction)
   else:
      raise InvalidInputException("Invalid/Unsupported L-Format Operation")

def convertAddOperationsToBinary(MIPS_Instruction):
   opcode = L_FORMAT_OPERATIONS.get(MIPS_Instruction[0])
   rs = convertToBinaryStr(MIPS_Instruction[2][1:], 5)
   rt = convertToBinaryStr(MIPS_Instruction[1][1:], 5)
   immediate = convertToBinaryStr(MIPS_Instruction[3], 16)

   return opcode + rs + rt + immediate

def convertWordOperationsToBinary(MIPS_Instruction):
   opcode = L_FORMAT_OPERATIONS.get(MIPS_Instruction[0])
   rt = convertToBinaryStr(MIPS_Instruction[1][1:], 5)

   operand2 = MIPS_Instruction[2].split("(")
   immediate = operand2[0]
   immediate = convertToBinaryStr(immediate, 16)
   rs = operand2[1][1:][:-1]
   rs = convertToBinaryStr(rs, 5)

   return opcode + rs + rt + immediate