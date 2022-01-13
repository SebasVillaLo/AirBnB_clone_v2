#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
from datetime import datetime
from fabric.api import local
from os import exists


def do_pack():
    """
    Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        tgzName = "web_static_" + date + ".tgz"
        path_archive = local("tar -czvf versions/{} web_static".format(tgzName))
        return path_archive
    except Exception:
        return None
