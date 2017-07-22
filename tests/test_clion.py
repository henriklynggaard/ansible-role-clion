import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


desktop_file_location = "/root/.local/share/applications/clion-2017.2.desktop"


def test_desktop_file_exists(File):
    f = File(desktop_file_location)

    assert f.exists
    assert f.is_file


def test_desktop_file_contains_fullpath(File):
    f = File(desktop_file_location)

    assert f.contains("/root/Tools/clion-2017.2/bin/clion.png")
    assert f.contains("/root/Tools/clion-2017.2/bin/clion.sh")


def test_desktop_file_contains_right_name(File):
    f = File(desktop_file_location)

    assert f.contains("CLion 2017.2")


def test_start_file_exists(File):
    f = File('/root/Tools/clion-2017.2/bin/clion.sh')

    assert f.exists
    assert f.is_file
