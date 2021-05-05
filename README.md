# Antivirus_Checker

A Python code that checks antivirus or any software that you mention into the wordlist; the status with its version information.

Note: These scripts are particularly made to use for Windows OS only.


**PRE-REQUISITES:**

You may need to install wmi module. For those who haven't use a simple pip command: pip install wmi


**USAGE:**

Run the soft_check.py, it will return the list of softwares installed by user specifically and prints it to a log file _softLog_ for you to check this list of software.
Basically, this script just enumerates all the entries from the _HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall_ and creates a softLog file as mentioned before.

Next, you have to run version_check.py to filter out specific version details for the software that is in the wordlist.
This script compares the version of installed software with the new version that has been mentioned into the _jsondata_ variable (it fetches the name of the software from the wordlist to check if it is inside the softLog file and finally compares the version information present inside the softLog file with the jsondata variable inside of the script). You may create a database of different softwares with their latest versions or fetch data using any API if you want. You are free to edit and use this script as per your own convenience.
