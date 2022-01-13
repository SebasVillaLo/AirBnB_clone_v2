#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from datetime import datetime
from fabric.api import local
from os import exists

def do_pack():
    """
    Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo, using the function do_pack.
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    tgzName = ("web_static_" + date + ".tgz")
    path_archive = ("tar -czvf versions/{} web_static".format(tgzName))
    if exists(path_archive) is False:
        return None
    return path_archive
