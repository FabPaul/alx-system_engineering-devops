# Puppet file that installs nginx web server

package { 'nginx':
  ensure => 'present',
}

exec { 'nginx install':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'Intro':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec { 'port 80 and redirect':
  command  => 'sudo sed -i "/server_name _;/a location /redirect_me {\\n\\treturn 301 https:\/\/twitter.com\/FabPaul1;\\n\\t}\\n" /etc/nginx/sites-available/default'
  provider => shell,
}

exec { 'Nginx restart':
  command  => 'sudo service nginx restart'
  provider => shell,
}
