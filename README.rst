README
======

Phox version 0.0.1

.. contents::

Description
-----------

Phox is a Twilio endpoint using the Flask Python web framework.


What is a Twilio endpoint?
--------------------------

When you set up your telephone numbers with Twilio, you must provide a URL for Twilio to hit each time you receive a phone call. This can be a static text file containing TwiML or an application server responding with TwiML etc.


Phox can be used as a basic Twilio endpoint or to start your own applications.

Running
-------


1) Modify the functions 'voice' and 'sms' to control the call flow:

phox/views/main.py

2) Run it:

./manage.py runserver

3) Go to twilio.com and configure yourphone number URL with:

http://yourserver.com/voice
http://yourserver.com/sms

Use the excellent http://progrium.com/localtunnel/ to test Phox without uploading to a production server on the Internet.




Features in first release
-------------------------

 * Secure - Phox ensures API requests are coming from Twilio
 * Using Flask makes it easy to customize voice and SMS functionality
 * Controllable via command-line with a twerp plugin


TODO
----

See http://blog.cakebread.info/

