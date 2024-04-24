# This Puppet manifest configures the global SSH client settings

# Ensure the /etc/ssh/ssh_config file exists and has the correct permissions
file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',

  # The content of the file sets the private key to ~/.ssh/school and turns off password authentication
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
