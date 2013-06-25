#!/usr/bin/env python
# coding: utf-8
import sys
import gntp.notifier

growler = gntp.notifier.GrowlNotifier(
    applicationName = 'Growl Python Notifier',
    notifications = ['python_note'],
    defaultNotifications = ['python_note']
)

growler.register()

def growl(title, message):
    global growler
    growler.notify(noteType='python_note', title=title, description=message)

    
def main():
    growl = gntp.notifier.GrowlNotifier(
        applicationName = 'Growl Python Notifier',
        notifications = ['cli_note'],
        defaultNotifications = ['cli_note']
    )

    growl.register()
    if len(sys.argv) < 3:
        usage()
    if len(sys.argv) > 3:
        status = None
        if len(sys.argv)==4:
            try:
                status = int(sys.argv[3])
            except ValueError:
                pass
        from subprocess import call
        status = status if status is not None else call(sys.argv[3:], shell=True)
        if not status: # Pass
            growl.notify(noteType='cli_note', title=sys.argv[1], description='%s succeeded' %sys.argv[2])
        else:
            growl.notify(noteType='cli_note', title=sys.argv[1], description='%s failed' %sys.argv[2])
    else:
        growl.notify(noteType="cli_note", title=sys.argv[1], description=sys.argv[2])


def usage():
    print "growl <title> <message> [<cmd>]"


if __name__ == "__main__":
    main()
