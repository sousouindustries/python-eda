from libsousou.meta import hybrid_property


class EventHandler:
    _handles = set()
    ANY = '*'

    @hybrid_property
    def events(self):
        return self._handles

    def is_valid_event(self, event):
        """Return a boolean indicating if the handler can process the given
        `event`, based on its type.
        """
        return event.event_type in self.events

    def can_handle(self, event):
        return True

    def handle(self, event):
        raise NotImplementedError("Subclasses must override this method.")


class AnyEventHandler(EventHandler):
    """A :class:`EventHandler` implementation that handles any
    event.
    """

    @hybrid_property
    def events(self):
        return self.ANY

    def is_valid_event(self, event):
        """Return a boolean indicating if the handler can process the given
        `event`, based on its type.
        """
        return True


def handles(event_class):
    """A class-decorator that indicates an event type that can be
    handled by the decorated handler class.
    """

    def f(cls):
        cls._handles.add(event_class.event_type)
        return cls

    return f
