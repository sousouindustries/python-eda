from libsousou.meta import hybrid_property

from eda.exc import UnexpectedEventFormat


class Event:
    RESERVED = set([
        'event_type','metadata','RESERVED','_params','_event_type',
        'event_id','event_timestamp'])
    _event_type = None
    _params = None
    _initialized = False

    @hybrid_property
    def event_type(self):
        return self._event_type

    def __init__(self, event_type, params):
        self._event_type = event_type
        self._params = params
        self._initialized = True

    def __setattr__(self, attname, value):
        if self._initialized:
            raise AttributeError('{0} objects are immutable.'.format(self._event_type))
        super(Event, self).__setattr__(attname, value)

    def __getattr__(self, attname):
        if attname not in (set(self._params.keys()) | self.RESERVED):
            raise UnexpectedEventFormat(attname)
        return self._params[attname]

    def __repr__(self):
        params = ', '.join(
            ["{0}={1}".format(x, repr(y)) for x,y in self._params.items()])
        return "{0}({1})".format(self._event_type, params)


class EventFactory:
    """A conveniance factory that allows the creation of events by
    exposing the path of the identifier as attributes, similar to
    the :func:`func()` function in :mod:`sqlalchemy`.
    """

    @property
    def event_type(self):
        return self.path

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
