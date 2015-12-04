#/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Jordi Ortiz (nenjordi@gmail.com)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import notmuch
import time
import os

db = notmuch.Database()
db.__init__()

messageids = []
importantaddresses = ['skarmeta@um.es', 'pedromj@um.es', 'edumart@um.es', 'emtg@um.es', 'angeles.ros@gmail.com', 'angelesrosg@gmail.com']

query = db.create_query('tag:inbox and tag:unread and date:yesterday..now')
messages = list(query.search_messages())
for m in messages:
    if not messageids.__contains__(m.get_message_id()):
        important = False
        for addr in importantaddresses:
            if m.get_header('from').find(addr) != -1:
                os.system('notify-send -t 30000 -u critical "notmuch" "' + m.get_header('from') + ' ' + m.get_header('subject')  + '"')
                #os.system('twmnc -t notmuch -c "' + m.get_header('from') + ' ' + m.get_header('subject')  + '" -d 10000 --fg red --bg white')
                important = True
        if not important:
            os.system('notify-send -t 10000 -u low "notmuch" "' + m.get_header('from') + ' ' + m.get_header('subject')  + '"')
            #os.system('twmnc -t notmuch -c "' + m.get_header('from') + ' ' + m.get_header('subject')  + '" -d 3000 --fg blue --bg gray')
    messageids.append(m.get_message_id())


# TODO: Save message list to database and recover at the beginning

