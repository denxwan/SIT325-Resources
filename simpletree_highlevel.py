#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet

#default values
n_value = int(1) 
aggregationSwitches = []
edgeSwitches = []
hosts = []
temp_var = 0


class Tree_Topology ( Topo ):
	def __init__( self ):
		Topo.__init__(self)
		
		#Core switch
		for i in range(int(n_value)**0):
			coreSwitch = self.addSwitch('c1')
			
		#Aggregation switches
		for i in range(int(n_value)**1):
			aggregationSwitches.append(i)
			aggregationSwitches[i] = self.addSwitch(f's{i+1}') 
			
			self.addLink(aggregationSwitches[i], coreSwitch)
			
		#Edge switches
		for i in range(int(n_value)**2):
			edgeSwitches.append(i)
			edgeSwitches[i] = self.addSwitch(f'e{i+1}')
			
				
		#Hosts
		for i in range(int(n_value)**3):
			hosts.append(i)
			hosts[i] = self.addHost(f'h{i+1}')
			
		#Linking edge switches to aggregation switches
		temp_var = 0
		for i in range(int(n_value)**1): #-->2
			for j in range(temp_var, temp_var+(int(n_value)**1)):
				self.addLink(aggregationSwitches[i], edgeSwitches[j])
			temp_var += int(n_value)**1
			
		#Linking hosts to edge switches
		temp_var = 0
		for i in range(int(n_value)**2): #-->4
			for j in range(temp_var, (temp_var+int(n_value)**1)):
				self.addLink(edgeSwitches[i], hosts[j])
			
			temp_var += (int(n_value)**1)
	
def treeAutomation(n_value):
	topo = Tree_Topology()
	net = Mininet(topo)
	#Staring the topology
	net.start()
	
	#Printing detailed connectivity of the network
	print(net.hosts)
	
	#Pinging all nodes
	net.pingAll()
	
	#Stopping the script
	net.stop()
	
if __name__ == '__main__':
	n_value = input("Enter n value: ")
	treeAutomation(n_value)
	
