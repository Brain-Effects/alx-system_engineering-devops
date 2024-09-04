# This Puppet manifest optimizes the Nginx configuration to handle high load and reduce failed requests.

# Class: optimize_nginx
# This class ensures that Nginx is installed, configured, and running optimally.
# It also stops Apache to avoid port conflicts and validates the Nginx configuration.
class optimize_nginx {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

# Ensure Apache is stopped to avoid port conflicts
  service { 'apache2':
    ensure => stopped,
    enable => false,
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/nginx.conf'],
  }

  # Optimize Nginx configuration
  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('/alx-system_engineering-devops/0x1B-web_stack_debugging_4/optimize_nginx/templates/nginx.conf.erb'),
    notify  => Service['nginx'],
  }

# Validate Nginx configuration before starting the service
  exec { 'nginx_config_test':
    command     => '/usr/sbin/nginx -t',
    refreshonly => true,
    subscribe   => File['/etc/nginx/nginx.conf'],
    notify      => Service['nginx'],
  }
}

# Apply the class
include optimize_nginx
