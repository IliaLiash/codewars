def flap_display(lines, rotors):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'
    s = ''
    buff_res = []
    final_result = []
    for j in range(len(lines)):
        for rotor in rotors:
            for k in range(len(rotor)):
                for i in range(len(lines[j])):
                    a = (alpha.index(lines[j][i]) + rotor[k]) % len(alpha)
                    buff_res.append(alpha[a])
                buff_res = ''.join(buff_res)
                lines[j] = buff_res
                
                s += buff_res[k]
                buff_res = []
                
            final_result.append(s)
            s = ''
            j += 1
            if len(final_result) == len(lines):
                return final_result
