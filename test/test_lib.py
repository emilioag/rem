from script.lib import replace_lines

def test_replace_lines():
    assert replace_lines("(version:\s+?)\d+(.\d+)?(.\d+)?", "\1rem", [
        "version: 1.0.1"
    ]) == (['version: 1.0.1'], ['\x01rem'], [('version: 1.0.1', '\x01rem')])