from binaryninja import *
import pyperclip

def conv(view, start, length):
    types = ['char', 'int16_t', 'int32_t', 'int64_t']
    curr = start
    var = view.get_data_var_at(start)
    if var == None:
        log_error("Not a variable.")
        return()
    name = view.get_symbol_at(start).name if view.get_symbol_at(start) != None else 'data_'+hex(start)[2:]
    e = 'little' if view.endianness == enums.Endianness.LittleEndian else 'big'
    typ = str(var.type.get_tokens_before_name()[0])
    if typ not in types:
        log_error("Type %s not supported." % typ)
        return
    wt = var.type.width
    al = var.type.alignment
    if typ != 'char':
        if al != 0:
            out = []
            for i in range(0,wt,al):
                out.append(int.from_bytes(view.read(curr,al),e))
                curr += al
            pyperclip.copy(name + ' = ' + str(out))
        else:
            pyperclip.copy(name + ' = ' + int.from_bytes(view.read(curr,al),e))
    else:
        if al != 0:
            out = b""
            for i in range(0,wt,al):
                out += view.read(curr,al)
                curr += al
            pyperclip.copy(name + ' = ' + str(out))
        else:
            pyperclip.copy(name + ' = ' + view.read(curr,al))
    log_info("Data copied! ☑️")


PluginCommand.register_for_range("pyconv", "convert binja data to python", conv)
