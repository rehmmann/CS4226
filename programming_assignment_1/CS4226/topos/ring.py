#!/usr/bin/python

import os, sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from mininet.node import Host, RemoteController

class TreeTopo( Topo ):
    "Tree topology"

    def build( self ):
        # Read ring.in
        # Load configuration of Hosts, Switches, and Links
        # You can write other functions as you need.

        # Add hosts
        # > self.addHost('h%d' % [HOST NUMBER])

        # Add switches
        # > sconfig = {'dpid': "%016x" % [SWITCH NUMBER]}
        # > self.addSwitch('s%d' % [SWITCH NUMBER], **sconfig)

        # Add links
        # > self.addLink([HOST1], [HOST2])
        with open('ring.in', 'r') as f:
            lines = f.readlines()
        
        num_hosts,num_switches,num_links = map(int,lines[0].split())

        #Add hosts
        for i in range(1,num_hosts+1):
            self.addHost('h%d' % i)


        #Add switches
        for i in range(1,num_switches+1):
            sconfig = {'dpid': "%016x" % i}
            self.addSwitch('s%d' % i, **sconfig)
        
        #Add links
        for line in lines[1:]:
            h1,h2 = line.rstrip('\n').split(',')
            self.addLink(h1,h2)
        
                    
topos = { 'sdnip' : ( lambda: TreeTopo() ) }

if __name__ == '__main__':
    sys.path.insert(1, '/home/sdn/onos/topos')
    from onosnet import run
    run( TreeTopo() )