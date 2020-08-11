from builtins import range
import socket
import struct
from socket import inet_ntoa
from struct import pack


def ip2long(ip):
    return struct.unpack("!L", socket.inet_aton(ip))[0]


def long2ip(value):
    return socket.inet_ntoa(struct.pack('!L', value))


def calc_range_int(ip, netmask):
    start = long2ip(ip2long(ip) & ip2long(netmask))
    end = long2ip(ip2long(ip) | (~ip2long(netmask) + (1 << 32)))
    return start, end


def cidr2dot(mask):
    bits = 0
    for i in range(32 - mask, 32):
        bits |= (1 << i)
    return inet_ntoa(pack('>I', bits))
