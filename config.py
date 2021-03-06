###
# Copyright (c) 2013-2014, spline
# All rights reserved.
###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Stock', True)


Stock = conf.registerPlugin('Stock')
conf.registerChannelValue(Stock, 'msgUsersOutput', registry.Boolean(False, """Message users in specific channel all output?"""))


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=179:
