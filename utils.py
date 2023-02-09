from constants import REGISTER_NUMBER_MAPPING

def readDataFromInput(filename = None):
   MIPS_Instruction = []

   if not filename:
      filename = "input"

   f = open(filename, "r")
   for line in f:
      MIPS_Instruction.append(line.strip())
   f.close()

   return MIPS_Instruction

def getRegisterNumber(registerName: str):
   if registerName not in REGISTER_NUMBER_MAPPING:
      return registerName[1:]
      pass

   return REGISTER_NUMBER_MAPPING.get(registerName)

def convertToBinaryStr(decimalInput, length):
   decimalInput = int(decimalInput)

   if decimalInput < 0:
      binary = convertNegativeDecimalTo2sComplement(decimalInput, length)
   else:
      binary = str(bin(decimalInput)[2:])

      while len(binary) < length:
         binary = "0" + binary

   return binary 

def convertNegativeDecimalTo2sComplement(decimalInput, length):
   binary = str(bin(decimalInput)[3:])
   binary = list(binary)

   ### Invert all the bits
   for i in range(0, len(binary)):
      bit = binary[i]
      if bit == "0":
         binary[i] = "1"
      else:
         binary[i] = "0"

   ### Perform the +1
   binary = binary[::-1]
   for i in range(0, len(binary)):
      bit = binary[i]

      if bit == "0":
         binary[i] = "1"
         break
      else:
         binary[i] = "0"
         continue
   binary = "".join(binary[::-1])

   while len(binary) < length:
      binary = "1" + binary

   return binary

def convertBinaryToHex(binaryInput):
   decimalRepresentation = int(binaryInput, 2)
   return hex(decimalRepresentation)[2:]