#!/usr/bin/python3
"""
do_deploy_web_static module
"""
import os
from fabric.api import env, put, run, local
from datetime import datetime


env.hosts = ["100.26.209.142", "54.158.214.70"]
env.user = "ubuntu"


def do_pack():
    """
    This is used to genaerate a .tgz archive
    """
    local("mkdir -p versions")
    created_at = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_path = "versions/web_static_{}.tgz".format(created_at)
    archive = local("tar -czvf {} web_static".format(archived_path))
    if archive.succeeded:
        return archived_path
    else:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to webservers
    """
    # check if file path exists
    if not os.path.exists(archive_path):
        return False

    # get archive file without extension
    archive_file = archive_path.split('/')[1]
    file_name = archive_file.split('.')[0]
    remote_path = "/data/web_static/releases/"

    try:
        # upload the archive to remoteserver
        put(archive_path, "/tmp/")

        # create release folder
        run("sudo mkdir -p {}{}".format(remote_path, file_name))

        # uncompress archive
        run("sudo tar -zxf /tmp/{} -C {}{}".format(
            archive_file, remote_path, file_name))

        # delete the archive from webservers
        run("sudo rm /tmp/{}".format(archive_file))

        run("sudo mv {}{}/web_static/* {}{}".format(
            remote_path, file_name, remote_path, file_name))

        run("sudo rm -rf {}{}/web_static".format(remote_path, file_name))

        # delete symbolic link
        run("sudo rm -rf /data/web_static/current")

        # create new symbolic link
        run("sudo ln -s {}{} /data/web_static/current".format(
            remote_path, file_name))
        print("New version deployed!")
        return True

    except Exception:
        return False
