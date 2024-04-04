#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the web_static"""

import fabric.api from local
import time


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
