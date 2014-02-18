#!/usr/bin/env python
# encoding: utf-8

from ldif import LDIFParser # python-ldap
import sys
import os

class LDIF2John(LDIFParser):
    def __init__(self, infile=None, outfile=None):
        if infile:
            self._if = open(infile, "r")
        else:
            self._if = sys.stdin
        if outfile:
            self._of = open(outfile, "w")
        else:
            self._of = sys.stdout
        LDIFParser.__init__(self, self._if)

    #override
    def handle(self, dn, entry):
        if "objectClass" in entry and \
            "posixAccount" in entry["objectClass"]:
            cn = "cn" in entry and entry["cn"][0] or ""
            userPassword = "userPassword" in entry and entry["userPassword"][0] or ""
            if userPassword.startswith("{"):
                #The john will guess what the password's hash algorism is.
                userPassword = userPassword[userPassword.find("}")+1:]
            uidNumber = "uidNumber" in entry and entry["uidNumber"][0] or ""
            gidNumber = "gidNumber" in entry and entry["gidNumber"][0] or ""
            gecos = "gecos" in entry and entry["gecos"][0] or ""
            homeDirectory = "homeDirectory" in entry and entry["homeDirectory"][0] or ""
            loginShell = "loginShell" in entry and entry["loginShell"][0] or ""
            line = [cn,userPassword,uidNumber,gidNumber,
                    gecos,homeDirectory,loginShell]
            #line = [l.replace(":"," ") for l in line]
            #line = [l.replace(","," ") for l in line]
            self._of.write(":".join(line))
            self._of.write(os.linesep)
    #override
    def parse_and_close(self):
        self.parse()
        self._of.close()
        self._if.close()

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        LDIF2John().parse_and_close()
    elif argc < 3:
        LDIF2John(sys.argv[1]).parse_and_close()
    else:
        LDIF2John(sys.argv[1],sys.argv[2]).parse_and_close()
