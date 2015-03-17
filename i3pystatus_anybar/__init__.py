from i3pystatus import IntervalModule

import asyncio
import threading
import collections


class AnyBar(IntervalModule):

    """
    Shows dot with given color
    """

    colors = {
        "black": "#444444",  # 4C4C4C
        "black_alt": "#FFFFFF",
        "blue": "#4A90E2",
        "cyan": "#27F2CB",
        "exclamation": "#DE504C",  # vary
        "green": "#80EB0C",
        "orange": "#FF9F00",
        "purple": "#9013FE",
        "question": "#4C4C4C",  # vary
        "question_alt": "#FFFFFF",
        "red": "#CF0700",
        "white": "#4C4C4C",  # border
        "white_alt": "#FFFFFF",
        "yellow": "#FFEC00",
    }
    color = '#444444'
    interval = 1

    settings = (
        ("port", "port to listen"),
        ("color", "standard color"),
    )

    #required = ("command",)

    def on_data(self, data, addr):
        i = data.decode().strip()
        self.color = self.colors.get(i, '#ff0000')

    def init(self):
        loop = getattr(self.__class__, "loop", asyncio.get_event_loop())

        port = int(getattr(self, 'port', 1738))

        proto = type('AnyBarProto%d' % port, tuple(), {
            'connection_made': lambda s, t: None,
            'datagram_received': self.on_data
        })
        listen = loop.create_datagram_endpoint(
            proto, local_addr=('127.0.0.1', port))
        loop.create_task(listen)
        #transport, protocol = loop.run_until_complete(listen)
        if not hasattr(self.__class__, "loop_thread"):
            self.__class__.loop_thread = threading.Thread(
                target=loop.run_forever)
            self.__class__.loop_thread.start()

    def run(self):
        self.output = {
            "full_text": "●",
            "color": self.color
        }


def anybar_append(status, **kw):
    "keys for kw is port and color"
    anybar = AnyBar(**kw)
    anybar.registered(status.modules.status_handler)
    collections.UserList.append(status.modules, anybar)
    return anybar


def anybar_remove(status, anybar):
    collections.UserList.remove(status.modules, anybar)
