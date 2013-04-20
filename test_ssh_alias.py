from ssh_alias import read_host_config, write_host_config, delete_host_config
import os
from tempfile import NamedTemporaryFile


def test_read_host_config():
    """
    Test the read_host_config function.
    """
    lines = [
            'Host foo',
            ' HostName foo.example.com',
            ' Port 23',
            ' User foouser',
            '',
            'host bar',
            ' hostname bar.example.com',
            ' port 24',
            ' user baruser',
            ' identityfile ~/.ssh/bar.key',
            ]
    tf = NamedTemporaryFile(delete=False)
    for line in lines:
        tf.write("{0}\n".format(line))
    tf.close()
    foo_config = read_host_config('foo', tf.name)
    assert foo_config['hostname'] == 'foo.example.com'
    assert foo_config['port'] == '23'
    assert foo_config['user'] == 'foouser'
    assert 'identityfile' not in foo_config
    bar_config = read_host_config('bar', tf.name)
    assert bar_config['hostname'] == 'bar.example.com'
    assert bar_config['port'] == '24'
    assert bar_config['user'] == 'baruser'
    assert bar_config['identityfile'] == '~/.ssh/bar.key'
    os.remove(tf.name)


def test_write_host_config():
    """ Test the write_host_config function. """
    lines = [
            'Host foo',
            ' HostName foo.example.com',
            ' Port 23',
            ' User foouser',
            ]
    tf = NamedTemporaryFile(delete=False)
    for line in lines:
        tf.write("{0}\n".format(line))
    tf.close()
    new_foo = {
            'hostname': 'newfoo.example.com',
            'port': '24',
            'user': 'newfoouser',
            'identityfile': 'newidfile',
            }
    write_host_config('foo', new_foo, tf.name)
    lines = [ln.rstrip() for ln in open(tf.name)]
    assert len(lines) == 5
    assert lines[0] == 'host foo'
    assert ' hostname newfoo.example.com' in lines[1:]
    assert ' user newfoouser' in lines[1:]
    assert ' port 24' in lines[1:]
    assert ' identityfile newidfile' in lines[1:]
    bar = {
            'hostname': 'bar.example.com',
            'port': '25',
            'user': 'baruser',
            }
    write_host_config('bar', bar, tf.name)
    lines = [ln.rstrip() for ln in open(tf.name)]
    assert len(lines) == 10
    assert lines[6] == 'host bar'
    assert ' hostname bar.example.com' in lines[7:]
    assert ' port 25' in lines[7:]
    assert ' user baruser' in lines[7:]
    os.remove(tf.name)


def test_delete_host_config():
    """
    Test the delete_host_config function.
    """
    lines = [
            'Host foo',
            ' HostName foo.example.com',
            ' Port 23',
            ' User foouser',
            '',
            'host bar',
            ' hostname bar.example.com',
            ' port 24',
            ' user baruser',
            ' identityfile ~/.ssh/bar.key',
            ]
    tf = NamedTemporaryFile(delete=False)
    for line in lines:
        tf.write("{0}\n".format(line))
    tf.close()
    delete_host_config('foo', tf.name)
    lines = [ln.rstrip() for ln in open(tf.name)]
    assert len(lines) == 5
    assert lines[0] == 'host bar'
    assert lines[1] == ' hostname bar.example.com'
    assert lines[2] == ' port 24'
    assert lines[3] == ' user baruser'
    assert lines[4] == ' identityfile ~/.ssh/bar.key'


if __name__ == "__main__":
    arguments = docopt(__doc__)
    print arguments
