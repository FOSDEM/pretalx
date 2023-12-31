from pretalx.common.signals import EventPluginSignal

footer_link = EventPluginSignal()
"""
This signal allows you to add links to the footer of an event page. You are
expected to return a dictionary containing the keys ``label`` and ``url``.

As with all plugin signals, the ``sender`` keyword argument will contain the event.
Additionally, the signal will be called with the ``request`` it is processing.
"""

cfp_steps = EventPluginSignal()
"""
This signal allows you to add CfP steps of your own. This signal will expect a
list of ``pretalx.cfp.flow.BaseCfPStep`` objects. The integration of CfP steps
in the CfP workflow is currently considered **unstable** and may change without
notice between versions.

As with all plugin signals, the ``sender`` keyword argument will contain the event.
Additionally, the signal will be called with the ``request`` it is processing.
"""

html_above_submission_list = EventPluginSignal()
"""
This signal is sent out to display additional information on the personal user
submission list page, above the submission list.

As with all plugin signals, the ``sender`` keyword argument will contain the event.
Additionally, the signal will be called with the ``request`` it is processing.
Thereceivers are expected to return HTML.
"""

html_above_profile_page = EventPluginSignal()
"""
This signal is sent out to display additional information on the personal user
profile page, above the submission list.

As with all plugin signals, the ``sender`` keyword argument will contain the event.
Additionally, the signal will be called with the ``request`` it is processing.
Thereceivers are expected to return HTML.
"""
html_head = EventPluginSignal()
"""
This signal allows you to put code inside the HTML ``<head>`` tag of every page
in the frontend (i.e. everything not in the organiser backend). You will get the request
as the keyword argument ``request`` and are expected to return plain HTML.

As with all plugin signals, the ``sender`` keyword argument will contain the event.
Additionally, the signal will be called with the ``request`` it is processing.
Thereceivers are expected to return HTML.
"""
html_below_track = EventPluginSignal()
"""
This signal allows you to put code inside the tracks page. The receiver should export html,
it will contain the track when called.
"""
on_save_track = EventPluginSignal()
"""
This signal is triggered when the Track form is received and is triggered after saving it.
"""
extra_user_settings = EventPluginSignal()
"""
This signal allow one to enter extra options in the user profile screen.
"""
on_save_user = EventPluginSignal()
