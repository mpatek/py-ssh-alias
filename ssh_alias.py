"""SSH Alias.

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
"""
from docopt import docopt


def read_host_config(host, config_file):
    """
    Returns list of host configurations.
    """
    in_host_config = False
    config = None
    for line in open(config_file):
        tokens = line.strip().split()
        if tokens:
            first_token = tokens[0].lower()
            if not in_host_config:
                if first_token == 'host' and tokens[1] == host:
                    in_host_config = True
                    config = {}
            else:
                config[first_token] = ' '.join(tokens[1:])
        elif in_host_config:
            in_host_config = False

    return config


def fetch_other_lines(host, config_file):
    """ Get lines not associated with specified host. """
    in_host_config = False
    lines = []
    for line in open(config_file):
        tokens = line.strip().split()
        if tokens:
            first_token = tokens[0].lower()
            if not in_host_config:
                if first_token == 'host' and tokens[1] == host:
                    in_host_config = True
        if not tokens and in_host_config:
            in_host_config = False
        elif not in_host_config:
            lines.append(line)
    return lines


def write_host_config(host, config, config_file):
    """
    Adds/updates host configuration.
    """
    in_host_config = False
    lines = fetch_other_lines(host, config_file)
    if lines:
        last_line = lines[-1].strip()
        if last_line:
            lines.append("\n")  # separator
    lines.append("host {0}\n".format(host))
    for k, v in config.items():
        lines.append(" {0} {1}\n".format(k, v))
    with open(config_file, 'w') as ofh:
        for line in lines:
            ofh.write(line)


def delete_host_config(host, config_file):
    """
    Removes host configuration.
    """
    in_host_config = False
    lines = fetch_other_lines(host, config_file)
    with open(config_file, 'w') as ofh:
        for line in lines:
            ofh.write(line)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    print arguments
