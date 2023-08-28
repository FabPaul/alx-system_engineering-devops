# Puppet client configuration file (w/Puppet)

file_line {'Password authentication and File ID':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no\n	IdentityFile ~/.ssh/school',
}
