# README #

This README would normally document whatever steps are necessary to get your application up and running.

### How do I get set up? ###
* Some system has limit on number of open files, to increase the limist: ulimit -n 8192
* http://www.commercialventvac.com/dpkt.html#mozTocId363973
* ubuntu: apt-get install libpcap-dev python-dev tshark
* centos:
*   yum install gcc libpcap-devel libxslt-devel python-devel wireshark
*   yum install python-virtualenv
* Windows pypcap and lxml:
*	http://stackoverflow.com/questions/36515474/installing-pypcap-on-windows-10-python-2-7-64-bit
*	set INCLUDE=%INCLUDE%;c:\WpdPack\Include
*	set LIB=%LIB%;c:\WpdPack\Lib
*	wheel install libs\lxml-3.7.1-cp27-cp27m-win32.whl --force
* pip install futures pypcap pyshark netaddr netifaces
