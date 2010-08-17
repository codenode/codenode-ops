"""
USAGE:
    $ fab deploy:the_target

    $ fab deploy:target=staging,fastcgi_host=ec2-75-101-225-234.compute-1.amazonaws.com

"""
from fabric.api import env, run, local, put, sudo, abort, hosts
from fabric.contrib.console import confirm
from fabric.contrib.files import upload_template


env.user = "codenode"

NGINX_HOST = "codenode.org"
NGINX_DIR = "/usr/local/nginx/"
NGINX_TEST = "/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf"
NGINX_RELOAD = "kill -HUP `cat /usr/local/nginx/logs/nginx.pid`"
NGINX_CONF_TMPL = "codenode.conf"

NGINX_CONF_CTX = {
    "fastcgi_host":"---", 
    "static_path":"---", 
}


@hosts(NGINX_HOST)
def deploy(target, fastcgi_host):
    """Deploy to target."""
    if target not in ['staging', 'production']:
        abort("target must be either 'staging' or 'production'")
    put(NGINX_CONF_TMPL, "/tmp/%s.%s" % (NGINX_CONF_TMPL, target))
    _restart_nginx(target, fastcgi_host)

def _restart_nginx(target, fastcgi_host):
    """Restart Nginx with target being
    either 'staging' or 'production'.
    """
    NGINX_CONF_CTX["fastcgi_host"] = fastcgi_host
    fname = NGINX_CONF_TMPL 
    destination = NGINX_DIR + NGINX_CONF_TMPL + "." + target #e.g. "/usr/local/nginx/codenode.conf.production"
    upload_template(fname, destination, NGINX_CONF_CTX, use_jinja=True, use_sudo=True) #TODO allow no password for cmd
    sudo(NGINX_TEST + " && " + NGINX_RELOAD)


def install():
    #deal with Database, templates, static files.
    #create and install in a venv
    #restart
    pass
