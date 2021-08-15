from itertools import product
import random
import nmap3
import json
import argparse


# TODO: Store results in an organized json file, and if process is terminated without finishing, next run will skip former results.
class nmapRandom:
    def __init__(self):
        self.ip_list = []
        self.common_port_list = []
        self.big_port_list = list(range(1,65535))
        self.random_combinations = []
    def ip_port_list_import(self):
        with open("ip_list.txt", "r") as ip_file:
            self.ip_list = [line.rstrip() for line in ip_file]
            self.ip_list = list(dict.fromkeys(self.ip_list))
            ip_file.close()
        with open("common_1000_ports.txt", "r") as ports_file:
            content = ports_file.read()
            self.common_port_list = content.split(",")
            ports_file.close()


    def randomaizer(self, is_heavy):
        myClass.ip_port_list_import()
        if is_heavy:
            # all ports scan
            combinations = [(a, b) for a in self.ip_list for b in self.big_port_list]
        else:
            # 1000 common ports scan
            combinations = [(a, b) for a in self.ip_list for b in self.common_port_list]
        self.random_combinations = random.sample(combinations, len(combinations))


    def nmap_scan(self):

        for i in self.random_combinations:
            nmap = nmap3.Nmap()
            ip = i[0]
            port = i[1]
            results = nmap.scan_top_ports(ip, args='-p' + port)
            result_ports = results[ip]['ports']
            for i in result_ports:
                if i['state'] == 'open':
                    print(ip + ':' + i['portid'] + ' open')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script that randomize ports and ips in nmap scan.')
    parser.add_argument('--heavy',action='store_true', help='if used. nmap will scan all ports for all ip\'s, if not \n'
                                                            'nmap will scan only top ports.')
    args = parser.parse_args()

    myClass = nmapRandom()
    if args.heavy:
        myClass.randomaizer(True)
    else:
        myClass.randomaizer(False)
    myClass.nmap_scan()