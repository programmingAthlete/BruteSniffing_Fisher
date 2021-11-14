import nmap
import os
import utils.utils as include
import Setup.setup as setup
import time


class InformationGathering:

    def __str__(self):
        return 'Nmap attack'

    @staticmethod
    def run():
        scanner()


def scanner():
    """ Runs the scanner """

    slash = include.command(setup.commands, 'slash')
    directory = "data%sInformationGathering" % slash

    target = str(input('target to scan: '))
    port = str(input('port where to scan: '))
    try:
        nm_scan = nmap.PortScanner()
    except Exception as exc:
        print(f"[-] An error occorred while initiating the scan {exc}")
        time.sleep(1)
        print("Exiting the attack....")
        time.sleep(5)
        return
    try:
        nm_scanner = nm_scan.scan(target, port, arguments='-O')  # -O argument for OS finger printing
    except Exception as exc:
        print(f"[-] Incorrect host %s - {exc}" % target)
        time.sleep(2)
        print("Exiting the attack....")
        time.sleep(5)
        return
    host_is_up = "The host is : " + nm_scanner['scan'][target]['status']['state'] + '\n'
    port_is_open = "The port %s is : %s" % (port, nm_scanner['scan'][target]['tcp'][int(port)]['state']) + "\n"
    methos_scan = "The method of scanning is : " + nm_scanner['scan'][target]['tcp'][int(port)]['reason'] + "\n"

    # Checks on the existence and creation if necessary
    if not os.path.isdir(directory):
        os.system('mkdir %s' % directory)
    var = 'w'
    if os.path.isfile(directory + target + ".txt"):
        var = 'a'

    with open(directory + target + ".txt", var) as f:
        f.write('\n')
        f.write(host_is_up + port_is_open + methos_scan)
        f.write("\nReport generated " + time.strftime("%Y-%m-%d_%H:%M:%S GMT", time.gmtime()))
        f.write('\n')

    print("[+] The scan on %s and port %s completed succeffuly.\n The results are in /data/%s.txt" % (
        target, port, target))
