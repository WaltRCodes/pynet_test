from __future__ import print_function, unicode_literals
from snmp_helper import snmp_get_oid_v3, snmp_extract
import line_graph
import time
from getpass import getpass


def get_int(devicesnmp, usersnmp, stat_type, row):
    oid_dict = {
        'in_octets':    '1.3.6.1.2.1.2.2.1.10',
        'out_octets':   '1.3.6.1.2.1.2.2.1.16',
        'in_ucast_pkts':    '1.3.6.1.2.1.2.2.1.11',
        'out_ucast_pkts':    '1.3.6.1.2.1.2.2.1.17',
    }

    if stat_type not in oid_dict.keys():
        raise ValueError("Invalid value for stat_type: {}" % stat_type)

    row = int(row)

    oid = oid_dict[stat_type]
    oid = oid + '.' + str(row)

    snmp_data = snmp_get_oid_v3(devicesnmp, usersnmp, oid)
    return int(snmp_extract(snmp_data))


def generategraph(graph_stats, sample_duration):


    print()
    x_labels = []
    for x_label in range(1, 13):
        x_labels.append(str(x_label * sample_duration))

    if line_graph.twoline("pynet-rtr1-octets.svg", "pynet-rtr1 Fa4 Input/Output Bytes",
                          graph_stats["in_octets"], "In Octets", graph_stats["out_octets"],
                          "Out Octets", x_labels):
        print("In/Out Octets graph created")

    if line_graph.twoline("pynet-rtr1-pkts.svg", "pynet-rtr1 Fa4 Input/Output Unicast Packets",
                          graph_stats["in_ucast_pkts"], "In Packets", graph_stats["out_ucast_pkts"],
                          "Out Packets", x_labels):
        print("In/Out Packets graph created")
    print()


def main():


    rtr1_ip_addr = '184.105.247.70'
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'

    usersnmp = (a_user, auth_key, encrypt_key)
    devicesnmp = (rtr1_ip_addr, 161)

    row = 5
    graph_stats = {
        "in_octets": [],
        "out_octets": [],
        "in_ucast_pkts": [],
        "out_ucast_pkts": [],
    }
    base_count_dict = {}


    SLEEP_TIME = 3
    for count in range(12):
        print()
        time_track = count * SLEEP_TIME
        print("{:>20} {:<60}".format("time", time_track))

        for entry in graph_stats.keys():
            snmp_retrieved_count = get_int(devicesnmp, usersnmp, entry, row)

            base_count = base_count_dict.get(entry)
            if base_count:

                calculated_diff = snmp_retrieved_count - base_count

                graph_stats[entry].append(calculated_diff)
                print("{:>20} {:<60}".format(entry, calculated_diff))

            base_count_dict[entry] = snmp_retrieved_count
        time.sleep(SLEEP_TIME)


    generategraph(graph_stats, sample_duration=SLEEP_TIME)


if __name__ == '__main__':
    main()
