
from bisslog_core.adapt_handler.adapt_handler import AdaptHandler
from bisslog_core.adapters.base_adapter import BaseAdapter
from bisslog_core.ports.publisher import IPublisher



class PublisherBlank(IPublisher, BaseAdapter):

    def __call__(self, queue_name: str, body: object, partition: str = None, *args, **kwargs) -> None:
        separators = "#" * 80
        string = (f"\n{separators}\nPublishing on {queue_name} with partition" +
                  f" {partition}:\nbody: {body}\n{separators}")
        self.log.info(string, checkpoint_id="bisslog-blank-publisher")


class PublisherHandler(AdaptHandler):

    def generate_blank_adapter(self, item_name: str):
        return PublisherBlank()


bisslog_pubsub = PublisherHandler("publisher-handler-default")
