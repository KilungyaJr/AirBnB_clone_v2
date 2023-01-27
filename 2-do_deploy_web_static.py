#!/usr/bin/python3
from datetime import datetime
from fabric.api import env, local, put, run, settings

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
    """
    Distributes an archive to your web servers
    """
    if not local("test -e {}".format(archive_path), capture=True).succeeded:
        return False

    archive_name = archive_path.split("/")[-1]
    rlsFldr = "/data/web_static/releases/{}".format(archive_name.split(".")[0])

    with settings(warn_only=True):
        # Upload archive to /tmp/ on the web server
        put(archive_path, "/tmp/")

        # Uncompress archive to releases folder
        run("mkdir -p {}".format(rlsFldr))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, rlsFldr))

        # Delete archive from web server
        run("rm /tmp/{}".format(archive_name))

        # Delete and recreate the symbolic link
        run("rm -f /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(rlsFldr))
    print('New version deployed!')
    return True
