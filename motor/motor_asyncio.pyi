from typing import TypeVar, Type

from .core import (
    AgnosticClient,
    AgnosticClientSession,
    AgnosticDatabase,
    AgnosticCollection,
    AgnosticCursor,
    AgnosticCommandCursor,
    AgnosticLatentCommandCursor,
    AgnosticChangeStream,
    AgnosticClientEncryption,
)
from .motor_gridfs import (
    AgnosticGridFSBucket,
    AgnosticGridIn,
    AgnosticGridOut,
    AgnosticGridOutCursor,
)

T = TypeVar("T")

def create_asyncio_class(cls: Type[T]) -> Type[T]: ...

AsyncIOMotorClient: Type[AgnosticClient]
AsyncIOMotorClientSession: Type[AgnosticClientSession]
AsyncIOMotorDatabase: Type[AgnosticDatabase]
AsyncIOMotorCollection: Type[AgnosticCollection]
AsyncIOMotorCursor: Type[AgnosticCursor]
AsyncIOMotorCommandCursor: Type[AgnosticCommandCursor]
AsyncIOMotorLatentCommandCursor: Type[AgnosticLatentCommandCursor]
AsyncIOMotorChangeStream: Type[AgnosticChangeStream]
AsyncIOMotorGridFSBucket: Type[AgnosticGridFSBucket]
AsyncIOMotorGridIn: Type[AgnosticGridIn]
AsyncIOMotorGridOut: Type[AgnosticGridOut]
AsyncIOMotorGridOutCursor: Type[AgnosticGridOutCursor]
AsyncIOMotorClientEncryption: Type[AgnosticClientEncryption]
