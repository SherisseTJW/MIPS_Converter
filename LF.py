from constants import L_FORMAT_OPERATIONS
from utils import convertToBinaryStr

def convertLMIPSToBinary(MIPS_Instruction):
   opcode = L_FORMAT_OPERATIONS.get(MIPS_Instruction[0])
   rs = convertToBinaryStr(MIPS_Instruction[2][1:], 5)
   rt = convertToBinaryStr(MIPS_Instruction[1][1:], 5)
   immediate = convertToBinaryStr(MIPS_Instruction[3], 16)

   fullBinary = opcode + rs + rt + immediate
   return fullBinary