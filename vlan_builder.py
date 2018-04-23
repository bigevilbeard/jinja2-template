#!/usr/bin/env python

##############################################################
# Network Automation Template Configurations
# Author: Stuart Clark <stuaclar@cisco.com>
#
# https://blogs.cisco.com/developer/network-automation-template-configurations
##############################################################

from jinja2 import Environment, FileSystemLoader

#This line uses the current directory
file_loader = FileSystemLoader('.')
# Load the enviroment
env = Environment(loader=file_loader)
template = env.get_template('vlan.j2')
vlans = ['vlan10', 'vlan20', 'vlan30']
output = template.render(vlans=vlans)
#Print the output
print(output)