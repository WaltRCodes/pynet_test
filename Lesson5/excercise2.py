from __future__ import unicode_literals, print_function
import pyeapi
import argparse
import six

def output_result(output):
    return output[0]['result']


def sh_vlan_check(eapi_conn, vlan_id):
    vlan_id = six.text_type(vlan_id)
    cmd = 'show vlan id {}'.format(vlan_id)
    try:
        response = eapi_conn.enable(cmd)
        check_vlan = output_result(response)['vlans']
        return check_vlan[vlan_id]['name']
    except (pyeapi.eapilib.CommandError, KeyError):
        pass
    return False


def config_vlan(eapi_conn, vlan_id, vlan_name=None):
    string1 = 'vlan {}'.format(vlan_id)
    cmd = [string1]
    if vlan_name is not None:
        string2 = 'name {}'.format(vlan_name)
        cmd.append(string2)
    return eapi_conn.config(cmd)


def main():
    eapi_conn = pyeapi.connect_to("pynet-sw2")
    parser = argparse.ArgumentParser(
        description="Idempotent addition/removal of VLAN to Arista switch"
    )
    parser.add_argument("vlan_id", help="VLAN number to create or remove", action="store", type=int)
    parser.add_argument(
        "--name",
        help="Specify VLAN name",
        action="store",
        dest="vlan_name",
        type=str
    )
    parser.add_argument("--remove", help="Remove the given VLAN ID", action="store_true")

    cli_args = parser.parse_args()
    vlan_id = cli_args.vlan_id
    remove = cli_args.remove
    vlan_name = six.text_type(cli_args.vlan_name)

    check_vlan = sh_vlan_check(eapi_conn, vlan_id)

    if remove:
        if check_vlan:
			try:
				question = raw_input("VLAN exists, are you sure you want to remove?[Y/N]")
			except NameError:
				question = input("VLAN exists, are you sure you want to remove?[Y/N]")
				
			if (question == "y" or  question == "Y"):
				print("OK, removing it")
				command_str = 'no vlan {}'.format(vlan_id)
				eapi_conn.config([command_str])
        else:
            print("VLAN does not exist, no action required")
    else:
        if check_vlan:
            if vlan_name is not None and check_vlan != vlan_name:
                print("VLAN already exists, setting VLAN name")
                config_vlan(eapi_conn, vlan_id, vlan_name)
            else:
                print("VLAN already exists, no action required")
        else:
            print("Adding VLAN including vlan_name (if present)")
            config_vlan(eapi_conn, vlan_id, vlan_name)


if __name__ == "__main__":
    main()
