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


class EnumTest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "enum_string_required",
        }
        class properties:
            
            
            class enum_string_required(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        "UPPER": "UPPER",
                        "lower": "LOWER",
                        "": "EMPTY",
                    }
                ),
                schemas.StrSchema
            ):
                
                @classmethod
                @property
                def UPPER(cls):
                    return cls("UPPER")
                
                @classmethod
                @property
                def LOWER(cls):
                    return cls("lower")
                
                @classmethod
                @property
                def EMPTY(cls):
                    return cls("")
            
            
            class enum_string(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        "UPPER": "UPPER",
                        "lower": "LOWER",
                        "": "EMPTY",
                    }
                ),
                schemas.StrSchema
            ):
                
                @classmethod
                @property
                def UPPER(cls):
                    return cls("UPPER")
                
                @classmethod
                @property
                def LOWER(cls):
                    return cls("lower")
                
                @classmethod
                @property
                def EMPTY(cls):
                    return cls("")
            
            
            class enum_integer(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        1: "POSITIVE_1",
                        -1: "NEGATIVE_1",
                    }
                ),
                schemas.Int32Schema
            ):
                
                @classmethod
                @property
                def POSITIVE_1(cls):
                    return cls(1)
                
                @classmethod
                @property
                def NEGATIVE_1(cls):
                    return cls(-1)
            
            
            class enum_number(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        1.1: "POSITIVE_1_PT_1",
                        -1.2: "NEGATIVE_1_PT_2",
                    }
                ),
                schemas.Float64Schema
            ):
                
                @classmethod
                @property
                def POSITIVE_1_PT_1(cls):
                    return cls(1.1)
                
                @classmethod
                @property
                def NEGATIVE_1_PT_2(cls):
                    return cls(-1.2)
        
            @classmethod
            @property
            def stringEnum(cls) -> typing.Type['StringEnum']:
                return StringEnum
        
            @classmethod
            @property
            def IntegerEnum(cls) -> typing.Type['IntegerEnum']:
                return IntegerEnum
        
            @classmethod
            @property
            def StringEnumWithDefaultValue(cls) -> typing.Type['StringEnumWithDefaultValue']:
                return StringEnumWithDefaultValue
        
            @classmethod
            @property
            def IntegerEnumWithDefaultValue(cls) -> typing.Type['IntegerEnumWithDefaultValue']:
                return IntegerEnumWithDefaultValue
        
            @classmethod
            @property
            def IntegerEnumOneValue(cls) -> typing.Type['IntegerEnumOneValue']:
                return IntegerEnumOneValue
            __annotations__ = {
                "enum_string_required": enum_string_required,
                "enum_string": enum_string,
                "enum_integer": enum_integer,
                "enum_number": enum_number,
                "stringEnum": stringEnum,
                "IntegerEnum": IntegerEnum,
                "StringEnumWithDefaultValue": StringEnumWithDefaultValue,
                "IntegerEnumWithDefaultValue": IntegerEnumWithDefaultValue,
                "IntegerEnumOneValue": IntegerEnumOneValue,
            }
        additional_properties = schemas.AnyTypeSchema
    
    enum_string_required: MetaOapg.properties.enum_string_required
    enum_string: typing.Union[MetaOapg.properties.enum_string, schemas.Unset]
    enum_integer: typing.Union[MetaOapg.properties.enum_integer, schemas.Unset]
    enum_number: typing.Union[MetaOapg.properties.enum_number, schemas.Unset]
    stringEnum: typing.Union['StringEnum', schemas.Unset]
    IntegerEnum: typing.Union['IntegerEnum', schemas.Unset]
    StringEnumWithDefaultValue: typing.Union['StringEnumWithDefaultValue', schemas.Unset]
    IntegerEnumWithDefaultValue: typing.Union['IntegerEnumWithDefaultValue', schemas.Unset]
    IntegerEnumOneValue: typing.Union['IntegerEnumOneValue', schemas.Unset]
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["enum_string_required"]) -> MetaOapg.properties.enum_string_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["enum_string"]) -> typing.Union[MetaOapg.properties.enum_string, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["enum_integer"]) -> typing.Union[MetaOapg.properties.enum_integer, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["enum_number"]) -> typing.Union[MetaOapg.properties.enum_number, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["stringEnum"]) -> typing.Union['StringEnum', schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["IntegerEnum"]) -> typing.Union['IntegerEnum', schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["StringEnumWithDefaultValue"]) -> typing.Union['StringEnumWithDefaultValue', schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["IntegerEnumWithDefaultValue"]) -> typing.Union['IntegerEnumWithDefaultValue', schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["IntegerEnumOneValue"]) -> typing.Union['IntegerEnumOneValue', schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def __getitem__(self, name: typing.Union[str, typing.Literal["enum_string_required"], typing.Literal["enum_string"], typing.Literal["enum_integer"], typing.Literal["enum_number"], typing.Literal["stringEnum"], typing.Literal["IntegerEnum"], typing.Literal["StringEnumWithDefaultValue"], typing.Literal["IntegerEnumWithDefaultValue"], typing.Literal["IntegerEnumOneValue"], ]):
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
        enum_string_required: typing.Union[MetaOapg.properties.enum_string_required, str, ],
        enum_string: typing.Union[MetaOapg.properties.enum_string, str, schemas.Unset] = schemas.unset,
        enum_integer: typing.Union[MetaOapg.properties.enum_integer, int, schemas.Unset] = schemas.unset,
        enum_number: typing.Union[MetaOapg.properties.enum_number, float, schemas.Unset] = schemas.unset,
        stringEnum: typing.Union['StringEnum', schemas.Unset] = schemas.unset,
        IntegerEnum: typing.Union['IntegerEnum', schemas.Unset] = schemas.unset,
        StringEnumWithDefaultValue: typing.Union['StringEnumWithDefaultValue', schemas.Unset] = schemas.unset,
        IntegerEnumWithDefaultValue: typing.Union['IntegerEnumWithDefaultValue', schemas.Unset] = schemas.unset,
        IntegerEnumOneValue: typing.Union['IntegerEnumOneValue', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'EnumTest':
        return super().__new__(
            cls,
            *args,
            enum_string_required=enum_string_required,
            enum_string=enum_string,
            enum_integer=enum_integer,
            enum_number=enum_number,
            stringEnum=stringEnum,
            IntegerEnum=IntegerEnum,
            StringEnumWithDefaultValue=StringEnumWithDefaultValue,
            IntegerEnumWithDefaultValue=IntegerEnumWithDefaultValue,
            IntegerEnumOneValue=IntegerEnumOneValue,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.integer_enum import IntegerEnum
from petstore_api.model.integer_enum_one_value import IntegerEnumOneValue
from petstore_api.model.integer_enum_with_default_value import IntegerEnumWithDefaultValue
from petstore_api.model.string_enum import StringEnum
from petstore_api.model.string_enum_with_default_value import StringEnumWithDefaultValue
