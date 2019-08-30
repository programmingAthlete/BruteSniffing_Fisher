import nmap
import time

def scanner():
    ''' Runs the scanner '''

    slash = include.command(commands, 'slash')
    dir = "data%sInformationGathering" % slash

    target = str(input('target to scan: '))
    port = int(input('port where to scan: '))

    nm_scan = nmap.PortScanner()

    nm_scanner = nm_scan.scan(target, port, arguments='-O')  # -O argument for OS finger printing

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

