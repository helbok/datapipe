from datapipe.cli import main


def test_version_command(capsys):
    assert main(["version"]) == 0
    out = capsys.readouterr().out.strip()
    assert out
