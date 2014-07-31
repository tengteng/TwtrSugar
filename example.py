
# easy_install twitter.

from twitter import *

t = Twitter(auth=OAuth('2694141234-Fng4bHcVOfEBhNq2LD9yaH9YPCTyP9Ev5qqA8B4',
                       'jIp0TI5bgoXIGABnbRdd6S4MO9bN89aKVPsP3VPpiOY2z',
                       'BnlN6PJmIn1YWgxIVfbQm0gGy',
                       'CVJc1vtEYWQjcXsrOhpaS6SwEbbbekchN8e6hYFtq6de7PQIW1'))
x = t.statuses.home_timeline()
x[0]['user']['followers_count']
x[0]['user']['friends_count']
