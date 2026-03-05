#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import re


def timestampToId(timestamp: float):
    assert isinstance(timestamp, float)
    return int(str(timestamp).replace(".", ""))

def splitANSI(string: str):
    ansi_regex = re.compile(r'\x1b\[[0-9;?]*[A-Za-z]')
    result = []
    current_ansi = ''
    i = 0
    while i < len(string):
        m = ansi_regex.match(string, i)
        if m:
            current_ansi += m.group()
            i = m.end()
        else:
            result.append(current_ansi + string[i])
            current_ansi = ''
            i += 1
    return result
