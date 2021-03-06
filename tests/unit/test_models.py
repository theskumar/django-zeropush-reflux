# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# # Third Party Stuff
import pytest

# # Clustr Stuff
from zeropush.models import PushDevice
import zeropush

from .. import factories as f

pytestmark = pytest.mark.django_db


def test_register_device(settings):
    # given two user and one device
    # device should get attached to only user
    users = f.UserFactory.create_batch(2)

    zeropush.register_apple_device(users[0], 'abc')
    assert PushDevice.objects.count() == 1
    zeropush.register_apple_device(users[1], 'abc')
    assert PushDevice.objects.count() == 1

    zeropush.deregister_apple_device(users[1], 'abc')
    assert PushDevice.objects.count() == 0
