from enum import StrEnum


class ObjectModel(StrEnum):

    CUBE = 'cube'
    VIEW = 'view'
    DIMENSION = 'dimension'
    HIERARCHY = 'hierarchy'
    ELEMENT = 'element'
    SUBSET = 'subset'
    CHORE = 'chore'
    PROCESS = 'process'