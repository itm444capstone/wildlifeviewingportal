#! /bin/bash

# Update the packages and install the standard
# ubuntu packages

apt-get install -y build-essential
apt-get install -y python-dev
apt-get install -y python3-dev
apt-get install -y python3-pip
apt-get install -y supervisor
apt-get install -y libjpeg-dev
apt-get install -y libpng12-dev
apt-get install -y libfreetype6-dev
apt-get install -y nginx
pip3 install virtualenv

cd ../
PROJDIR=$(pwd)

if [ -d "/var/www" ]; then
    mkdir /var/www
fi

cd /var/www

python3 -m virtualenv wildlife2
mv PROJDIR wildlife/
cd wildlife

VIRTUALENV=$(pwd)
mkdir run
mkdir log

RUNDIR="$VIRTUALENV/run/gunicorn.sock"
source bin/activate

cd wildlifeviewingportal/install

echo "=============================================="
echo "     WILDLIFE VIEWING PORTAL INSTALLATION     "
echo "=============================================="
echo "Before we begin, we must collect some basic"
echo "information. "
echo "\n"
echo "DATABASE INFORMATION"
echo "We need some basic database information so"
echo "we can properly connect to the database."
echo "The database is required to be a postgres"
echo "database."
while true; do
    echo ""
    echo "-----------------------------------------"
    echo "HOST (url):"
    read DBHOST
    echo "Port: "
    read DBPORT
    echo "Database Name: "
    read DBNAME
    echo "Database User: "
    read DBUSER
    echo "Database Password: "
    read DBPASSWORD
    if [ -z "$DBHOST" ]; then
        echo "You must specify a host"
        continue
    fi
    if [ -z "$DBPORT" ]; then
        echo "You must specify a port"
        continue
    fi
    if [ -z "$DBNAME" ]; then
        echo "You must specify a database name"
        continue
    fi
    if [ -z "$DBUSER" ]; then
        echo "You must specify a database user"
        continue
    fi
    if [ -z "$DBPASSWORD" ]; then
        echo "You must specify a database password"
        continue
    fi
    break
done

echo "\n"
echo "-----------------------------------------------"
echo "Great! Now we are going to continue with the install"
echo "process."

INSTALL_DIR=$(pwd)

# Configure the settings.py file
cp settings.py settings_copy.py
sed -i 's/SED_DB_HOST_REPLACE/$DBHOST/g' settings.py
sed -i 's/SED_DB_PORT_REPLACE/$DBPORT/g' settings.py
sed -i 's/SED_DB_NAME_REPLACE/$DBNAME/g' settings.py
sed -i 's/SED_DB_USER_REPLACE/$DBUSER/g' settings.py
sed -i 's/SED_DB_PASSWORD_REPLACE/$DBPASSWORD/g' settings.py
cd ..

# Configure the media folder
DJANGO_DIR=$(pwd)
chmod -R 777 media

# Configure gunicorn_start file
echo "\n"
echo "We need some more information regarding the user to"
echo "run the website as."
echo "User: "
read USER
echo "Group: "
read GROUP
cd install
cp gunicorn_start gunicorn_start_copy
sed -i 's/SED_DJANGO_DIR_REPLACE/$DJANGO_DIR/g' gunicorn_start
sed -i 's/SED_SOCK_FILE_REPLACE/$RUNDIR/g' gunicorn_start
sed -i 's/SED_USER_REPLACE/$USER/g' gunicorn_start
sed -i 's/SED_GROUP_REPLACE/$GROUP/g' gunicorn_start

# Configure gunicorn.conf
STDOUT_FILE = "$VIRTUALENV/log/gunicorn.log"
STDERR_FILE = "$VIRTUALENV/log/gunicorn.err.log"
GUNICORN_START_FILE = "$VIRTUALENV/bin/gunicorn_start"
cp gunicorn.conf gunicorn.copy.conf
sed -i 's/SED_STDERR_FILE_REPLACE/$STDERR_FILE/g' gunicorn.conf
sed -i 's/SED_STDOUT_FILE_REPLACE/$STDOUT_FILE/g' gunicorn.conf
sed -i 's/SED_USER_REPLACE/$USER/g' gunicorn.conf
sed -i 's/SED_COMMAND_REPLACE/$GUNICORN_START_FILE/g' gunicorn.conf


# Configure nginx file
echo "--------------------------------------------"
echo "Configuring nginx server"
echo "We need one more piece of information"
echo "What is the name of this server?"
read SERVER_NAME
SERVER_URL="unix:$RUNDIR"
ACCESS_LOG="$VIRTUALENV/log/access.log"
MEDIA="$DJANGO_DIR/media/";
STATIC="$DJANGO_DIR/static/";

cp itm444_nginx.conf itm444_nginx_copy.conf
sed -i 's/SED_SERVER_REPLACE/$SERVER_URL/g' itm444_nginx.conf
sed -i 's/SED_SERVER_NAME_REPLACE/$SERVER_NAME/g' itm444_nginx.conf
sed -i 's/SED_ACCESS_LOG_REPLACE/$ACCESS_LOG/g' itm444_nginx.conf
sed -i 's/SED_MEDIA_REPLACE/$MEDIA/g' itm444_nginx.conf
sed -i 's/SED_STATIC_REPLACE/$STATIC/g' itm444_nginx.conf
cp itm444_nginx.conf /etc/nginx/sites-available
cp itm444_nginx_copy.conf itm444_nginx.conf

cd ..

