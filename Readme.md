# notmuch-notifier
Notification python script to receive notifications via libnotify from notmuch search

The idea is to have a script to be called periodically (probably with cron) that checks for a notmuch search and notifies just once messages listed. In addition some highlighting options are added in config file.

## Dependencies
* notmuch
* python-notify2

## notmuch-notifier.conf
```
[file]
db = /tmp/notmuch-notifier.db

[notmuch]
filter = tag:inbox and tag:unread and date:yesterday..now

[notifications]
highlight = important@domain.net, important2@domain2.net
highlight_time = 30000
time = 10000
app = notmuch
summary_length = 200
```

* db is the file where the message-ids already shown will be stored
* filter is the notmuch filter (in the sample any message arrived today to inbox and marked as unread)
* highlight is a list of address to be highlighted and notified as critical to libnotify
* highlight_time is the time to show messages from previous field addresses
* time is the default time to show nofitications
* app is the app name to send to libnotify2
* summary_length is the ammount of bytes of the body to be shown in the notification
