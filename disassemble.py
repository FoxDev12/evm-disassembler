import sys
from optable import OP_TABLE

def get_opcode_name(opcode):
    if opcode in OP_TABLE:
        return OP_TABLE[opcode]
    else:
        return "INVALID"
def handle_push(code, pos):
    """ Handle PUSH operations by assembling the opcode with its data. """
    bytes_to_push = code[pos] - 0x5f
    output = f"PUSH{bytes_to_push} 0x"
    
    # Check if there are enough bytes left to read
    if pos + bytes_to_push + 1 > len(code):
        output += "ERROR: Incomplete data for PUSH instruction"
    else:
        output += ''.join(format(code[i], '02x') for i in range(pos + 1, pos + bytes_to_push + 1))
    
    output += "\n"
    return output, bytes_to_push + 1

def disassemble(code):
    """ Disassemble the bytecode into human-readable opcode instructions. """
    output = ""
    i = 0
    while i < len(code):
        opcode = code[i]
        if 0x60 <= opcode <= 0x7f:  # PUSHX instructions
            push_output, increment = handle_push(code, i)
            output += push_output
            i += increment
        else:
            opname = get_opcode_name(opcode)
            output += opname + "\n"
            i += 1
    return output

def is_bytecode(str):
    """ Check if a string consists solely of valid hexadecimal characters and is of even length. """
    return all(c in "0123456789abcdefABCDEF" for c in str) and len(str) % 2 == 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python disassemble.py [<filename> | <code>]")
        sys.exit(1)
    
    input_arg = sys.argv[1]
    code = None
    
    try:
        if is_bytecode(input_arg):
            code = bytes.fromhex(input_arg)
        else:
            with open(input_arg, "r") as f:
                file_content = f.read().strip()
                if is_bytecode(file_content):
                    code = bytes.fromhex(file_content)
                else:
                    print("Error: File content is not valid hexadecimal data.")
                    sys.exit(1)
    except Exception as e:
        print(f"Error processing input: {e}")
        sys.exit(1)
    
    if code:
        print(disassemble(code))
    else:
        print("Invalid input or file could not be processed.")