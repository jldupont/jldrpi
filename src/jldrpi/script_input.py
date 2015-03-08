"""
    Created on 2015-02-28
    @author: jldupont
"""
import logging
import json

from defs import Pin
        


def parse_pin_definition(input_list):
    """
    Format:
    
      25:UF ==> pin 25, pull-up,   falling edge
      1:DR  ==> pin 1,  pull-down, rising edge

    """
    result = []
    
    for pindef in input_list:
        try:
            pindef = pindef.lower()
            pin_number, props = pindef.split(":")
        except:
            raise Exception("wrong format for entry: %s" % pindef)
            
        pin = Pin.parse_and_validate(pin_number, props)
        result.append(pin)

    return result


def run(pins=None, debug=False):
    """
    Entry Point
    """
    
    try:
        dpins = parse_pin_definition(pins)
        
    except Exception, e:
        logging.warn(e.message)
        return
    
    
    print dpins
#
#