#!/usr/bin/python3

# SOFTWARE\Microsoft\Windows\CurrentVersion\Run
# Microsoft\Windows NT\CurrentVersion\Winlogon\System
# HKEY_LOCAL_MACHINE

from email import parser
import winreg
import argparse
import sys

class Registry:
    def __init__(self):
        pass

    @staticmethod
    def getArgs():
        parser = argparse.ArgumentParser(description="Query registers")
        parser.add_argument("-e","--enum", help="Enumerate all values")
        parser.add_argument("-q","--query",help="Query values")

        return parser.parse_args()

    def enum(self , hive , reg_path):
        try:
            registryKey = winreg.OpenKey(hive, reg_path,0 , winreg.KEY_READ)
            
            i=0
            while True:
                value = winreg.EnumKey(registryKey,i)
                print(value)
                i = i + 1
            
            winreg.CloseKey(registryKey)
        except:
            print("key not found")

    def query(self , hive , reg_path, value_name):
        try :
            registryKey = winreg.OpenKey(hive,reg_path,0,winreg.KEY_READ)
            value = winreg.QueryValueEx(registryKey,value_name)

            print(value)

            winreg.CloseKey(registryKey)
        except:
            print("key not found")

    
    def main(self):
        args = self.getArgs()
        hive = winreg.HKEY_CURRENT_USER

        if args.enum:
            self.enum(hive,args.enum)
        if args.query:
            self.query(hive , args.query[0],args.query[1])


if __name__ == '__main__':
    instance = Registry()
    instance.main()

        