from controller.health_controller import HealthController


def _setup():
    return HealthController()

def test_init():
    healthController = _setup()

    assert hasattr(healthController, 'healthStatus')