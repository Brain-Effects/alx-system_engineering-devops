# This Puppet manifest fixes the Apache 500 error by ensuring the
# required directory exists with correct permissions
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => '<html><body><h1>It works!</h1></body></html>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

exec { 'apache_configtest':
  command     => '/usr/sbin/apachectl configtest',
  refreshonly => true,
  notify      => Service['apache2'],
}

service { 'apache2':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/var/www/html/index.html'],
  require    => Exec['apache_configtest'],
}
