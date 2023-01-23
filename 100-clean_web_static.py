#!/usr/bin/python3
from datetime import datetime
from fabric.api import env, local, put, run, settings
import os

env.hosts = ['52.91.121.190', '100.26.168.135']


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
    """
    Distributes an archive to your web servers
    """
    if not local("test -e {}".format(archive_path), capture=True).succeeded:
        return False

    archive_name = archive_path.split("/")[-1]
    release_folder = "/data/web_static/releases/{}".format(archive_name.split(".")[0])

    with settings(warn_only=True):
        # Upload archive to /tmp/ on the web server
        put(archive_path, "/tmp/")

        # Uncompress archive to releases folder
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, release_folder))

        # Delete archive from web server
        run("rm /tmp/{}".format(archive_name))

        # Delete and recreate the symbolic link
        run("rm -f /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_folder))
    print('New version deployed!')
    return True

def deploy():
    """Create and distribute an archive to a web server."""
    archivePath = do_pack()
    if archivePath is None:
        return False
    return do_deploy(archivePath)

def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
