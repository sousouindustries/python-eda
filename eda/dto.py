from collections import namedtuple

from marshmallow.fields import *
from marshmallow import Schema as Adapter
from marshmallow.schema import SchemaMeta


class ImmutableDict(dict):

    def __setitem__(self, key, value):
        raise NotImplementedError


class DataTransferObject(Adapter):

    def __init__(self, *args, **kwargs):
        super(DataTransferObject, self).__init__(*args, **kwargs)
        self.__namedtuple__ = namedtuple('DTO', list(self._declared_fields.keys()))

    def load(self, *args, **kwargs):
        params = super(DataTransferObject, self).load(*args, **kwargs)
        for key, value in list(params.items()):
            if isinstance(key, dict):
                params[key] = ImmutableDict(value)

            if isinstance(key, list):
                params[key] = tuple(value)

        return self.__namedtuple__(**params)
