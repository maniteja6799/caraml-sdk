# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities

    The version of the OpenAPI document: 0.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ValueType(str, Enum):
    """
    ValueType
    """

    """
    allowed enum values
    """
    FLOAT64 = "float64"
    INT64 = "int64"
    BOOLEAN = "boolean"
    STRING = "string"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ValueType from a JSON string"""
        return cls(json.loads(json_str))
