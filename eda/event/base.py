from eda.event.meta import EventMeta


class Event(metaclass=EventMeta):
    """The base class for all enterprise-level events.

    An enterprise-level event is a representation of a fact that happened
    that is interesting to the enterprise. It describes a fact as detailed
    as possible, so that subscribers do not have to invoke additional services
    to process the incoming event, but at the same time do not have the
    data-requirements of a certain client system creep into the event
    model.

    Events may be specified using the following syntax:

    .. code:: python

        import eda

        class OrderPlaced(eda.Event):
            order_id = eda.fields.Integer(required=True)
            customer_id = eda.fields.Integer(required=True)

    """
    ValidationError = type('ValidationError', (Exception,), {})

    @property
    def header(self):
        return self._header

    @property
    def body(self):
        return self._body

    def __init__(self, **params):
        self._body, errors = self._adapter.load(params)
        if errors:
            raise self.ValidationError
