[← Return to Index]()

# MIPS Architecture

## Simplified MIPS Architecture

**Fetch** (from memory) → **Decode** (code instruction) → **Execute** (compute) → Repeat!

### Control
- Central Processor
- Facilitates communication between GPR, ALU, Memory and Co-Processors

### General Purpose Registers (GPR)
- Has 32 registers
- Acts as "short term memory"
- Communicates with the ALU

### Arithmetic Logic Unit (ALU)
- Performs computations
- Load-store architecture
- Communicates with GPR

## Memory
| Memory Diagram |
|:--:            |
| OS-only        |
| Text segment   |
| Static data    |
| Heap           |
| ...            |
| Stack          |
| OS-only        |

### Text Segment
- Grows downwards
- Starts at `0x00400000`
- Executable code goes here
- PC Register holds a reference to a specific address here

### Data Segment
- Grows downards
- Starts at `0x10000000`
- Contains static data (global variables)
- Grows into heap

### Stack Segment
- Grows upwards
- Starts at `0x7FFFFFFC`
- Called the 'system stack


## MIPS Instruction Format

### R-Type ("Register" Operands)
| 6 bits | 5 bits | 5 bits | 5 bits | 5 bits | 6 bits |
|:---:   |:---:   |:---:   |:---:   |:---:   |:---:   |
| `OPCODE`| `REG_RS` | `REG_RT` | `REG_RD` | ` SHIFT `| `FUNCTION` |

### I-Type ("Immediate" Operands)
| 6 bits | 5 bits | 5 bits | 16 bits |
|:---:   |:---:   |:---:   |:---:   |
| `OPCODE`| `REG_RS` | `REG_RT` | `IMMEDIATE VALUE` |

### J-Type ("Jump")
| 6 bits | 26 bits |
|:---:   |:---:   |
| `OPCODE`| `ADDRESS VALUE` |


