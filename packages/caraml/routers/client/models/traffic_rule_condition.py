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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from routers.client.models.field_source import FieldSource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TrafficRuleCondition(BaseModel):
    """
    TrafficRuleCondition
    """ # noqa: E501
    field_source: FieldSource
    field: StrictStr = Field(description="For HTTP_JSON protocol, the valid `field_source` are `header` and `payload`. Whereas, for UPI_V1 protocol the valid `field_source` are `header` and `prediction_context`. If `field_source` is `header`, then `field` should contain the name of the request header. If `field_source` is `payload`, then `field` should be a valid json path. If `field_source` is `prediction_context`, then `field` should contain variable name stored in `prediction_context` field of the incoming request. ")
    operator: StrictStr
    values: List[StrictStr]
    __properties: ClassVar[List[str]] = ["field_source", "field", "operator", "values"]

    @field_validator('operator')
    def operator_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('in'):
            raise ValueError("must be one of enum values ('in')")
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
        """Create an instance of TrafficRuleCondition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TrafficRuleCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "field_source": obj.get("field_source"),
            "field": obj.get("field"),
            "operator": obj.get("operator"),
            "values": obj.get("values")
        })
        return _obj


