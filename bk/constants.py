
R_FORMAT_OPERATIONS = {
   "add": "000000",
   "addu": "000000",
   "sub": "000000",
   "subu": "000000",
   "sll": "000000",
   "srl": "000000"
}

L_FORMAT_OPERATIONS = {
   "addi": "001000",
   "addiu": "001001",
   "beq": "000100",
   "bne": "000101",
   "lw": "100011",
   "sw": "101011"
}

L_FORMAT_ADD_OPERATIONS = {
   "addi": "001000",
   "addiu": "001001"
}

L_FORMAT_LOOP_OPERATIONS = {
   "beq": "000100",
   "bne": "000101"
}

L_FORMAT_WORD_OPERATIONS = {
   "lw": "100011",
   "sw": "101011"
}

J_FORMAT_OPERATIONS = {
   "J": "000010"
}

REGISTER_NUMBER_MAPPING = {
   "$zero": 0,
   "$v0": 2, "$v1": 3,
   "$a0": 4, "$a1": 5, "$a2": 6, "$a3": 7,
   "$t0": 8, "$t1": 9, "$t2": 10, "$t3": 11, "$t4": 12, "$t5": 13, "$t6": 14, "$t7": 15,
   "$s0": 16, "$s1": 17, "$s2": 18, "$s3": 19, "$s4": 20, "$s5": 21, "$s6": 22, "$s7": 23,
   "$t8": 24, "$t9": 25
}