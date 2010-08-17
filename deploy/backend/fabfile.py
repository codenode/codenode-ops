"""
1) Create file ``~/.fabric`` that contains:
    fab_key_filename = /path/to/ec2/keypair-file.private
"""
from fabric.api import env, run, local, put

env.user = "root"
env.key_filename = ""

def bootstrap(): 
    run("apt-get -qq update && apt-get upgrade -y")
    #Create 'codenode' user
    #install deps
    #Edit Sage twistd plugin file?


def devel_tools():
    run("apt-get install -y vim git-core ipython")
    put("../resources/vimrc", ".vimrc")
