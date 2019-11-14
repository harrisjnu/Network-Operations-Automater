
#Analyse and Parsing Function Library

##Support Library Calls
#Generic Libraries
import sys
import logging

#Specific Libraries
from pyats.log.utils import banner
from pyats.topology import loader
from genie.conf import Genie
import genie
import pyats


# Logging Engine Load
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s')
log = logging.getLogger(__name__)

class get_generic:
    def config(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            config = dev.parse("show running-config")
        except:
            log.info("\n CONFIG EXTRACTION FAILED '{}'.\n".format(dev.name))
            pass
        return config

    def cdp(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            cdp = dev.parse("show cdp neighbors")
        except:
            log.info("\n CDP EXTRACTION FAILED '{}'.\n".format(dev.name))
            pass
        return cdp

    def environment(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            environment = dev.parse("show environment all")
        except:
            log.info("CDP EXTRACTION FAILED '{}'.\n".format(dev.name))
            pass
        return environment

    def inventory(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            inventory = dev.parse("show inventory")
        except:
            log.info("INVENTORY COLLECTION FAILED '{}'.\n".format(dev.name))
            pass
        return inventory

    def stackpower(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            stackpower = dev.parse("show stack-power")
        except:
            log.info("STACK POWER FETCH FAILED '{}'.\n".format(dev.name))
            pass
        return stackpower

class get_interface:
    def status(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            interfaces = dev.parse("show interfaces")
        except:
            log.info("INTERFACE STATUS COLLECTION FAILED '{}'.\n".format(dev.name))
            pass
        return interfaces

    def brief(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            interfaces = dev.parse("show ip interface brief")
        except:
            log.info("INTERFACE BRIEF COLLECTION FAILED '{}'.\n".format(dev.name))
            pass
        return interfaces

    def lldp(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            lldp = dev.parse("show lldp entry *")
        except:
            log.info("LLDP STATE COLLECTION FAILED '{}'.\n".format(dev.name))
            pass
        return lldp

    def stp(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            stp = dev.parse("show spanning-tree summary")
        except:
            log.info("STP STATE COLLECTION FAILED '{}'.\n".format(dev.name))
            pass
        return stp

    def routing(dev):
        assert dev is not None, "Target device not loaded"
        if not dev.is_connected():
            log.debug("\n Device '{}' not connected...Connecting Now.\n".format(dev.name))
            dev.connect()
        try:
            route = dev.parse("show ip route")
        except:
            log.info("ROUTING STATE COLLECTION FAILED '{}'.\n".format(dev.name))
            pass
        return route

