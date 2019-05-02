from genie.conf import Genie
from genie.libs.ops.interface.iosxe.interface import Interface

# Load Genie testbed
testbed = Genie.init(testbed="default_testbed.yaml")

# Map all testbed devices to aliases for easy reference
xe1 = testbed.devices['csr1000v-1']
xe2 = testbed.devices['csr1000v-2']
xe3 = testbed.devices['csr1000v-3']
xe4 = testbed.devices['csr1000v-4']
xe5 = testbed.devices['csr1000v-5']

# Just connect to the first device for initial testing
xe1.connect()

xe1.configure('''\
interface {intf}
 description AUTOMATED LOOPBACK CONFIG
 ip address 1.1.1.1 255.255.255.255
 no shut'''.format(intf='loopback1'))
