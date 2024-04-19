# This Puppet manifest kills a process named 'killmenow'
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
}
