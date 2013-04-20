py-ssh-alias
============

SSH Alias Management in Python

Installation:

    $ git clone https://github/mpatek/py-ssh-alias
    $ cd py-ssh-alias
    $ python setup.py install

Command line usage:

    Usage:
      ssh_alias.py add <alias> <host> [--user=<user>]
                                      [--port=<port>]
                                      [--id-file=<idfile>]
                                      [--config-file=<config_file>]
      ssh_alias.py update <alias> [--user=<user>]
                                  [--port=<port>]
                                  [--id-file=<idfile>]
                                  [--host=<host>]
                                  [--config-file=<config_file>]
      ssh_alias.py rm <alias> [--config-file=<config_file>]

    Options:
      --user=<user>                Username [default: root].
      --port=<port>                Port [default: 22].
      --id-file=<idfile>           Identity file.
      --host=<host>                Host.
      --config-file=<config_file>  SSH Config File [default: ~/.ssh/config].
