# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This file contains tests for the eighth module.

To run the following tests, use "./manage.py test intranet.apps.eighth"
"""

from datetime import date
from django.db import transaction
from django.test import TestCase
from ..users.models import User
from .models import EighthBlock, EighthActivity, EighthScheduledActivity, EighthSignup, EighthRoom


class EighthTest(TestCase):

    def test_signups(self):
        """Do some sample signups.
        """

        user1 = User.objects.create(username="user1")
        block1 = EighthBlock.objects.create(
            date=date(2015, 01, 01),
            block_letter="A"
        )
        room1 = EighthRoom.objects.create(name="room1")

        act1 = EighthActivity.objects.create(name="Test Activity 1")
        act1.rooms.add(room1)
        schact1 = EighthScheduledActivity.objects.create(
            activity=act1,
            block=block1
        )

        def verifySignup(user, schact):
            old_count = (schact.eighthsignup_set
                               .count())
            schact.add_user(user)
            self.assertEqual((schact.eighthsignup_set
                                    .count()), old_count + 1)
            self.assertEqual((user.eighthsignup_set
                                  .filter(scheduled_activity__block=schact.block)
                                  .count()), 1)
        
        verifySignup(user1, schact1)
