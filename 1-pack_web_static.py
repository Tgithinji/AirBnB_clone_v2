#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    This function is used to run the script
    """
    # create directory to store archived files
    local("mkdir -p versions")

    # get the time each file is created
    created_at = datetime.now().strftime("%Y%m%d%H%M%S")
    # create a path to the archived file
    archived_path = f"versions/web_static_{created_at}.tgz"

    archive = local(f"tar -czvf {archived_path} web_static")

    if archive.return_code == 0:
        return archived_path
    else:
        return None
