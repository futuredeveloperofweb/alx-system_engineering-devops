#!/usr/bin/pup
## Install a given version of flask
package {'flask':
 ensure   => '2.1.0',
 provider => 'pip3'
}
