"""SSH Alias.

Usage:
  ssh_alias.py add <alias> <host> [--user=<user>]
                                  [--port=<port>]
                                  [--id-file=<idfile>]
  ssh_alias.py update <alias> [--user=<user>]
                              [--port=<port>]
                              [--id-file=<idfile>]
                              [--host=<host>]
  ssh_alias.py rm <alias>

Options:
  --user=<user>       Username [default: root].
  --port=<port>       Port [default: 22].
  --id-file=<idfile>  Identity file.
  --host=<host>       Host.

"""
from docopt import docopt

if __name__ == "__main__":
    arguments = docopt(__doc__)
    print arguments
