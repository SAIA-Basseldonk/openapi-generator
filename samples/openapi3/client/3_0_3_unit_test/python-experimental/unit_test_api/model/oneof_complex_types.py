# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class OneofComplexTypes(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        additional_properties = schemas.AnyTypeSchema
        
        
        class one_of_0(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "bar",
                }
                class properties:
                    bar = schemas.IntSchema
                    __annotations__ = {
                        "bar": bar,
                    }
                additional_properties = schemas.AnyTypeSchema
        
            
            bar: MetaOapg.properties.bar
            
            @typing.overload
            def __getitem__(self, name: typing.Literal["bar"]) -> MetaOapg.properties.bar: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
            
            def __getitem__(self, name: typing.Union[str, typing.Literal["bar"], ]):
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
                bar: typing.Union[MetaOapg.properties.bar, int, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *args,
                    bar=bar,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "foo",
                }
                class properties:
                    foo = schemas.StrSchema
                    __annotations__ = {
                        "foo": foo,
                    }
                additional_properties = schemas.AnyTypeSchema
        
            
            foo: MetaOapg.properties.foo
            
            @typing.overload
            def __getitem__(self, name: typing.Literal["foo"]) -> MetaOapg.properties.foo: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
            
            def __getitem__(self, name: typing.Union[str, typing.Literal["foo"], ]):
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
                foo: typing.Union[MetaOapg.properties.foo, str, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *args,
                    foo=foo,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @property
        @functools.cache
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
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
    ) -> 'OneofComplexTypes':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
