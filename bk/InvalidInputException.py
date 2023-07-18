class InvalidInputException(Exception):
   def __init__(self, message) -> None:
      name = "InvalidInputException"
      errMessage = "Invalid MIPS Instruction detected"
      if message:
         errMessage = f"{errMessage}: {message}"

      super().__init__(name, errMessage)