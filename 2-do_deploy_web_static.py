#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
from datetime import datetime
from fabric.api import put, run, env
from os.path import exists

env.hosts = {'23.21.15.186', '34.138.82.74'}


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
    using the function do_deploy
    """
    if exists(archive_path) is False:
        return False
    try:
        nameFile = archive_path.split("/")[-1]
        NFile_no_ext = nameFile.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, NFile_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(nameFile, path, NFile_no_ext))
        run('rm /tmp/{}'.format(nameFile))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, NFile_no_ext))
        run('rm -rf {}{}/web_static'.format(path, NFile_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, NFile_no_ext))
        return True
    except Exception:
        return False

