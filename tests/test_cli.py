from datapipe.cli import main


def test_version_command(capsys):
    assert main(["version"]) == 0
    out = capsys.readouterr().out.strip()
    assert out


def test_nodes_command(capsys):
    from datapipe.cli import main
    assert main(["nodes"]) == 0
    out = capsys.readouterr().out
    assert out


def test_edge_case_cli_019():
    from datapipe.cli import main
    assert main(['version']) == 0
