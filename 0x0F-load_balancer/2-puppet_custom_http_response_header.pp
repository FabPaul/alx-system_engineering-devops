# automate the task of creating a custom HTTP header response, but with Puppet.

# Run apt-get update
exec { 'update':
  command => '/usr/bin/apt-get update',
}

# Ensuure package is installed
package { 'nginx':
  ensure => 'present',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['http_header'],
}

# Create a file_line resource to add the custom httpheader to nginx
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "add_header X-Served-By \"${hostname}\";",
  match => '^.*http\s*{.*$',
}

# Restart nginx
#exec { 'execute':
#  command => '/usr/sbin/service nginx restart',
#  require => Package['nginx'],
#}
