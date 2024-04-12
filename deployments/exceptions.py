from utils.exceptions import NotFoundError


class DeploymentNotFoundError(NotFoundError):
    def __str__(self):
        return 'Deployment not found.'
