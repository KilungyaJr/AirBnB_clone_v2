#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ['100.26.235.136', '54.165.230.119']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    of the AirBnB Clone repo
    """
    # Create versions folder if it doesn't exist
    local("mkdir -p versions")

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the archive file name
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Create the archive
    local("tar -czvf versions/{} web_static".format(archive_name))

    # Check if the archive was created successfully
    if local("ls versions/{}".format(archive_name), capture=True).succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None

def do_deploy(archive_path):
    """Distributes an .tgz archive through web servers
    """

    if path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))

        print('New version deployed!')

        return True

    return False
