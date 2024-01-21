#!/usr/bin/env bash
# make changes to our configuration file

include stdlib

file { '/etc/ssh/ssh_config':
 ensure => present,
}

file_line { 'Turn off passwd auth':
 path => '/etc/ssh/ssh_config',
 line => 'PasswordAuthentication no',
 match => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
 path => '/etc/ssh/ssh_config',
 line => 'IdentifyFile ~/.ssh/school',
 match => '^#IdentifyFile',
}
