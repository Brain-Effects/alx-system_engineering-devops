# This Puppet script increases the file descriptor limits for the holberton user

exec { 'holberton hard':
  path     => ['/usr/bin/'],
  command  => "sudo sed -i 's/^holberton hard /holberton hard nofile 2000/g' /etc/security/limits.conf",
  provider => 'shell',
}

exec { 'holberton soft':
  path     => ['/usr/bin/'],
  command  => "sudo sed -i 's/^holberton soft /holberton soft nofile 2000/g' /etc/security/limits.conf",
  provider => 'shell',
}
