import dns.resolver
import socket
import re
import sys



def check_tcp(address, port):
	# Create a TCP socket
	s = socket.socket()
	try:
		s.connect((address, port))
		return "Connected to %s on port %s" % (address, port)
		return True
	except socket.error, e:
		return "Connection to %s on port %s failed: %s" % (address, port, e)
		return False

def check_con_tcp(hosts):
    '''
    Check tcp connections for host in list
    '''
    answer=[]
    for host in hosts:
        answer.append(check_tcp(host[0],host[1]))
    return answer


def check_dns(name):
    '''
    Check dns entries for name list and retrun an list of resolved names.
    '''
    answer_list=[]
    for domain in name:
        answer=dns.resolver.query(domain, "CNAME")
        domain_list={}
        for data in answer:
            print domain + " > "+ str(data)
        answer_list.append([domain,str(data)])
    return answer_list


def check_dns_hosts(name):
        '''
        Check up one host used for setting to what server to release
        '''

        answer=dns.resolver.query(name, "CNAME")
        for data in answer:
            resolved = str(data)

        return resolved




