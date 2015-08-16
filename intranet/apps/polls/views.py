# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from intranet import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

logger = logging.getLogger(__name__)


@login_required
def polls_view(request):

    if settings.PRODUCTION and not request.user.has_admin_permission('polls'):
        return render(request, "polls/not_ready.html")

    return render(request, "polls/polls.html")
