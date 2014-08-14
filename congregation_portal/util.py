# -*- coding: utf-8 -*-

from congregation_portal.models import Congregation


def clean_phone(phone):
    return phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

congregations = Congregation.objects.all()

msgs = {'msg_login': u'User does not exist or password was incorrect.',
        'msg_insufficient_privileges': u'Sorry. That action is not allowed.'}
