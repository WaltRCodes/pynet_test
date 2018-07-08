from __future__ import print_function, unicode_literals
import pyeapi
import six


def output_result(output):
    return output[0]['result']


def main():
    con_establish = pyeapi.connect_to("pynet-sw2")
    interfaces = con_establish.enable("show interfaces")
    interfaces = output_result(interfaces)
    interfaces = interfaces['interfaces']
    statistics = {}
    for interface, items in interfaces.items():
        int_counters = items.get('interfaceCounters', {})
        statistics[interface] = (int_counters.get('inOctets'), int_counters.get('outOctets'))
    print("\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets"))
    for ints, octets in sorted(statistics.items()):
        print("{:20} {:<20} {:<20}".format(ints, six.text_type(octets[0]),
                                           six.text_type(octets[1])))



if __name__ == '__main__':
    main()
