#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

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
