# This Puppet manifest optimizes the Nginx configuration to handle high load and reduce failed requests.

class optimize_nginx {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure     => running,
    enable     => true,
    subscribe  => File['/etc/nginx/nginx.conf'],
  }

  # Optimize Nginx configuration
  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('/alx-system_engineering-devops/0x1B-web_stack_debugging_4/optimize_nginx/templates/nginx.conf.erb'),
    notify  => Service['nginx'],
  }
}

# Apply the class
include optimize_nginx
