from constants import R_FORMAT_OPERATIONS
from utils import readDataFromInput, convertBinaryToHex
from RF import convertMIPSToBinary

if __name__ == "__main__":
   MIPS_Instruction = readDataFromInput()

   # If MIPS_Instruction is 1 line, then assume no loops involved
   if len(MIPS_Instruction) == 1:
      instruction = MIPS_Instruction[0].replace(",", "").split(" ")
      operation = instruction[0].lower()

      if operation in R_FORMAT_OPERATIONS:
         binary = convertMIPSToBinary(instruction)
         print(f"Binary representation: {binary}")
         print(f"Hexadecimal representation: {convertBinaryToHex(binary)}")