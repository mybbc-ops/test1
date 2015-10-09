
#!/bin/bash

set -e

# Remove the welcome configuration
rm -f /etc/httpd/conf.d/welcome.conf

# Enable Apache
chkconfig httpd on

