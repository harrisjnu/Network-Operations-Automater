
####            Project SuperNova           ####

##Support Library Calls
#Generic Libraries
import sys
import argparse
import logging
import pickle

#Specific Libraries
from pyats.log.utils import banner
from pyats.topology import loader
from genie.conf import Genie
from genie.utils.diff import Diff
# from genie.libs.parser.utils import get_parser_exclude
# from genie.ops.base import Base
import genie
import pyats

# Logging Engine Load
# Swap Logging Statement for detailed log views.
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='(%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d]),\n %(message)s')
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='(%(message)s')
log = logging.getLogger(__name__)

##Function Library Calls
import analyse


parser = argparse.ArgumentParser()
parser.add_argument('-inventory', help="Set -inventory /File/Name to input device to be probed")
parser.add_argument('-parse', help="Set -parse True to parse device configurations")
parser.add_argument('-golden', help="Set -golden True to refresh stored data")
args = parser.parse_args()

parse = args.parse
golden = args.golden
inventory = args.inventory

# Default value for configuration parsing is false
if parse is None:
    parse = True
# Default value for Golden Data refresh is false
if golden is None:
    golden = False

## GOLDEN CONFIG PREVENTION HOLD
if golden:
    log.info(banner("User has commanded to rewrite the Golden States for all devices ... \n Prompting User for Confirmation " + "\n"))
    print("Are you sure of rebuilding the Golden Configs ? This action is irreversible")
    print("Type YES to Continue, Press any key to stop.!!!!")
    user_input = input()
    if user_input != "YES":
        sys.exit()
    else:
        pass

## Load Inventory
log.debug(banner("Loading Inventory Data"))
#inventory = pyats.topology.loader.load("inventory.yaml")
inventory = pyats.topology.loader.load(inventory)
log.debug("\nPASS: Loaded Inventory Data '{}'\n".format(inventory.name))
inventory = genie.conf.Genie.init(inventory)

