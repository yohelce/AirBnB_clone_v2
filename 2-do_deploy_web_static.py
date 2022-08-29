#!/usr/bin/python3
"""script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['3.84.114.176', '3.82.38.127']
path_release = '/data/web_static/releases'

def do_deploy(archive_path):
    if not path.isfile(archive_path):
        return False
    
    filename = archive_path.split('/')[-1]
    fname = filename.split('.')[0]

    if put(archive_path, '/tmp/{}'.format(filename)).failed:
        return False

    if run('mkdir -p /data/web_static/releases/{}'.format (fname)) .failed:
        return False

    if run('tar -xf /tmp/{} -C /data/web_static/releases/{}'.format (filename, fname)).failed:
	return False

    if run('rm /tmp/{}'.format (Filenane)).failed:
	return False

    path_web = '{}/{}'. format (path_releases, fname)

    if run('mv {}/web_static/* {}'.format (path_web, path_web)).failed:
	return False

    if run('rm -rf {}/web_static'. format (path_web)).failed:
	return False

    if run('rm -rf /data/web_static/current').failed:
	return False

    if run('ln -s {} /data/web_static/current'.format(path_web)).failed:
	return False

    return True
