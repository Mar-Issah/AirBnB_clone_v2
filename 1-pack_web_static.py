#!/usr/bin/python3
"""script that gen .tgz archive from contents of web_static folder """
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Archives the contents of the static files."""
    # if not os.path.isdir("versions"):
    #     os.mkdir("versions")
    local("mkdir -p versions")

    # cur_time = datetime.now()
    # output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
    #     cur_time.year,
    #     cur_time.month,
    #     cur_time.day,
    #     cur_time.hour,
    #     cur_time.minute,
    #     cur_time.second
    # )
    time_format = "%Y%m%d%H%M%S"
    timestamp = datetime.now().strftime(time_format)
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    try:
        print(f"Packing web_static to {archive_path}")
        local(f"tar -cvzf {archive_path} web_static")
        archize_size = os.stat(archive_path).st_size
        print(f"web_static packed: {archive_path} -> {archize_size} Bytes")
    except Exception:
        output = None
    return output
