import inflection
from flask_migrate import Migrate
from flask_restful import fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Query, ColumnProperty, RelationshipProperty

from sarna.core import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

__all__ = ['db', 'Base']


@app.after_request
def auto_commit(resp):
    db.session.commit()
    return resp


class Base(object):
    query: Query

    _exclude_attrs = None
    _include_attrs = None

    @declared_attr
    def __tablename__(cls):
        return inflection.underscore(cls.__name__).lower()

    def __init__(self, *args, **kwargs):
        db.Model.__init__(self, *args, **kwargs)

    def set(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def to_dict(self):
        d = {}
        for attr in self.__mapper__.attrs.keys():
            d[attr] = getattr(self, attr)

        return d

    @classmethod
    def _get_serializable_attrs(cls):
        ret = set(cls._include_attrs or cls.__mapper__.attrs.keys())
        ret = ret.difference(set(cls._exclude_attrs or []))
        return sorted(ret)

    @classmethod
    def rest_fields(cls, visited=None):
        visited = visited or set()

        if cls in visited:
            return None

        visited.add(cls)

        field_type_map = {
            Integer: fields.Integer,
            String: fields.String,
        }

        ret = dict()
        for attr in cls._get_serializable_attrs():
            prop = cls.__mapper__.attrs.get(attr)
            if isinstance(prop, ColumnProperty):
                ret[prop.key] = field_type_map.get(prop.expression.type.__class__, fields.String)()
            elif isinstance(prop, RelationshipProperty):
                nested_type = prop.mapper.class_.rest_fields(visited)
                if nested_type:
                    if prop.uselist:
                        ret[prop.key] = fields.List(fields.Nested(nested_type))
                    else:
                        ret[prop.key] = fields.Nested(nested_type)

        visited.remove(cls)
        return ret

    def delete(self, synchronize_session=False):
        self.query.delete(synchronize_session=synchronize_session)
