from sarna.model.enums.base_choice import BaseChoice
from sarna.model.enums.language import Language


class Secuence(BaseChoice):
    _init_ = "value translation"
    Image = 1, {
        Language.English: 'Image',
        Language.Spanish: 'Imagen'
    }
    Table = 2, {
        Language.English: 'Table',
        Language.Spanish: 'Tabla'
    }
