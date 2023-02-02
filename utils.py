def readDataFromInput(filename = None):
   MIPS_Instruction = []

   if not filename:
      filename = "input"

   f = open(filename, "r")
   for line in f:
      MIPS_Instruction.append(line.strip())
   f.close()

   return MIPS_Instruction

def convertToBinaryStr(decimalInput, length):
   binary = str(bin(int(decimalInput))[2:])
   while len(binary) < length:
      binary = "0" + binary


   return binary 