## Inventory Connectivity Loop
for name,dev in inventory.devices.items():
    dev.connect()
    log.debug("\n Connecting to '{}'\n".format(dev))
    if dev.is_connected():
        log.debug("\n Connected to '{}'\n".format(dev))
    else:
        dev.connect()
        log.debug("\n Connecting to '{}'\n".format(dev))

    if parse == True:
        log.info(banner("Executing Parsers on '{}'\n".format(name)))
        # Retrieving Current Configurations
        try:
            current_config = analyse.get_generic.config(dev)
            log.debug("\nRetrieving Configuration Details")
            if golden:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_CONFIG_" + str(name) + ".pickle"
            else:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_CONFIG_" + str(
                    name) + ".pickle"
            with open(file_name, 'wb') as f:
                pickle.dump(current_config, f, protocol=pickle.HIGHEST_PROTOCOL)
                log.debug("\nCurrent config for '{}' .......... Parsed and saved to file '{}'".format(name, f.name))
        except:
            log.info("\nConfig extraction failed for '{}'".format(name,f.name))
            current_config = None
            pass
        #with open("CURRENT_CONFIG_" + str(name) + ".pickle",'wb') as f:


        # # Retrieving CDP Neighbors
        try:
            current_cdp_neighbors = analyse.get_generic.cdp(dev)
            log.debug("\nRetrieving current CDP Neighborhood Details")
            if golden:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_CDP_" + str(name) + ".pickle"
            else:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_CDP_" + str(name) + ".pickle"
            with open(file_name, 'wb') as f:
                pickle.dump(current_cdp_neighbors, f, protocol=pickle.HIGHEST_PROTOCOL)
                log.debug(
                    "\nCurrent CDP Neighborhood for '{}' .......... Parsed and saved to file '{}'".format(name, f.name))
        except:
            log.info("\nCDP extraction failed for '{}'".format(name,f.name))
            current_cdp_neighbors = None
            pass
        #with open("CURRENT_CDP_" + str(name) + ".pickle",'wb') as f:


        # # Retrieving Environmental Conditions
        try:
            current_environment = analyse.get_generic.environment(dev)
            log.debug("\nRetrieving current environment details")
            if golden:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_ENVIRONMENT_" + str(
                    name) + ".pickle"
            else:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_ENVIRONMENT_" + str(
                    name) + ".pickle"
            with open(file_name, 'wb') as f:
                pickle.dump(current_environment, f, protocol=pickle.HIGHEST_PROTOCOL)
                log.debug(
                    "\nCurrent environment for '{}' .......... Parsed and saved to file '{}'".format(name, f.name))
        except:
            log.info("\nEnvironment Conditions extraction failed for '{}'".format(name,f.name))
            current_environment = None
            pass

        # with open("CURRENT_CDP_" + str(name) + ".pickle",'wb') as f:


        # Retrieving Current Inventory
        try:
            current_inventory = analyse.get_generic.inventory(dev)
            log.debug("\nRetrieving current inventory details")
            if golden:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_INVENTORY_" + str(
                    name) + ".pickle"
            else:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_INVENTORY_" + str(
                    name) + ".pickle"
            with open(file_name, 'wb') as f:
                pickle.dump(current_inventory, f, protocol=pickle.HIGHEST_PROTOCOL)
                log.debug("\nCurrent inventory for '{}' .......... Parsed and saved to file '{}'".format(name, f.name))
        except:
            log.info("\nInventory extraction failed for '{}'".format(name,f.name))
            current_inventory = None
            pass

        # with open("CURRENT_CDP_" + str(name) + ".pickle",'wb') as f:

        # # Retrieving Current Stack Power
        try:
            current_stackpower = analyse.get_generic.stackpower(dev)
            log.debug("\nRetrieving current stack power details")
            if golden:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_STACKPOWER_" + str(
                    name) + ".pickle"
            else:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_STACKPOWER_" + str(
                    name) + ".pickle"
            with open(file_name, 'wb') as f:
                pickle.dump(current_stackpower, f, protocol=pickle.HIGHEST_PROTOCOL)
                log.debug(
                    "\nCurrent stack power for '{}' .......... Parsed and saved to file '{}'".format(name, f.name))

        except:
            log.info("\nStackPower extraction failed for '{}'".format(name,f.name))
            current_stackpower = None
            pass
        # with open("CURRENT_CDP_" + str(name) + ".pickle",'wb') as f:


        # # Retrieving Interface Brief
        try:
            current_interface_brief = analyse.get_interface.brief(dev)
            log.debug("\nRetrieving Current Interfaces Brief...")
            if golden:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_INTERFACE-BRIEF_" + str(
                    name) + ".pickle"
                print(file_name)
            else:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_INTERFACE-BRIEF_" + str(
                    name) + ".pickle"
            with open(file_name, 'wb') as f:
                pickle.dump(current_interface_brief, f, protocol=pickle.HIGHEST_PROTOCOL)
                log.debug(
                    "\nCurrent Interface Status of '{}' .......... Parsed and saved to file '{}'".format(name, f.name))
        except:
            log.info("\nInterface Brief failed for '{}'".format(name,f.name))
            current_interface_brief = None
            pass
        # with open("CURRENT_CDP_" + str(name) + ".pickle",'wb') as f:


        # # Retrieving LLDP Neigbours
        try:
            current_lldp = analyse.get_interface.lldp(dev)
            log.debug("\nRetrieving Current LLDP Status...")
            if golden:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_LLDP_" + str(name) + ".pickle"
            else:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_LLDP_" + str(name) + ".pickle"
            with open(file_name, 'wb') as f:
                pickle.dump(current_lldp, f, protocol=pickle.HIGHEST_PROTOCOL)
                log.debug("\nCurrent LLDP Status of '{}' .......... Parsed and saved to file '{}'".format(name, f.name))

        except:
            log.info("\nLLDP extraction failed for '{}'".format(name,f.name))
            current_lldp = None
            pass
        # with open("CURRENT_CDP_" + str(name) + ".pickle",'wb') as f:


        # # Retrieving STP STATUS
        try:
            current_stp = analyse.get_interface.stp(dev)
            log.debug("\nRetrieving Current STP Status...")
            if golden:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_STP_" + str(name) + ".pickle"
            else:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_STP_" + str(name) + ".pickle"
            with open(file_name, 'wb') as f:
                pickle.dump(current_stp, f, protocol=pickle.HIGHEST_PROTOCOL)
                log.debug("\nCurrent STP Status of '{}' .......... Parsed and saved to file '{}'".format(name, f.name))
        except:
            log.info("\nSTP STATUS extraction failed for '{}'".format(name,f.name))
            current_stp = None
            pass
        # with open("CURRENT_CDP_" + str(name) + ".pickle",'wb') as f:



        # # Retrieving Routing Status
        try:
            current_routes = analyse.get_interface.routing(dev)
            log.debug("\nRetrieving Current STP Status...")
            if golden:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_ROUTE_" + str(name) + ".pickle"
            else:
                file_name = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_ROUTE_" + str(name) + ".pickle"
            with open(file_name, 'wb') as f:
                pickle.dump(current_routes, f, protocol=pickle.HIGHEST_PROTOCOL)
                log.debug(
                    "\nCurrent Routing Status of '{}' .......... Parsed and saved to file '{}'".format(name, f.name))

        except:
            log.info("\nRouting extraction failed for '{}'".format(name,f.name))
            current_routes = None
            pass
        # with open("CURRENT_CDP_" + str(name) + ".pickle",'wb') as f:

    dev.disconnect()

