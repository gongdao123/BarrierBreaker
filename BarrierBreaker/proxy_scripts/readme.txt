# install required lib
apt-get install polipo python-pip cronolog
pip install shadowsocks

# Prepration
mkdir ~/app
ln -s ~/app /app
cd /app
svn co http://svn.motherapp.com/BarrierBreaker/proxy_scripts/
cd /app/proxy_scripts/
mkdir logs run

# add crontab job
# m h  dom mon dow   command
@reboot cd /app/proxy_scripts && ./start_proxy && ./check_proxy_status | /usr/bin/cronolog --period="1 day" /app/proxy_scripts/logs/boot.\%Y-\%m-\%d.log
*/10 * * * * /app/proxy_scripts/check_proxy_status | /usr/bin/cronolog --period="1 day" /app/proxy_scripts/logs/check.\%Y-\%m-\%d.log

