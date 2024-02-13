# coding: utf-8

"""
    Turing Minimal Openapi Spec for SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Event(BaseModel):
    """
    Event
    """ # noqa: E501
    id: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    version: Optional[StrictInt] = None
    event_type: Optional[StrictStr] = None
    stage: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "version", "event_type", "stage", "message"]

    @field_validator('event_type')
    def event_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('info', 'error'):
            raise ValueError("must be one of enum values ('info', 'error')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "updated_at",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "version": obj.get("version"),
            "event_type": obj.get("event_type"),
            "stage": obj.get("stage"),
            "message": obj.get("message")
        })
        return _obj


