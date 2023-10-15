#!/usr/bin/python3
"""
clean_web_static module
"""
from fabric.api import *
import os


env.hosts = ["100.26.209.142", "54.158.214.70"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    Deletes archives
    """
    try:
        number = int(number)
        if number < 0:
            return False
        if number == 0:
            number = 1
        else:
            number = number + 1

        # remove archives in local directory
        with lcd("versions"):
            local("ls -t | tail -n +{} | xargs -I {{}} rm {{}}".format(number))

        # remove archives from remote servers
        with cd("/data/web_static/releases"):
            run("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".
                format(number))

    except Exception:
        return False
