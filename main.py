# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import checkDNS
import dns
from dns import zone,query,resolver

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dnsList=['ns1.hosting.reg.ru','ns2.hosting.reg.ru']
    listOfNsIP=checkDNS.DnsChecker.getDNSIP(dnsList)
    for i in dnsList:
        print(i,' : ')
        print(listOfNsIP.get(i)[0])
        listiplenght=len(listOfNsIP.get(i))
        print(listiplenght)
        myResolver = dns.resolver.Resolver()
        myResolver.nameservers = listOfNsIP.get(i)
        try:
            myAnswers = myResolver.query("myfproject.online", "A")
            for rdata in myAnswers:
                print("IP from NS ", i, " : ", rdata)
        except:
            print("Query failed")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
