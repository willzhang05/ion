# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import user_passes_test


def admin_required(group):
    """Decorator that requires the user to be in a certain admin group.
    For example, @admin_required("polls") would check whether a user is
    in the "admin_polls" group or in the "admin_all" group.

    """
    def in_admin_group(user):
        return user.is_authenticated() and user.has_admin_permission(group)

    return user_passes_test(in_admin_group)


# Convenience decorators for some of the apps
eighth_admin_required = admin_required("eighth")
announcements_admin_required = admin_required("announcements")
attendance_taker_required = user_passes_test(lambda u: u.is_attendance_taker)