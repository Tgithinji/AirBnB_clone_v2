#!/usr/bin/python3
"""
do_deploy_web_static module
"""
import os
from fabric.api import env, put, run

env.hosts = ["100.26.209.142", "54.158.214.70"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    distributes an archive to webservers
    """
    # check if file path exists
    if not os.path.exists(archive_path):
        return False
    # get archive file without extension
    archive_file = os.path.basename(archive_path)
    file_name = archive_file.split('.')[0]
    remote_path = "/data/web_static/releases/"

    try:
        # upload the archive to remoteserver
        put(archive_file, "/tmp/")

        # create release folder
        run("mkdir -p {}{}".format(remote_path, file_name))

        # uncompress archive
        run("tar -zxf /tmp/{} -C {}{}".format(
            archive_file, remote_path, file_name))

        # delete the archive from webservers
        run("rm -rf /tmp/{}".format(archive_file))

        # delete symbolic link
        run("rm -rf /data/web_static/current")

        # create new symbolic link
        run("ln -s {}{} /data/web_static/current".format(
            remote_path, file_name))
        return True

    except Exception:
        return False