###### Program break if in Golden Config Learning Mode

if golden:
    log.info(banner("Executed in Golden State Absorption Mode... SYS EXIT NOW"))
    sys.exit()
else:
    pass

# Device Data Parsing and Learning End
# Differentiate Logic Block
## CONFIG PARSER DIFF ENGINE
for name, dev in inventory.devices.items():
    log.info(banner("RUNNING CONFIGURATION PARSER DIFF ENGINE '{}'".format(name)))

    ## Running Config Diffs
    try:
        pre_config = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_CONFIG_" + str(name) + ".pickle"
        with open(pre_config,'rb') as pre_config:
            pre_config = pickle.load(pre_config)
        post_config = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_CONFIG_" + str(name) + ".pickle"
        with open(post_config,'rb') as post_config:
            post_config = pickle.load(post_config)
        diff_config: Diff = Diff(pre_config,post_config)
        diff_config.findDiff()
        log.debug("DIFFERENTIATION COMPLETED FOR CONFIG")
        if str(diff_config) is "":
            log.info(banner("NO CONFIGURATION CHANGES BY ANALYSER FOR '{}'".format(name)))
        else:
            log.info(banner("CONFIGURATION CHANGE BY ANALYSER FOR '{}'".format(name)))
            print(diff_config)
    except:
        log.info(banner("NO CONFIGURATION PARAMETERS AVAILABLE FOR '{}'".format(name)))
        pass



    ## Running CDP Diffs
    try:
        pre_cdp = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_CDP_" + str(name) + ".pickle"
        with open(pre_cdp,'rb') as pre_cdp:
            pre_cdp = pickle.load(pre_cdp)
        post_cdp = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_CDP_" + str(name) + ".pickle"
        with open(post_cdp,'rb') as post_cdp:
            post_cdp = pickle.load(post_cdp)
        diff_cdp = Diff(pre_cdp,post_cdp,exclude="hold_time")
        diff_cdp.findDiff()
        log.debug("DIFFERENTIATION COMPLETED FOR CDP - PARSER")
        if str(diff_cdp) is "":
            log.info(banner("NO CDP CHANGES BY ANALYSER FOR '{}'".format(name)))
        else:
            log.info(banner("CDP CHANGE BY ANALYSER FOR '{}'".format(name)))
            print(diff_cdp)
    except:
        log.info(banner("NO CDP PARAMETERS AVAILABLE FOR '{}'".format(name)))
        pass

    ## Running Environmental Conditions Diffs
    try:
        pre_env = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_ENVIRONMENT_" + str(name) + ".pickle"
        with open(pre_env,'rb') as pre_env:
            pre_env = pickle.load(pre_env)
        post_env = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_ENVIRONMENT_" + str(name) + ".pickle"
        with open(post_env,'rb') as post_env:
            post_env = pickle.load(post_env)
        diff_env = Diff(pre_env,post_env)
        diff_env.findDiff()
        log.debug("DIFFERENTIATION COMPLETED FOR ENVIRONMENTAL CONDITIONS - PARSER")
        if str(diff_env) is "":
            log.info(banner("NO ENVIRONMENTAL CHANGES BY ANALYSER FOR '{}'".format(name)))
        else:
            log.info(banner("ENVIRONMENTAL CHANGES BY ANALYSER FOR '{}'".format(name)))
            print(diff_env)
    except:
        log.info(banner("NO ENVIRONMENT PARAMETERS AVAILABLE FOR '{}'".format(name)))
        pass

    ## Running Inventory Diffs
    try:
        pre_inventory = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_INVENTORY_" + str(name) + ".pickle"
        with open(pre_inventory, 'rb') as pre_inventory:
            pre_inventory = pickle.load(pre_inventory)
        post_inventory = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_INVENTORY_" + str(name) + ".pickle"
        with open(post_inventory, 'rb') as post_inventory:
            post_inventory = pickle.load(post_inventory)
        diff_inventory = Diff(pre_inventory,post_inventory)
        diff_inventory.findDiff()
        log.debug("DIFFERENTIATION COMPLETED FOR INVENTORY - PARSER")
        if str(diff_inventory) is "":
            log.info(banner("NO INVENTORY CHANGES BY ANALYSER FOR '{}'".format(name)))
        else:
            log.info(banner("INVENTORY CHANGES BY ANALYSER FOR '{}'".format(name)))
            print(diff_inventory)
    except:
        log.info(banner("NO INVENTORY PARAMETERS AVAILABLE FOR '{}'".format(name)))
        pass



    ## Running Power Consumption  Diffs
    try:
        pre_power = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_STACKPOWER_" + str(name) + ".pickle"
        with open(pre_power, 'rb') as pre_power:
            pre_power = pickle.load(pre_power)
        post_power = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_STACKPOWER_" + str(name) + ".pickle"
        with open(post_power, 'rb') as post_power:
            post_power = pickle.load(post_power)
        diff_power = Diff(pre_power,post_power)
        diff_power.findDiff()
        log.debug("DIFFERENTIATION COMPLETED FOR POWER CONDITIONS - PARSER")
        if str(diff_power) is "":
            log.info(banner("NO POWER CONSUMPTION CHANGES BY ANALYSER FOR '{}'".format(name)))
        else:
            log.info(banner("POWER CONSUMPTION CHANGES BY ANALYSER FOR '{}'".format(name)))
            print(diff_power)
    except:
        log.info(banner("NO POWER PARAMETERS AVAILABLE FOR '{}'".format(name)))
        pass

    ## Running Interface Brief Diffs
    try:
        pre_interface_brief = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_INTERFACE-BRIEF_" + str(name) + ".pickle"
        with open(pre_interface_brief,'rb') as pre_interface_brief:
            pre_interface_brief = pickle.load(pre_interface_brief)
        post_interface_brief = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_INTERFACE-BRIEF_" + str(name) + ".pickle"
        with open(post_interface_brief,'rb') as post_interface_brief:
            post_interface_brief = pickle.load(post_interface_brief)
        diff_interface_brief = Diff(pre_interface_brief,post_interface_brief)
        #diff_interface = Diff(pre_interface,post_interface,exclude=get_parser_exclude('show ipv6 interface', dev))
        diff_interface_brief.findDiff()
        log.debug("DIFFERENTIATION COMPLETED FOR INTERFACE - PARSER")
        if str(diff_interface_brief) is "":
            log.info(banner("NO INTERFACE CHANGES FOR '{}'".format(name)))
        else:
            log.info(banner("INTERFACE CHANGES FOR '{}'".format(name)))
            print(diff_interface_brief)
    except:
        log.info(banner("NO INTERFACE PARAMETERS AVAILABLE FOR '{}'".format(name)))
        pass



    ## Running LLDP Diffs
    try:
        pre_lldp = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_LLDP_" + str(name) + ".pickle"
        with open(pre_lldp, 'rb') as pre_lldp:
            pre_lldp = pickle.load(pre_lldp)
        post_lldp = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_LLDP_" + str(name) + ".pickle"
        with open(post_lldp, 'rb') as post_lldp:
            post_lldp = pickle.load(post_lldp)
        diff_lldp = Diff(pre_lldp,post_lldp,exclude="time_remaining")
        # diff_interface = Diff(pre_interface,post_interface,exclude=get_parser_exclude('show ipv6 interface', dev))
        diff_lldp.findDiff()
        log.debug("DIFFERENTIATION COMPLETED FOR LLDP - PARSER")
        if str(diff_lldp) is "":
            log.info(banner("NO LLDP CHANGES FOR '{}'".format(name)))
        else:
            log.info(banner("LLDP CHANGES FOR '{}'".format(name)))
            print(diff_lldp)
    except:
        log.info(banner("NO LLDP PARAMETERS AVAILABLE FOR '{}'".format(name)))
        pass


    ## Running STP Diffs
    try:
        pre_stp = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_STP_" + str(name) + ".pickle"
        with open(pre_stp, 'rb') as pre_stp:
            pre_stp = pickle.load(pre_stp)
        post_stp = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_STP_" + str(name) + ".pickle"
        with open(post_stp, 'rb') as post_stp:
            post_stp = pickle.load(post_stp)
        diff_stp = Diff(pre_stp,post_stp)
        # diff_interface = Diff(pre_interface,post_interface,exclude=get_parser_exclude('show ipv6 interface', dev))
        diff_stp.findDiff()
        log.debug("DIFFERENTIATION COMPLETED FOR STP - PARSER")
        if str(diff_stp) is "":
            log.info(banner("NO STP CHANGES FOR '{}'".format(name)))
        else:
            log.info(banner("STP CHANGES FOR '{}'".format(name)))
            print(diff_stp)
    except:
        log.info(banner("NO STP PARAMETERS AVAILABLE FOR '{}'".format(name)))
        pass


    ## Running Routing Diffs
    try:
        pre_routes = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "GOLDEN_ROUTE_" + str(name) + ".pickle"
        with open(pre_routes, 'rb') as pre_routes:
            pre_routes = pickle.load(pre_routes)
        post_routes = '/Pylab/Robotix/codes/SuperNova/Fly_Data_Parsed/' + "CURRENT_ROUTE_" + str(name) + ".pickle"
        with open(post_routes, 'rb') as post_routes:
            post_routes = pickle.load(post_routes)
        diff_routes = Diff(pre_routes,post_routes)
        # diff_interface = Diff(pre_interface,post_interface,exclude=get_parser_exclude('show ipv6 interface', dev))
        diff_routes.findDiff()
        log.debug("DIFFERENTIATION COMPLETED FOR ROUTING STATUS - PARSER")
        if str(diff_routes) is "":
            log.info(banner("NO ROUTING CHANGES FOR '{}'".format(name)))
        else:
            log.info(banner("ROUTING CHANGES FOR '{}'".format(name)))
            print(diff_routes)
    except:
        log.info(banner("NO ROUTING PARAMETERS AVAILABLE FOR '{}'".format(name)))
        pass
