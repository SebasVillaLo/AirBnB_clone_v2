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
    archive_name = archive_path.split('/')[1]
    name_archive = archive_name.split('.')[0]
    re_archive = "/data/web_static/releases/{}".format(name_archive)
    up_archive = "/tmp/{}".format(archive_name)
    put(archive_path, up_archive)
    run('mkdir -p ' + re_archive)
    run('tar -xzf /tmp/{} -C {}/'.format(archive_name, re_archive))
    run('rm {}'.format(up_archive))
    mv = 'mv ' + re_archive + '/web_static/* ' + re_archive + '/'
    run(mv)
    run('rm -rf ' + re_archive + '/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s ' + re_archive + ' /data/web_static/current')
    return True
