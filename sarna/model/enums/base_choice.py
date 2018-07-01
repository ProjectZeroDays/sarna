from aenum import OrderedEnum


class BaseChoice(OrderedEnum):
    @classmethod
    def choices(cls):
        return [(None, "---")] + [cls.choice(elem) for elem in cls]

    @classmethod
    def choice(cls, elem):
        if isinstance(elem, cls):
            desc = getattr(elem, 'desc', None)
            name = getattr(elem, 'code', elem.name.replace("_", " "))
            if desc:
                return elem, "{} - {}".format(name, desc)
            else:
                return elem, name
        elif elem:
            return cls[elem], cls[elem].name.replace("_", " ")
        else:
            return None

    @classmethod
    def coerce(cls, item):
        if not item or item == 'None':
            return None

        return cls[item.replace(" ", "_")] if not isinstance(item, cls) else item

    def __str__(self):
        return self.name.replace("_", " ")
