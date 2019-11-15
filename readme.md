SuperNova

Python 3 based network configuration automation, change analyser and validator.
PyATS and Genie based library for parsing multi vendor/platform devices. Tested and Supports NXOS, IOS, IOS-XE, JUNOS.
Inventory file lists Cisco Always On Sandbox devices to test the codes out of box and make manupulaitons.
Realworld testing made on network running 300+ devices.


Use NAPALM library for adding support to devices at https://napalm.readthedocs.io/en/latest/support/

File Explanations

__main__.py           >       Primary Codes. Imports Genie/PyATS and other Libraries. analyse import is for function imports from analyse.py running core configuration gathering functions irrespective of ventor/OS.
inventory.yaml        >       YAML file specifing devices to be inspected. Can be converted from csv using online tools or native python scripts. As example contain device logins of Cisco Always On Sandboxes.
analyse.py            >       Functions called in __main__.py for aquiring various command outputs parsed as dictionary, handles multi vendor output into common frame.


Installation

** Python 3.7 Virtual Environment
pip install -r requirements.txt
** For first time run, the code needs to collect golden states of the devices or states when the network the is considered all good.
** Run with -golden = True flag to enable gathering of golden configurations.
python __main__.py golden = True inventory = inventory.yaml
** Post Golden State aquisition, run code at set interval to detect around 10 parameter changes including configuraiton or dynamic routing changes.
** Additional functions can be added to suit needs.
