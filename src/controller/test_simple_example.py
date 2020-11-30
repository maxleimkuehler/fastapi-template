from controller.simple_example import SimpleExample


def _setup():
    return SimpleExample()

def test_init():
    simpleExample = _setup()

    assert hasattr(simpleExample, 'multiplier')