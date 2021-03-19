from .qradarmodel import QRadarModel


class Logsource(QRadarModel):
    def __init__(self, *, id=None, name=None, description=None, type_id=None, protocol_type_id=None, protocol_parameters=None, enabled=None, gateway=None,
                 internal=None, credibility=None, target_event_collector_id=None, disconnected_log_collector_id=None, coalesce_events=None, store_event_payload=None, log_source_extension_id=None,
                 language_id=None, group_ids=None, requires_deploy=None, status=None, auto_discovered=None, average_eps=None, creation_date=None, modified_date=None, last_event_time=None,
                 wincollect_internal_destination_id=None, wincollect_external_destination_ids=None, legacy_bulk_group_name=None, sending_ip=None, parsing_order=None):

        self.id = id
        self.name = name
        self.description = description
        self.type_id = type_id
        self.protocol_type_id = protocol_type_id
        self.protocol_parameters = protocol_parameters
        self.enabled = enabled
        self.gateway = gateway
        self.internal = internal
        self.credibility = credibility
        self.target_event_collector_id = target_event_collector_id
        self.disconnected_log_collector_id = disconnected_log_collector_id
        self.coalesce_events = coalesce_events
        self.store_event_payload = store_event_payload
        self.log_source_extension_id = log_source_extension_id
        self.language_id = language_id
        self.group_ids = group_ids
        self.requires_deploy = requires_deploy
        self.status = status
        self.auto_discovered = auto_discovered
        self.average_eps = average_eps
        self.creation_date = creation_date
        self.modified_date = modified_date
        self.last_event_time = last_event_time
        self.wincollect_internal_destination_id = wincollect_internal_destination_id
        self.wincollect_external_destination_ids = wincollect_external_destination_ids
        self.legacy_bulk_group_name = legacy_bulk_group_name
        self.sending_ip = sending_ip
        self.parsing_order = parsing_order
