import io
import traceback
import wmi
from winreg import (HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, OpenKey, EnumValue, QueryValueEx)

softFile = open('softLog.log', 'w')
errorLog = open('errors.log', 'w')
HKLM = 0x80000002
r = wmi.Registry()
result, names = r.EnumKey(hDefKey=HKLM, sSubKeyName=r"Software\Microsoft\Windows\CurrentVersion\Uninstall")
softFile.write('These subkeys are found under "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\\Uninstall"\n\n')
errorLog.write("Errors\n\n")
separator = "*" * 80
keyPath = r"Software\Microsoft\Windows\CurrentVersion\Uninstall"

for subkey in names:
    try:
        softFile.write(separator + '\n\n')
        path = keyPath + "\\" + subkey
        key = OpenKey(HKEY_LOCAL_MACHINE, path, 0, KEY_ALL_ACCESS) 
        try:
            temp = QueryValueEx(key, 'DisplayName')
            display = str(temp[0])
            temp2 = QueryValueEx(key, 'DisplayVersion')
            display2 = str(temp2[0])
            softFile.write('Display Name: ' + display + '\nVersion: ' + display2 + '\nRegkey: ' + subkey + '\n')
        except:
            softFile.write('Regkey: ' + subkey + '\n')
    except:
        fp = io.StringIO()
        traceback.print_exc(file=fp)
        errorMessage = fp.getvalue()
        error = 'Error for ' + key + '. Message follows:\n' + errorMessage
        errorLog.write(error)
        errorLog.write("\n\n")
        
softFile.close()
errorLog.close()
