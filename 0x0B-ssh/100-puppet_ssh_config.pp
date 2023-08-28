# Puppet client configuration file (w/Puppet)

file { 'etc/ssh/ssh_config':
  ensure  = file,
  content => '
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
',
}
