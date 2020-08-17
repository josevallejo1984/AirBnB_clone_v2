#!/usr/bin/python3
"""Desploy site web."""
import os.path
from fabric.api import *
from fabric.operations import run, put
env.hosts = ['35.231.89.82', '54.226.196.8']


def do_deploy(archive_path):
    """Upload file in the server remote."""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        put(archive_path, "/tmp/")
        unpack = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + unpack.split(".")[0])
        run("sudo mkdir -p {:s}".format(folder))

        run("sudo tar -xzf /tmp/{:s} -C {:s}".format(unpack, folder))

        run("sudo rm /tmp/{:s}".format(unpack))
        run("sudo mv {:s}/web_static/* {:s}/".format(folder, folder))
        run("sudo rm -rf {:s}/web_static".format(folder))

        run('sudo rm -rf /data/web_static/current')

        run("sudo ln -s {:s} /data/web_static/current".format(folder))
        return True
    except:
        return False
