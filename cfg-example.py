## This variable sets a dictionary that can replace the DNS server IP to a desidered one,
## you can disable the DNS redirecting by removing the content of this dictionary.
## Do not completely remove the variable otherwise it the script will crash
dns_server_replacement = {
    "gameboy.datacenter.ne.jp" : '127.0.0.1',
    "mail.srv1.dion.ne.jp" : '127.0.0.1',
    "pop.srv1.dion.ne.jp" : '127.0.0.1',
}

## This variable has the "real" domain; Mobile Adapter usually writes dion.ne.jp, but we
## want it to be our domain - this should be 10 characters or less.
real_email_domain = b"domain.tld"

## This is for our own login server; currently, this does not work, but in the future it
## hopefully should!
dion_login_ip = "127.0.0.1"
dion_login_port = 7705
enable_dion_login_server = False

## If the DNS server has no idea what IP it is meant to return, it'll instead return this IP.
backup_ip = '127.0.0.1'

## If this variable is enabled, the script will connect to an external email server
## instead of emulating a fake one.
enable_external_email_server = True

## If this variable is enabled, after the HELO command, the script will try to authenticate
## to the SMTP server.
## NOTE: You need to perform POP3 authentication first, otherwise the script won't be able to
## intercept the password.
require_smtp_authentication = True

## If this variable is enabled, the script will try to resolve domain name by using
## the system default DNS server
enable_external_dns_server = False 

## This mode prints each byte received and sent to the adapter
verbose_mode = False