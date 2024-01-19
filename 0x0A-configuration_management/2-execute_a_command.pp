#Using Puppet, create a manifest that kills a process named killmenow

exec { 'killmenow':
cmd      => 'pkill killmenow',
provider => 'shell'
} 
