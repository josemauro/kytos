# -*- coding: utf-8 -*-
"""Module with Kyco Events"""

from datetime import datetime

# Base Events Classes


class KycoEvent(object):
    """Base Event class

    The event data will be passed on the content attribute, which should be a
    dictionary.

    Args:
        content (dict): Dictionary with all event informations
    """
    def __init__(self, content, connection=None, timestamp=datetime.now()):
        self.content = content
        self.connection = connection
        self.timestamp = timestamp


class KycoCoreEvent(KycoEvent):
    """Kyco Core Event base class.

    Events generated by Kyco or any Core NApps"""
    def __init__(self, content, connection=None, timestamp=datetime.now()):
        super().__init__(content, connection, timestamp)
        self.context = 'core'


class KycoMsgEvent(KycoEvent):
    """Base class for all Events related to OpenFlow Messages"""
    def __init__(self, content, connection=None, timestamp=datetime.now()):
        super().__init__(content, connection, timestamp)
        self.context = 'message'


class KycoAppEvent(KycoEvent):
    """Base class for all Events generated to/by Apps that are not OpenFlow
    Messages"""
    def __init__(self, content, connection=None, timestamp=datetime.now()):
        super().__init__(content, connection, timestamp)
        self.context = 'apps'


class KycoShutdownEvent(KycoEvent):
    def __init__(self, content={}, connection=None, timestamp=datetime.now()):
        super().__init__(content, connection, timestamp)


class KycoRawEvent(KycoCoreEvent):
    """Kyco Event generated by incoming packets from the network.

    This needs to be handled and a new event will be generated by the handler.
    Mainly this will have an OpenFlowMessage or will be an event about a new
    incoming TCP connection.
    """
    pass


# Core Generated Events

class KycoNewConnection(KycoRawEvent):
    """A new connection was stabilished"""
    pass


class KycoConnectionLost(KycoRawEvent):
    """A connection was lost"""
    pass


class KycoSwitchUp(KycoCoreEvent):
    """A connection with a switch was stabilished"""
    pass


class KycoSwitchDown(KycoCoreEvent):
    """A connection with a switch was lost"""
    pass


class KycoRawOpenFlowMessage(KycoRawEvent):
    """New OpenFlowMessage received

    This event contains the header of the message and also the body in binary
    format, that still needs to be unpacked."""
    pass


class KycoAppInstalled(KycoCoreEvent):
    pass


class KycoAppLoaded(KycoCoreEvent):
    pass


class KycoAppUninstalled(KycoCoreEvent):
    pass


class KycoAppUnloaded(KycoCoreEvent):
    pass


class KycoServerDown(KycoCoreEvent):
    pass


class KycoMessageIn(KycoMsgEvent):
    pass


class KycoMessageOut(KycoMsgEvent):
    pass


class KycoMessageInHello(KycoMessageIn):
    pass


class KycoMessageOutHello(KycoMessageOut):
    pass


class KycoMessageInEchoRequest(KycoMessageIn):
    pass


class KycoMessageOutEchoReply(KycoMessageOut):
    pass


class KycoMessageOutFeaturesRequest(KycoMessageOut):
    pass


class KycoMessageOutSetConfig(KycoMessageOut):
    pass
