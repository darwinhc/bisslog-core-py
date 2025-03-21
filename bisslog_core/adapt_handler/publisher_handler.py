
from bisslog_core.adapt_handler.adapt_handler import AdaptHandler
from bisslog_core.adapters.base_adapter import BaseAdapter
from bisslog_core.ports.publisher import IPublisher


class PublisherHandler(AdaptHandler):
    pass


bisslog_pubsub = PublisherHandler("publisher-default")
