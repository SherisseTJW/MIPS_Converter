from constants import R_FORMAT_OPERATIONS
from utils import readDataFromInput
from RF import convertMIPSToBinary

if __name__ == "__main__":
   MIPS_Instruction = readDataFromInput()

   # If MIPS_Instruction is 1 line, then assume no loops involved
   if len(MIPS_Instruction) == 1:
      instruction = MIPS_Instruction[0].replace(",", "").split(" ")
      operation = instruction[0].lower()

      if operation in R_FORMAT_OPERATIONS:
         print(f"Binary representation: {convertMIPSToBinary(instruction)}")