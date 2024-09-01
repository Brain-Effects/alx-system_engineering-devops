# This Puppet manifest fixes the Apache 500 error by ensuring the
# required directory exists with correct permissions
file { '/var/www/html':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}
