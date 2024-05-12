# evm disassembler
 A very barebones disassembler for EVM bytecode. Feel free to contribute, open PRs, report bugs.. 

## Usage : 
 python3 disassemble.py <file-or-code>


# TODO

## Short term :
    QoL improvements : 
        Add the option to save to a file 
            can be achieved in the shell with redirections (use `python3 disassemble.py <file-or-code> > <output_file>`)
            but make it a program argument
    Features : 
        Add the option to auto detect and remove constructor code

## Longer term : 
    Add labels for jumps 
    Make an assembler 
    Make an usable assembly language for this assembler. 