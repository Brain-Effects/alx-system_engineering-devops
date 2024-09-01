# This Puppet manifest fixes the Apache 500 error by ensuring the
# required directory exists with correct permissions
file { '/var/www/html':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

exec { 'apache_configtest':
  command     => '/usr/sbin/apachectl configtest',
  refreshonly => true,
  notify      => Exec['restart_apache'],
}

exec { 'restart_apache':
  command     => '/usr/sbin/systemctl restart apache2',
  refreshonly => true,
}

service { 'apache2':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/var/www/html'],
}
