# Puppet file that installs nginx web server

exec { 'server setup':
  provider => shell,
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Hello World!" > /var/www/html/index.html; sudo sed -i "/server_name _;/a location /redirect_me {\\n\\treturn 301 https://twitter.com/FabPaul1;\\n\\t}\\n" /etc/nginx/sites-available/default; sudo service nginx restart',
}
