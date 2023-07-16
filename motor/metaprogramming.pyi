from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    Optional,
    Tuple,
    Type,
    Union,
)

from gridfs.grid_file import (
    GridIn,
    GridOut,
)
from motor.motor_asyncio import (
    AsyncIOMotorCursor,
    AsyncIOMotorGridOutCursor,
)
from pymongo.client_session import ClientSession
from pymongo.collection import Collection
from pymongo.command_cursor import CommandCursor
from pymongo.database import Database

def coroutine_annotation(f: Callable) -> Callable: ...
def unwrap_args_session(args: Tuple[Dict[str, str]]) -> Iterator[Any]: ...
def unwrap_kwargs_session(kwargs: Dict[Any, Any]) -> Dict[Any, Any]: ...

class Async:
    def __init__(self, attr_name: Optional[str], doc: Optional[str] = ...) -> None: ...
    def create_attribute(self, cls: Any, attr_name: str) -> Callable: ...
    def unwrap(self, class_name: str) -> Union[AsyncRead, AsyncCommand]: ...
    def wrap(
        self,
        original_class: Union[
            Type[CommandCursor], Type[ClientSession], Type[Collection], Type[GridOut]
        ],
    ) -> Union[AsyncRead, AsyncCommand]: ...

class AsyncCommand:
    def __init__(
        self, attr_name: Optional[str] = ..., doc: Optional[str] = ...
    ) -> None: ...

class AsyncRead:
    def __init__(
        self, attr_name: Optional[str] = ..., doc: Optional[str] = ...
    ) -> None: ...

class AsyncWrite:
    def __init__(self, attr_name: None = ..., doc: Optional[str] = ...) -> None: ...

class DelegateMethod:
    def __init__(self, doc: Optional[str] = ...) -> None: ...
    def create_attribute(
        self, cls: Any, attr_name: str
    ) -> Union[property, Callable]: ...
    def wrap(
        self, original_class: Union[Type[Collection], Type[Database], Type[GridIn]]
    ) -> DelegateMethod: ...

class MotorAttributeFactory:
    def __init__(self, doc: Optional[str] = ...) -> None: ...

class MotorCursorChainingMethod:
    def create_attribute(
        self,
        cls: Union[Type[AsyncIOMotorGridOutCursor], Type[AsyncIOMotorCursor]],
        attr_name: str,
    ) -> Callable: ...

class ReadOnlyProperty:
    def create_attribute(self, cls: Any, attr_name: str) -> property: ...
