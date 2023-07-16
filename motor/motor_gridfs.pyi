from typing import Any, Type, TypeVar, Optional, Union

from gridfs import GridOutCursor as _GridOutCursor, GridOut as _GridOut, GridFSBucket
from motor.core import AgnosticCollection, AgnosticCursor
from motor.metaprogramming import (
    AsyncCommand,
    AsyncRead,
    DelegateMethod,
    ReadOnlyProperty,
)
from pymongo.client_session import ClientSession

T = TypeVar("T")

def create_class_with_framework(
    cls: Type[T], framework: Any, module: str
) -> Type[T]: ...

class AgnosticGridOutCursor(AgnosticCursor):
    __motor_class_name__: str
    __delegate_class__: Type[_GridOutCursor]

    def next_object(self) -> Optional[Any]: ...

class MotorGridOutProperty(ReadOnlyProperty):
    def create_attribute(self, cls: Type[T], attr_name: str) -> property: ...

class AgnosticGridOut:
    __motor_class_name__: str
    __delegate_class__: Type[_GridOut]

    _ensure_file: AsyncCommand
    _id: MotorGridOutProperty
    aliases: MotorGridOutProperty
    chunk_size: MotorGridOutProperty
    close: DelegateMethod
    content_type: MotorGridOutProperty
    filename: MotorGridOutProperty
    length: MotorGridOutProperty
    metadata: MotorGridOutProperty
    name: MotorGridOutProperty
    read: AsyncRead
    readable: DelegateMethod
    readchunk: AsyncRead
    readline: AsyncRead
    seek: DelegateMethod
    seekable: DelegateMethod
    tell: DelegateMethod
    upload_date: MotorGridOutProperty
    write: DelegateMethod

    def __init__(
        self,
        root_collection: AgnosticCollection,
        file_id: Any = None,
        file_document: Any = None,
        delegate: Any = None,
        session: Optional[ClientSession] = None,
    ): ...
    async def __aiter__(self) -> "AgnosticGridOut": ...
    async def __anext__(self) -> Union[Any, StopAsyncIteration]: ...
    def get_io_loop(self) -> Any: ...
    async def open(self) -> "AgnosticGridOut": ...
    async def stream_to_handler(self, request_handler: Any) -> None: ...

class AgnosticGridIn:
    __motor_class_name__: str
    __delegate_class__: Type[GridFSBucket]

    close: DelegateMethod
    closed: DelegateMethod
    write: AsyncCommand

    def __init__(
        self,
        root_collection: AgnosticCollection,
        file_id: Any = None,
        filename: Optional[str] = None,
        metadata: Optional[Any] = None,
        delegate: Any = None,
        session: Optional[ClientSession] = None,
        **kwargs
    ): ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_tb): ...
    def get_io_loop(self) -> Any: ...

class AgnosticGridFSBucket:
    __motor_class_name__: str
    __delegate_class__: Type[GridFSBucket]

    open_upload_stream: DelegateMethod
    open_upload_stream_with_id: DelegateMethod
    upload_from_stream: DelegateMethod
    upload_from_stream_with_id: DelegateMethod

    def __init__(
        self,
        database: Any,
        bucket_name: str = "fs",
        chunk_size_bytes: int = 255 * 1024,
        write_concern: Optional[Any] = None,
        read_preference: Optional[Any] = None,
        collection: Optional[Any] = None,
    ): ...
    def get_io_loop(self) -> Any: ...
    def wrap(self, obj: Any): ...
    def find(self, *args: Any, **kwargs: Any): ...
