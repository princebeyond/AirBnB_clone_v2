#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the web_static"""

from fabric.api import local
import time

def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    timestamp = (time.strftime("%Y%m%d%H%M%S"))
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(timestamp))
        return ("versions/web_static_{}.tgz".format(
                                                    timestamp))
    except:
        return None
