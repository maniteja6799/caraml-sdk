# coding: utf-8

"""
    Turing Minimal Openapi Spec for SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
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


class EnsemblerConfigKind(str, Enum):
    """
    EnsemblerConfigKind
    """

    """
    allowed enum values
    """
    BATCHENSEMBLINGJOB = 'BatchEnsemblingJob'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EnsemblerConfigKind from a JSON string"""
        return cls(json.loads(json_str))


