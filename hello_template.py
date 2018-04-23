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
#This line uses the specifies which directory the temapate is in
# file_loader = FileSystemLoader('my_templates')
# Load the enviroment
env = Environment(loader=file_loader)
template = env.get_template('hello_world.j2')
output = template.render()
#Print the output
print(output)