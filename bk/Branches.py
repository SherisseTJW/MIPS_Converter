from constants import L_FORMAT_LOOP_OPERATIONS
from utils import convertToBinaryStr, getRegisterNumber

def convertBranchMIPSToBinary(MIPS_Instruction):
   for i in range(0, len(MIPS_Instruction)):
      MIPS_Instruction[i] = MIPS_Instruction[i].replace(",", "").split(" ")

   for key in L_FORMAT_LOOP_OPERATIONS.keys():
      if key in MIPS_Instruction[0]:
         return convertLFBranchToBinary(MIPS_Instruction, key)
   
def convertLFBranchToBinary(MIPS_Instruction, operation):
   baseInstruction = MIPS_Instruction[0]

   # Get the immediate value
   label = baseInstruction[-1] + ":"
   immediate = 0

   for i in range (0, len(MIPS_Instruction)):
      if label in MIPS_Instruction[i]:
         immediate = i - 1


   opcode = L_FORMAT_LOOP_OPERATIONS.get(operation)
   rs = convertToBinaryStr(getRegisterNumber(baseInstruction[2]), 5)
   rt = convertToBinaryStr(getRegisterNumber(baseInstruction[3]), 5)
   immediate = convertToBinaryStr(immediate, 16)

   return opcode + rs + rt + immediate
