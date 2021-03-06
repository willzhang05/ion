# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import Announcement, AnnouncementRequest
from ..users.models import User
from ..users.forms import SortedTeacherMultipleChoiceField


class AnnouncementForm(forms.ModelForm):
    """
    A form for generating an announcement.

    """

    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        self.fields["notify_post"].help_text = (
            "If this box is checked, students who have signed up for notifications "
            "will receive an email. If the announcement is public, a link will be posted on Twitter."
        )

        self.fields["notify_email_all"].help_text = (
            "This will send an email notification to all of the users who can see this post. This option "
            "does NOT take users' email notification preferences into account, so please use with care."
        )

    expiration_date = forms.DateTimeInput()
    notify_email_all = forms.BooleanField(required=False, label="Send Email to All")

    class Meta:
        model = Announcement
        fields = [
            "title",
            "author",
            "content",
            "groups",
            "expiration_date",
            "notify_post",
            "notify_email_all",
            "pinned"
        ]


class AnnouncementRequestForm(forms.ModelForm):
    """
    A form for generating an announcement request.

    """

    def __init__(self, *args, **kwargs):
        super(AnnouncementRequestForm, self).__init__(*args, **kwargs)
        self.fields["title"].help_text = (
            "The title of the announcement that will appear on Intranet. Please enter "
            "a title more specific than just \"[Club name]'s Intranet Posting\'."
        )
        self.fields["author"].help_text = (
            "If you want this post to have a custom author entry, such as "
            "\"Basket Weaving Club\" or \"TJ Faculty,\" enter that name here. "
            "Otherwise, your name will appear in this field automatically.")
        self.fields["content"].help_text = (
            "The contents of the news post which will appear on Intranet."
        )
        self.fields["expiration_date"].help_text = (
            "An expiration date for when this post should expire (be not visible). "
            "To never expire, keep the default value of January 1st, 3000."
        )
        self.fields["notes"].help_text = (
            "Any information about this announcement you wish to share with the Intranet "
            "administrators and teachers selected above. If you want to restrict this posting "
            "to a specific group of students, such as the Class of 2016, enter that request here."
        )
        self.fields["teachers_requested"] = SortedTeacherMultipleChoiceField(queryset=User.objects.get_teachers_sorted())
        self.fields["teachers_requested"].label = "Sponsor"
        self.fields["teachers_requested"].help_text = (
            "The teacher(s) who will approve your announcement. They will be sent an email "
            "with instructions on how to approve this post. Please do not select more than "
            "one or two."
        )

    class Meta:
        model = AnnouncementRequest
        fields = [
            "title",
            "author",
            "content",
            "expiration_date",
            "teachers_requested",
            "notes"
        ]
