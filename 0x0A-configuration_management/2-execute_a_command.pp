# Kill a process called 'killmenow'

# Only kill the process if it exist

# If it doesn't exists, puppet should exit

# with a 0 return code and not 1


exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
