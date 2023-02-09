from constants import R_FORMAT_OPERATIONS
from utils import convertToBinaryStr, getRegisterNumber

'''
R-Format Operations: 
opcode rs rt rd shamt funct

opcode -> based on operation
rs -> Source Register
rt -> Destination Register
shamt -> Shift Amount (only for sll, srl)
funct -> 0 for sll, srl, 32 otherwise
'''
def convertRMIPSToBinary(MIPS_Instruction):
   opcode = R_FORMAT_OPERATIONS.get(MIPS_Instruction[0])
   rd = convertToBinaryStr(getRegisterNumber(MIPS_Instruction[1]), 5)

   if MIPS_Instruction[3][0] == "$":
      rt = convertToBinaryStr(getRegisterNumber(MIPS_Instruction[3]), 5)
      rs = convertToBinaryStr(getRegisterNumber(MIPS_Instruction[2]), 5)
      shamt = convertToBinaryStr(0, 5)
      funct = convertToBinaryStr(32, 6)
   else:
      rt = convertToBinaryStr(getRegisterNumber(MIPS_Instruction[2]), 5)
      rs = convertToBinaryStr(0, 5)
      shamt = convertToBinaryStr(MIPS_Instruction[3], 5)
      funct = convertToBinaryStr(0, 6)

   
   fullBinary = opcode + rs + rt + rd + shamt + funct
   return fullBinary