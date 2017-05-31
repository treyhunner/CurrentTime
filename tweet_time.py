#!/usr/bin/env python3.6
"""
Tweet current time:

    $ python3 tweet_time.py

Time is rounded down to the half hour.

"""
from datetime import datetime
import os
import tweepy


EMOJI = {
    '01:00': '\N{CLOCK FACE ONE OCLOCK}',
    '01:30': '\N{CLOCK FACE ONE-THIRTY}',
    '02:00': '\N{CLOCK FACE TWO OCLOCK}',
    '02:30': '\N{CLOCK FACE TWO-THIRTY}',
    '03:00': '\N{CLOCK FACE THREE OCLOCK}',
    '03:30': '\N{CLOCK FACE THREE-THIRTY}',
    '04:00': '\N{CLOCK FACE FOUR OCLOCK}',
    '04:30': '\N{CLOCK FACE FOUR-THIRTY}',
    '05:00': '\N{CLOCK FACE FIVE OCLOCK}',
    '05:30': '\N{CLOCK FACE FIVE-THIRTY}',
    '06:00': '\N{CLOCK FACE SIX OCLOCK}',
    '06:30': '\N{CLOCK FACE SIX-THIRTY}',
    '07:00': '\N{CLOCK FACE SEVEN OCLOCK}',
    '07:30': '\N{CLOCK FACE SEVEN-THIRTY}',
    '08:00': '\N{CLOCK FACE EIGHT OCLOCK}',
    '08:30': '\N{CLOCK FACE EIGHT-THIRTY}',
    '09:00': '\N{CLOCK FACE NINE OCLOCK}',
    '09:30': '\N{CLOCK FACE NINE-THIRTY}',
    '10:00': '\N{CLOCK FACE TEN OCLOCK}',
    '10:30': '\N{CLOCK FACE TEN-THIRTY}',
    '11:00': '\N{CLOCK FACE ELEVEN OCLOCK}',
    '11:30': '\N{CLOCK FACE ELEVEN-THIRTY}',
    '12:00': '\N{CLOCK FACE TWELVE OCLOCK}',
    '12:30': '\N{CLOCK FACE TWELVE-THIRTY}',
}


CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('TWITTER_ACCESS_KEY')
ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def tweet_time(now):
    """Tweet given time (rounded down to the half hour)."""
    now = now.replace(minute=now.minute // 30)
    time24 = now.strftime('%H:%M')
    time_emoji = EMOJI[now.strftime('%I:%M')]
    message = f"{time24} {time_emoji}"
    print(f"Tweeting: {message}")
    api.update_status(status=message)


if __name__ == "__main__":
    tweet_time(datetime.now())
