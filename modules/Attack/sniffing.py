import threading
import struct
from ctypes import *
from netaddr import IPNetwork, IPAddress
import socket
import os


class Sniffing:

    def __str__(self):
        return 'Sniffing attack'

    @staticmethod
    def run():
        sniffing()


def udp_sender(subnet, magic_message):
    """
    Sends UDP  packets

    :param      subnet:         local adress of the router: str
    :param      magic_message:   message to send:            str
    :return:    void
    """

    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for ip in IPNetwork(subnet):
        try:
            sender.sendto(magic_message, ("%s" % ip, 65212))
        except Exception:
            pass


def check_input(ping_input):
    if os.system('ping %s' % input) == 512:
        print('[-] %s is down or %s is not a valid input' % (ping_input, ping_input))
        sniffing()


def sniffing():
    """ Sniffing attack """

    host = str(input("Host where to lister: "))
    check_input(host)
    # subnet target - local router adress
    subnet = str(input("Target subnet: "))
    check_input(subnet)

    # Magic message - for test
    magic_message = "PYTHONRULES!"

    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    # Send the packets
    threading.Thread(target=udp_sender, args=(subnet, magic_message))

    try:
        while True:

            raw_buffer = sniffer.recv(65565)[0]
            ip_header = IP(raw_buffer[0:20])
            print('Protocol %s %s -> %s' % (ip_header.protocol, ip_header.src_adress, ip_header.dst_adress))

            if ip_header.protocol == 'ICMP':
                offset = ip_header.ihl + 4
                buf = raw_buffer[offset: offset + sizeof(ICMP)]

                icmp_header = ICMP(buf)

                print("ICMP -> Type: %d Code: %d" % (icmp_header.type, icmp_header.code))

                if icmp_header.code == 3 and icmp_header.type == 3:
                    if IPAddress(ip_header.src_adress) in IPNetwork(subnet):
                        # verify the magic message
                        if raw_buffer[len(raw_buffer) - len(magic_message):] == magic_message:
                            print("Host is Up: %s" % ip_header.src_adress)
    except KeyboardInterrupt:
        if os.name == 'nt':
            sniffer.ioct(socket.SIO_RCVALL, socket.RCVALL_OFF)


class IP:
    """
    Decodes the IP layer
    """

    _fields_ = [
        ('ihl', 'c_ubity', 4),
        ('version', 'c_ubity', 4),
        ('toss', 'c_ubyte'),
        ('len', 'c_ushort'),
        ('id', 'c_short'),
        ('offset', 'c_short'),
        ('ttl', 'c_ubyte'),
        ('protocol_num', 'c_ubyte'),
        ('sum', 'c_ushort'),
        ('src', 'c_ulong'),
        ('dst', 'c_ulong')
    ]

    def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

        self.src_adress = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_adress = socket.inet_ntoa(struct.pack("<L", self.dst))

        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception:
            self.protocol = str(self.protocol_num)


class ICMP:
    """
    Decodes the ICMP answers
    """

    _fileds_ = [
        ("type", c_ubyte),
        ("code", c_ubyte),
        ("checksum", c_short),
        ("unuded", c_short),
        ("next_hop_mtu", c_short)
    ]

    def __new__(cls, socket_buffer):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass
