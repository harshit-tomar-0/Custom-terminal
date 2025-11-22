#my terminal
import subprocess
import os
#color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
print(f"""{BOLD}{MAGENTA}COUSTUM TERMINAL
BLUE OUTPUT MEANS LINUX COMMANDS AS WINDOWS
YELLOW OUPUT MEANS WINDOWS COMMANDS
REMEMBER LINUX COMMANDS ON WINDOWS WILL NOT WORKS AS THEY WORK IN LINUX!!{RESET}""")
def terminal(cmd,color=RESET):
    result= subprocess.run(cmd,shell=True,capture_output=True,text=True)
    for i in result.stdout.split("\n"):
        print(f"{color}{i}{RESET}")
    if result.stderr:
        print(f"{RED}Error:\n{result.stderr}{RESET}")
inp=''
while(inp !="exit"):
    pwd=os.getlogin()
    inp = input("{}{}#{}".format(GREEN,pwd,RESET)) #better approch will be to save all this data in file
    command_map = {
        "ls": "dir /a",  # Linux 'ls' maps to Windows 'dir /a'
        "pwd": "echo %cd%",  # Linux 'pwd' maps to Windows 'echo %cd%'
        "cat": "type",  # Linux 'cat' maps to Windows 'type'
        #"clear": "cls",  # Linux 'clear' maps to Windows 'cls'
        "echo": "echo",  # Linux 'echo' maps to Windows 'echo'
        "mkdir": "mkdir",  # Linux 'mkdir' maps to Windows 'mkdir'
        "rm": "del",  # Linux 'rm' maps to Windows 'del' for deleting files
        "touch": "type nul > ",  # Linux 'touch' maps to Windows to create a new file
        "cp": "copy",  # Linux 'cp' maps to Windows 'copy'
        "mv": "move",  # Linux 'mv' maps to Windows 'move'
        "rmdir": "rmdir",  # Linux 'rmdir' maps to Windows 'rmdir'
        "man": "help",  # Linux 'man' maps to Windows 'help' (limited)
        "grep": "findstr",  # Linux 'grep' maps to Windows 'findstr'
        "cut": "for /f",  # Linux 'cut' maps to Windows 'for /f'
        "sort": "sort",  # Linux 'sort' maps to Windows 'sort'
        "wc": "find /c /v \"\"",  # Linux 'wc' maps to Windows workaround
        "head": "powershell -Command \"Select-Object -First 10\"",  # Linux 'head' maps to Windows PowerShell
        "tail": "powershell -Command \"Select-Object -Last 10\"",  # Linux 'tail' maps to Windows PowerShell
        "ps": "tasklist",  # Linux 'ps' maps to Windows 'tasklist'
        "kill": "taskkill",  # Linux 'kill' maps to Windows 'taskkill'
        "df": "fsutil volume diskfree",  # Linux 'df' maps to Windows 'fsutil volume diskfree'
        "du": "dir /s",  # Linux 'du' maps to Windows 'dir /s'
        "ping": "ping",  # Linux 'ping' maps to Windows 'ping'
        "ifconfig": "ipconfig",  # Linux 'ifconfig' maps to Windows 'ipconfig'
        "netstat": "netstat",  # Linux 'netstat' maps to Windows 'netstat'
        "uname": "systeminfo",  # Linux 'uname' maps to Windows 'systeminfo'
        "uptime": "systeminfo | find \"System Boot Time\"",  # Linux 'uptime' maps to Windows 'systeminfo'
        "whoami": "whoami",  # Linux 'whoami' maps to Windows 'whoami'
        "alias": "Not supported in Windows directly",  # Linux 'alias' has no direct equivalent
        "ssh": "powershell -Command \"Start-Process ssh\"",  # Linux 'ssh' maps to Windows ssh client (if installed)
        "scp": "powershell -Command \"Copy-Item\"",  # Linux 'scp' has no direct equivalent, PowerShell can be used
        "apt": "winget",  # Linux 'apt' maps to Windows Package Manager 'winget'
        "yum": "winget",  # Linux 'yum' maps to Windows Package Manager 'winget'
    }
    found=0
    for i in range(len(command_map)):
        if inp.startswith(list(command_map.keys())[i]):
            if len(inp.split(" "))==2:
                inp = inp.split(" ")
                terminal("{} {}".format(list(command_map.values())[i],inp[1]),color=CYAN)
            elif len(inp.split(' '))==1:
                terminal("{}".format(list(command_map.values())[i]),color=CYAN)
            else:
                print(":Coming Soon...")
            found =1
    if found !=1:        
        if inp.startswith('cd '):
            inp = inp[3:]
            try:
                os.chdir(inp)
                pwd = inp
            except FileNotFoundError:
                print("{} not found".format(inp))
            except PermissionError:
                print(f"{RED}Permission Denied{RESET}")
        elif inp.startswith('cls') or inp.startswith('clear'):
            os.system('cls')
        elif inp.startswith('fool'):
            print("fools")
            exit(0)
        else:
            terminal(inp,color=YELLOW)


