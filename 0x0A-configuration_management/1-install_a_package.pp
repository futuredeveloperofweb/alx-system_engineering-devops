# Using Puppet, install flask from pip3

package { 'python3':
    ensure   => installed,
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3'],
}

package { 'Werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3',
    require  => Package['flask'],
}

