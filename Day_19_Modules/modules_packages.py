# Modules - python file with related functions
# Packages - collection of related modules
# related codes make modules, related modules makes packages, related packages makes library
###NOTE - type of errors - Runtime, Logical, Syntax - in logical output comes, in runtime output does not.

# import os
# os.mkdir('test')

#CLI & GUI 
'''
CLI - Command Line Interface is powerful and fast.  ---> Linux server
GUI - Graphical User Interface

pypi.org - repository site for python code.
pip - python package manager. --> It helps to install, uninstall and update python pacakages
'''

import webbrowser
# title = input('Enter Youtube search title ')
# webbrowser.open('facebook.com')
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application %s'
webbrowser.get(chrome_path).open('https://www.facebook.com')
