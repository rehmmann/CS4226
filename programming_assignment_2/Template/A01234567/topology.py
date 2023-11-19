import atexit

from mininet.cli import CLI
from mininet.link import Link
from mininet.log import info, setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from router import FRRRouter

net = None


class Topology(Topo):
    def build(self):
    
        # Add routers
        self.addHost('r110', cls=FRRRouter, asn=100, loopback="100.100.1.1/32")
        self.addHost('r120', cls=FRRRouter, asn=100, loopback="100.100.1.2/32")
        self.addHost('r130', cls=FRRRouter, asn=100, loopback="100.100.1.3/32")
        self.addHost('r210', cls=FRRRouter, asn=200, loopback="100.100.2.1/32")
        self.addHost('r310', cls=FRRRouter, asn=300, loopback="100.100.3.1/32")
        self.addHost('r410', cls=FRRRouter, asn=400, loopback="100.100.4.1/32")
        
        # Add switches 
        # s120 = self.addSwitch('s120')
        # s130 = self.addSwitch('s130')
        # s210 = self.addSwitch('s210')
        # s310 = self.addSwitch('s310')
        # s410 = self.addSwitch('s410')
       
        # Add hosts
        self.addHost('h211', ip="10.2.1.1/24")
        self.addHost('h311', ip="10.3.1.1/24")
        self.addHost('h411', ip="10.4.1.1/25")
        self.addHost('h412', ip="10.4.1.129/25")
        
        # Link hosts to routers
        self.addLink('r210', 'h211')
        self.addLink('r410', 'h412')
        self.addLink('r410', 'h411')
        self.addLink('r310', 'h311')

        # Link Routers
        self.addLink('r210', 'r110')
        self.addLink('r110', 'r120')
        self.addLink('r110', 'r410')
        self.addLink('r120', 'r130')
        self.addLink('r410', 'r130')
        self.addLink('r130', 'r310')


        # self.addLink(r110, s120)
        # self.addLink(r120, s120)
        
        # self.addLink(r120, s130)
        # self.addLink(r130, s130)
        
        # self.addLink(r210, s210)
        # self.addLink(h211, s210)
        
        # self.addLink(r310, s310) 
        # self.addLink(h311, s310)
        
        # self.addLink(r410, s410)
        # self.addLink(h411, s410)
        # self.addLink(h412, s410)
       
        # Set IP addresses  
        # r110.setIP('r110-eth0', '192.168.1.0/31')
        # r120.setIP('r120-eth0', '192.168.1.1/31')
        
        # h211.setIP('h211-eth0', '10.2.1.1/24')
        # r210.setIP('r210-eth0', '10.2.1.254/24')
        
        # ... Configure other IPs
        
        # r110.configDefault()
        # r120.configDefault()
        # ... Configure default routes


def startNetwork():
    info("*** Creating the network\n")
    topology = Topology()

    global net
    net = Mininet(topo=topology, link=Link, autoSetMacs=True)

    info("*** Starting the network\n")
    net.start()
    info("*** Running CLI\n")
    CLI(net)


def stopNetwork():
    if net is not None:
        net.stop()


if __name__ == "__main__":
    # Force cleanup on exit by registering a cleanup function
    atexit.register(stopNetwork)

    # Tell mininet to print useful information
    setLogLevel("info")
    startNetwork()
