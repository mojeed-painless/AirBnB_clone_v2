#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['44.210.150.159', '35.173.47.15']
env.user = "ubuntu"


def do_clean(num=0):
    """ CLEANS """

    num = int(num)

    if num == 0:
        num = 2
    else:
        num += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(num))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, num))
