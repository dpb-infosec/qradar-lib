from .qradarmodel import QRadarModel


class NetworkHierarchy(QRadarModel):
    def __init__(self, *, id: int = None, network_id: int = None, group: str = None, name: str = None, cidr: str = None, description: str = None, domain_id: int = None, location: object = None, country_code: str = None) -> None:
        self.id = id
        self.network_id = network_id
        self.group = group
        self.name = name
        self.cidr = cidr
        self.description = description
        self.domain_id = domain_id
        self.location = location
        self.country_code = country_code
