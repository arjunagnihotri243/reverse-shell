import subprocess

cmdlet = 'mkdir a'
result = subprocess.check_output(cmdlet, shell=True)
