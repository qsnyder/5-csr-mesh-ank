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
interface1 = Interface(device=xe1)

# Letting Genie do its thing with the learn() module.  Information will be
# stored in interface.info

interface1.learn()

# We have to do a little Python magic to get inside some of the dictionaries
# But this will tell us descriptions and IP addresses of only UP interfaces
# Adding extra newline just for clarity in printing
print("")

dev1_ints = interface1.info.keys()
for intf in dev1_ints:
    if interface1.info[intf]['oper_status'] == 'up':
        ip_info = interface1.info[intf]['ipv4']
        int_key = dict.keys(ip_info)
        list_int_key = list(int_key)
        print(intf + " is up")
        print("Description: " + interface1.info[intf]['description'])
        print("IPv4 Address: " + interface1.info[intf]['ipv4'][list_int_key[0]]['ip'] + "/" + interface1.info[intf]['ipv4'][list_int_key[0]]['prefix_length'])
        print()
