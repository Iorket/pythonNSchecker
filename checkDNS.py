import socket
import dns
class DnsChecker:
        def getDNSIP(DNSlist):
                listNS_IP={}
                for i in DNSlist:
                        listNS_IP[i]= socket.gethostbyname_ex(i)[2]
                return listNS_IP
        def getARecordDNS(DNSList):
                currentNsIpList=DnsChecker.getDNSIP(DNSList)
