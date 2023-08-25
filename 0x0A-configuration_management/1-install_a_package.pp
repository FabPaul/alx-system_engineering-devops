# Install a package "flask" in this case

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
