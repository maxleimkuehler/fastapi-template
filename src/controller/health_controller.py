
import logging

log = logging.getLogger(__name__)


class HealthStatus:

    def __init__(self, status=True):
        self.status = status

    def unhealthy(self):
        self.status = False


class HealthController:

    def __init__(self):
        self.healthStatus = HealthStatus()
        try:
            #check instantiation of classes here, actual just setting status to true
            self.healthStatus.status = True
        except Exception as ex:
            log.exception(ex)
            self.healthStatus.unhealthy()

    def check(self):

        if not self.healthStatus.status:
            return self.healthStatus

        return self.healthStatus
