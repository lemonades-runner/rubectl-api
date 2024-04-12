from utils.exceptions import NotFoundError


class UpstreamNotFoundError(NotFoundError):
    def __str__(self):
        return 'Upstream not found.'
