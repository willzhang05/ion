# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

To run the following tests, use "./manage.py test intranet.apps.eighth"
"""

from datetime import date
from django.db import transaction
from django.test import TransactionTestCase
from ..users.models import User
from .models import EighthBlock, EighthActivity, EighthScheduledActivity, EighthSignup


class EighthTest(TransactionTestCase):
    reset_sequences = True

    def test_signups(self):
        """Do some sample signups.
        """

        print EighthActivity.objects.all()

        user1 = User.objects.create(username="user1")
        block1 = EighthBlock.objects.create(
            date=date(2015, 01, 01),
            block_letter="A"
        )

        act1 = EighthActivity.objects.create(name="Test Activity 1")
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
                                  .filter(block=schact.block)
                                  .count()), 1)
        
        verifySignup(user1, schact1)