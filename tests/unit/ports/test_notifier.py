import pytest
from abc import ABC
from bisslog.ports.notifier import INotifier
from typing import Any


class DummyNotifier(INotifier):
    def __call__(self, notification_obj: object) -> None:
        self.last_notification = notification_obj


@pytest.fixture
def notifier():
    return DummyNotifier()


def test_inotifier_call_stores_notification(notifier):
    payload = {"message": "Test"}
    notifier(payload)

    assert notifier.last_notification == payload


def test_inotifier_is_subclass_of_abc():
    assert issubclass(INotifier, ABC)


def test_dummy_notifier_is_instance_of_inotifier(notifier):
    assert isinstance(notifier, INotifier)
