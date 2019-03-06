import inflection
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Query

from sarna.core import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

__all__ = ['db', 'Base']


@app.after_request
def auto_commit(resp):
    db.session.commit()
    return resp


class Base(dict):
    query: Query

    @declared_attr
    def __tablename__(cls):
        return inflection.underscore(cls.__name__).lower()

    def __init__(self, *args, **kwargs):
        db.Model.__init__(self, *args, **kwargs)
        super().__init__(**kwargs)

    def set(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def to_dict(self):
        return self

    def __len__(self):
        return len(self.__mapper__.attrs.keys())

    def __getitem__(self, key):
        if key not in self:
            raise KeyError('key ot found', key)
        return getattr(self, key, None)

    def __setitem__(self, key, value):
        if key not in self:
            raise KeyError('Invalid key for current schema', key)
        setattr(self, key, value)

    def __delitem__(self, key):
        if key not in self:
            raise KeyError('key ot found', key)
        setattr(self, key, None)

    def __iter__(self):
        return iter(self.__mapper__.attrs.keys())

    def __contains__(self, item):
        return item in self.__mapper__.attrs.keys()

    def keys(self):
        return self.__mapper__.attrs.keys()

    def values(self):
        for attr in self.__mapper__.attrs.keys():
            yield getattr(self, attr)

    def items(self):
        for attr in self.__mapper__.attrs.keys():
            yield attr, getattr(self, attr)

    def __hash__(self):
        h = 0
        for k, v in self.items():
            h = h ^ hash(v)
        return h

    def __repr__(self):
        return "{{{}}}".format(
            ",".join(
                "{}: {}".format(k, v) for k, v in self.items()
            )
        )

    def delete(self, synchronize_session=False):
        pk = {
            k.name: getattr(self, k.name)
            for k in self.__mapper__.primary_key
        }
        self.query.filter_by(**pk).delete(synchronize_session=synchronize_session)
