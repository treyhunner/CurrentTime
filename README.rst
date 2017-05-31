CurrentTime
===========

Twitter bot that tweets the current time.

Tweet current time:

.. code-block:: bash

    $ python3 tweet_time.py

Tweet specific time:

.. code-block:: bash

    $ python3 tweet_time.py 19:00

The time will only be tweeted if on the hour (minutes is ``00``) or 30 minutes
past (minutes is ``30``).
