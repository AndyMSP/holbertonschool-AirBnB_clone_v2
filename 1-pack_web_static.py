#!/usr/bin/python3
"""fabfile to compress directory"""


def do_pack():
    """ Pack directory into .tgz file with specified format """

    from fabric.api import env
    env.abort_exception = Exception
    from datetime import datetime
    from fabric.api import local

    try:
        t = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        name = "versions/web_static_{}.tgz".format(t)
        local("mkdir -p versions")
        res = local("tar -cvzf {} web_static".format(name))
        return(name)
    except Exception:
        return None
