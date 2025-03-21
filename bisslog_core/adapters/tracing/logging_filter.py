import logging


class BisslogFilterLogging(logging.Filter):
    def filter(self, record):
        if not hasattr(record, "transaction_id"):
            record.transaction_id = "service-logging"
        if not hasattr(record, "checkpoint_id"):
            record.checkpoint_id = "unknown-checkpoint"
        return True
