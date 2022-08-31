# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class ScaleneTriangle(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        additional_properties = schemas.AnyTypeSchema
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                class properties:
                    
                    
                    class triangleType(
                        schemas.SchemaEnumMakerClsFactory(
                            enum_value_to_name={
                                "ScaleneTriangle": "SCALENE_TRIANGLE",
                            }
                        ),
                        schemas.StrSchema
                    ):
                        
                        @classmethod
                        @property
                        def SCALENE_TRIANGLE(cls):
                            return cls("ScaleneTriangle")
                    __annotations__ = {
                        "triangleType": triangleType,
                    }
                additional_properties = schemas.AnyTypeSchema
            
            triangleType: typing.Union[MetaOapg.properties.triangleType, schemas.Unset]
            
            @typing.overload
            def __getitem__(self, name: typing.Literal["triangleType"]) -> typing.Union[MetaOapg.properties.triangleType, schemas.Unset]: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
            
            def __getitem__(self, name: typing.Union[str, typing.Literal["triangleType"], ]):
                # dict_instance[name] accessor
                if not hasattr(self.MetaOapg, 'properties') or name not in self.MetaOapg.properties.__annotations__:
                    return super().__getitem__(name)
                try:
                    return super().__getitem__(name)
                except KeyError:
                    return schemas.unset
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                triangleType: typing.Union[MetaOapg.properties.triangleType, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    triangleType=triangleType,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @property
        @functools.cache
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                TriangleInterface,
                cls.all_of_1,
            ]

    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        if not hasattr(self.MetaOapg, 'properties') or name not in self.MetaOapg.properties.__annotations__:
            return super().__getitem__(name)
        try:
            return super().__getitem__(name)
        except KeyError:
            return schemas.unset

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'ScaleneTriangle':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.triangle_interface import TriangleInterface
