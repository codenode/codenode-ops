"""
USAGE:

Provide full path to the codenode repository
that contains the "doc" dir that you want to release.

Do not include the path "doc" in the full path.


EXAMPLE:

    $ fab release:/path/to/codenode

"""
from fabric.api import env, run, local, put, hosts

env.user = "codenode"
HOST = "codenode.org"


@hosts(HOST)
def release(codenode_dir):
    """Release docs from a repository"""
    local_cmd = "export PYTHONPATH=%s && sphinx-build %s/doc/ /tmp/doc"% (codenode_dir, codenode_dir)
    local(local_cmd)
    local("cd /tmp && tar -cvzf codenode-doc.tar.gz doc/")
    put("/tmp/codenode-doc.tar.gz", "/tmp/codenode-doc.tar.gz")
    run("cd /tmp && tar -zxvf codenode-doc.tar.gz && mv doc /home/codenode/website/docs")

