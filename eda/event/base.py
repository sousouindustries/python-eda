


class Event:
    RESERVED = set(['_event_type','metadata'])

    def __init__(self, event_type, params):
        self._event_type = event_type
        self._params = params

    def __repr__(self):
        params = ', '.join(
            ["{0}={1}".format(x, repr(y)) for x,y in self._params.items()])
        return "{0}({1})".format(self._event_type, params)


class EventFactory:
    """A conveniance factory that allows the creation of events by
    exposing the path of the identifier as attributes, similar to
    the :func:`func()` function in :mod:`sqlalchemy`.
    """

    def __init__(self, path=None):
        self.path = path

    def _append(self, part):
        p = part if self.path is None else '.'.join([self.path, part])
        return EventFactory(p)

    def __getattr__(self, attname):
        return self._append(attname)

    def __repr__(self):
        return "<EventType: {0}>".format(self.path)

    def __call__(self, **kwargs):
        for key in kwargs.keys():
            if key.startswith('_') or (key in Event.RESERVED):
                raise ValueError("{0} is a reserved attribute.".format(key))

        return Event(self.path, kwargs)


events = EventFactory()
