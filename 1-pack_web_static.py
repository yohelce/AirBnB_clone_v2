#!/usr/bin/python3
"""Generates a .tgz archive from the
contents of the web_static folder"""

from fabric.operations import local
from datetime import datetime


def do_pack():
    """Function to compress files"""
    try:
        local("mkdir -p versions")
        time = datetime.now()
        date = time.strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_" + date
        local("tar -cvzf {}.tgz web_static".format(path))
        return path
    except:
        return None
