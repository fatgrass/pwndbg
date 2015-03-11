import pwndbg.regs
import pwndbg.commands
import pwndbg.memory
import pwndbg.hexdump

@pwndbg.commands.ParsedCommand
@pwndbg.commands.OnlyWhenRunning
def hexdump(address=None, count=64):
    """Hexdumps some data"""
    address = int(address or pwndbg.regs.sp)
    count   = int(count)

    # if None not in (address, count):
    #     address = int(address)
    #     count   = int(count):

    if count > address > 0x10000:
        count -= address

    # if address is None:
    # 	address =

    data = pwndbg.memory.read(address, count)

    for line in pwndbg.hexdump.hexdump(data, address=address):
        print(line)

