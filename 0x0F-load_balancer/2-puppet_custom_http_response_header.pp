# 2-puppet_custom_http_response_header.pp
# This Puppet manifest configures Nginx to add a custom HTTP header 'X-Served-By' with the hostname of the server

class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/conf.d/custom_header.conf'],
  }

  file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => file,
    content => "add_header X-Served-By \$hostname;\n",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

include nginx_custom_header
