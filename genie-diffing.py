import pprint
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

# Instantiate the OPS object for the single connected device
interface1 = Interface(name='GigabitEthernet5', device=xe1)

interface1.learn()

# Let's modify one of the interface, so we can demonstrate the comparison

xe1.configure('''\
interface {intf}
 shut'''.format(intf='GigabitEthernet5'))

# let's take a new snapshot now and compare
interface1_after = Interface(name='GigabitEthernet5', device=xe1)

interface1_after.learn()


pprint.pprint(interface1.info)
diff = interface1_after.diff(interface1)
print("")
print("=" * 20)
print(diff)
print("=" * 20)
print("")

# Lets return to steady state
xe1.configure('''\
interface {intf}
 no shut'''.format(intf='GigabitEthernet5'))
