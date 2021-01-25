import nmap
import time
import Includes.includes as include
import Setup.setup as setup
import time

class InformationGathering:

    def __str__():
        return 'Nmap attack'

    def run():
        scanner()


def scanner():
    ''' Runs the scanner '''

    slash = include.command(setup.commands, 'slash')
    dir = "data%sInformationGathering" % slash

    target = str(input('target to scan: '))
    port = str(input('port where to scan: '))
    try:
        nm_scan = nmap.PortScanner()
    except:
        print("[-] An error occorred while initiating the scan")
        time.sleep(1)
        print("Exiting the attack....")
        time.sleep(5)
        return
    try:
        nm_scanner = nm_scan.scan(target, port, arguments='-O')  # -O argument for OS finger printing
    except:
        print("[-] Incorrect host %s" % target)
        time.sleep(2)
        print("Exiting the attack....")
        time.sleep(5)
        return
    host_is_up = "The host is : " + nm_scanner['scan'][target]['status']['state'] + '\n'
    port_is_open = "The port %s is : %s" % (port, nm_scanner['scan'][target]['tcp'][int(port)]['state']) + "\n"
    methos_scan = "The method of scanning is : " + nm_scanner['scan'][target]['tcp'][int(port)]['reason'] + "\n"

    # Checks on the existence and craeation if necessary
    if os.path.isdir(dir) == False:
        os.system('mkdir %s' % dir)
    var = 'w'
    if os.path.isfile(dir + target + ".txt"):
        var = 'a'

    with open(dir + target + ".txt", var) as f:
        f.write('\n')
        f.write(host_is_up + port_is_open + methos_scan)
        f.write("\nReport generated " + time.strftime("%Y-%m-%d_%H:%M:%S GMT", time.gmtime()))
        f.write('\n')

    print("[+] The scan on %s and port %s completed succeffuly.\n The results are in /data/%s.txt" %(target, port, target))
