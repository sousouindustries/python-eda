from libsousou.meta import hybrid_property


class EventHandler:
    _handles = set()

    @hybrid_property
    def events(self):
        return self._handles

    def is_valid_event(self, event):
        """Return a boolean indicating if the handler can process the given
        `event`, based on its type.
        """
        return event.event_type in self._handles

    def can_handle(self, event):
        return True

    def handle(self, event):
        pass


class AnyEventHandler(EventHandler):
    """A :class:`EventHandler` implementation that handles any
    event.
    """

    def is_valid_event(self, event):
        return True


def handles(event_class):
    """A class-decorator that indicates an event type that can be
    handled by the decorated handler class.
    """

    def f(cls):
        cls._handles.add(event_class.event_type)
        return cls

    return f
