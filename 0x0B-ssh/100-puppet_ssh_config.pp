# set up your client SSH configuration file so that you can connect to a server without typing a password

include stdlib
file_line { 'Turn of passwd auth':
	ensure => present,
	path => 'etc/ssh/shh_config',
	mode    => '0600',
	line => 'PasswordAuthentication no',
	replace => true,
}

file_line { 'Delare identity file':
	ensure => present,
        path => 'etc/ssh/shh_config',
	mode    => '0600',
	line => 'IdentityFile ~/.ssh/school',
	replace => true,
}
