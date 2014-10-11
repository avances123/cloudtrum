from fabric.api import *
from fabric.operations import put
from fabric.context_managers import shell_env
from fabtools import require
import fabtools


env.hosts           = ['54.72.230.45']
env.user            = 'ubuntu'
env.project         = 'cloudtrum'
env.repo_url        = 'git@github.com:avances123/cloudtrum.git'
env.use_ssh_config  = True
env.deploy_key_filename    = '/home/fabio/.ssh/id_rsa_%s_deploy' % env.project
env.project_path    = '/home/%s/src/%s' % (env.user,env.project)
env.virtualenv_path = '/home/%s/.virtualenvs/%s' % (env.user,env.project)


def linux():
    require.deb.uptodate_index(max_age={'day': 1})
    # Copio la key privada de deploy
    require.files.file('/home/%s/.ssh/id_rsa' % env.user, source=env.deploy_key_filename ,mode="600")
    # Conozco a github.com
    sudo('echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config')

    # locales
    fabtools.require.system.default_locale('es_ES.UTF-8')

    # Paquetes para el Pillow
    fabtools.require.deb.package('libjpeg-dev')
    fabtools.require.deb.package('libpng12-dev')
    fabtools.require.deb.package('zlib1g-dev')

    # Paquetes mios
    fabtools.require.deb.package('language-pack-es')
    fabtools.require.deb.package('byobu')
    fabtools.require.deb.package('htop')
    fabtools.require.deb.package('nmon')
    #fabtools.require.deb.package('libgdal-dev')
    #fabtools.require.deb.package('python-gdal')


def postfix():
    fabtools.require.deb.package('postfix') 


def supervisord():
    fabtools.require.deb.package('supervisor')
    require.files.directory('/var/log/cloudtrum/gunicorn',use_sudo=True)
    require.files.file('/etc/supervisor/conf.d/cloudtrum.conf',source='devops/supervisord-cloudtrum.conf',use_sudo=True,owner='root')
    fabtools.supervisor.reload_config()
    fabtools.supervisor.update_config()


def postgresql(version="9.3"):
    distrib = fabtools.system.distrib_codename()
    fabtools.deb.add_apt_key(keyid='ACCC4CF8', update=False, url='http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc')
    require.deb.source(
        'PGDG',
        'http://apt.postgresql.org/pub/repos/apt/',
        '%s-pgdg' % distrib,
        'main'
    )
    fabtools.require.postgres.server(version=version)
    fabtools.require.deb.package('postgresql-server-dev-9.3')
    require.postgres.user(env.user,env.project,superuser=True)
    require.postgres.database(env.project,owner=env.user)
    fabtools.require.deb.package("postgresql-%s-postgis-2.1" % version)
    run('psql cloudtrum -c "CREATE EXTENSION IF NOT EXISTS postgis"')

def nginx():
    require.nginx.server()
    require.files.directory('/var/log/cloudtrum/nginx',use_sudo=True)
    sudo("rm -rf /etc/nginx/sites-enabled/default")
    put(local_path='devops/nginx-cloudtrum.conf',remote_path='/etc/nginx/sites-available/cloudtrum',use_sudo=True)
    require.nginx.enabled(env.project)

def nodejs():
    require.deb.ppa('ppa:chris-lea/node.js')
    require.deb.package('nodejs')
    fabtools.nodejs.install_package('coffee-script')
    fabtools.nodejs.install_package('bower')
    fabtools.nodejs.install_package('less')

def redis():
    require.deb.package('redis-server')

def munin():
    require.deb.ppa('ppa:tuxpoldo/munin')
    require.deb.package('munin')
    require.deb.package('munin-node')
    require.deb.package('munin-plugins')
    require.deb.package('munin-plugins-extra')


def django(branch="master"):
    require.git.working_copy(env.repo_url,path=env.project_path,branch=branch,update=True)
    require.python.virtualenv(env.virtualenv_path)
    #fabtools.supervisor.stop_process('cloudtrum')
    with cd(env.project_path):
        with fabtools.python.virtualenv(env.virtualenv_path):
            require.python.requirements('devops/requirements.txt')
            run("pip install git+https://github.com/stormpat/blockr-python.git")

            with shell_env(DJANGO_SETTINGS_MODULE='cloudtrum.settings.production',AWS_ACCESS_KEY_ID="AKIAJGUN2PRW2M4A2BSA",AWS_SECRET_ACCESS_KEY="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"):
                run('python manage.py migrate --noinput')
                run('python manage.py collectstatic --noinput')


    # Renicio los servicios
    fabtools.supervisor.restart_process('cloudtrum')
    #fabtools.supervisor.restart_process('celery')

def deploy(branch="master"):
    linux()
    postfix()
    nginx()
    redis()
    supervisord()
    django(branch)
    #munin()

    
        
 
