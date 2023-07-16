import datetime
from _typeshed import NoneType
from typing import (
    Any,
    Awaitable,
    Collection,
    Iterable,
    Mapping,
    MutableMapping,
    Protocol,
    Sequence,
    TypeVar,
    Type,
    Optional,
    List,
    Coroutine,
    Callable,
    Dict,
    NoReturn,
    Tuple,
    Union,
)
import pymongo
from pymongo import CursorType
from pymongo import IndexModel
import pymongo.common
import pymongo.database
import pymongo.errors
import pymongo.mongo_client
from bson import CodecOptions
from pymongo import WriteConcern, ReadPreference
from pymongo.change_stream import ChangeStream
from pymongo.client_session import ClientSession, TransactionOptions
from pymongo.database import Database
from pymongo.encryption import ClientEncryption
from pymongo.read_concern import ReadConcern
from pymongo.collection import _IndexKeyHint, _IndexList, _Pipeline, _WriteOp
from pymongo.collation import Collation
from pymongo.results import (
    InsertManyResult,
    InsertOneResult,
    UpdateResult,
    BulkWriteResult,
    DeleteResult,
)
from bson.raw_bson import RawBSONDocument
from motor.docstrings import find_one_doc
from .metaprogramming import (
    AsyncCommand,
    AsyncRead,
    AsyncWrite,
    DelegateMethod,
    ReadOnlyProperty,
    Async,
)

T = TypeVar("T")

_HAS_SSL: bool
_WITH_TRANSACTION_RETRY_TIME_LIMIT: int

def _within_time_limit(start_time: float) -> bool: ...
def _max_time_expired_error(exc: Exception) -> bool: ...

class AgnosticBase(object):
    delegate: Any

    def __eq__(self, other: Any) -> bool: ...
    def __init__(self, delegate: Any) -> None: ...
    def __repr__(self) -> str: ...

class AgnosticBaseProperties(AgnosticBase):
    codec_options: ReadOnlyProperty
    read_preference: ReadOnlyProperty
    read_concern: ReadOnlyProperty
    write_concern: ReadOnlyProperty

class AgnosticClient(AgnosticBaseProperties):
    __motor_class_name__: str
    __delegate_class__: Type[pymongo.mongo_client.MongoClient]

    address: ReadOnlyProperty
    arbiters: ReadOnlyProperty
    close: DelegateMethod
    __hash__: DelegateMethod
    drop_database: AsyncCommand
    options: ReadOnlyProperty
    get_database: DelegateMethod
    get_default_database: DelegateMethod
    HOST: ReadOnlyProperty
    is_mongos: ReadOnlyProperty
    is_primary: ReadOnlyProperty
    list_databases: AsyncRead
    list_database_names: AsyncRead
    nodes: ReadOnlyProperty
    PORT: ReadOnlyProperty
    primary: ReadOnlyProperty
    read_concern: ReadOnlyProperty
    secondaries: ReadOnlyProperty
    server_info: AsyncRead
    topology_description: ReadOnlyProperty
    def start_session(
        self,
        causal_consistency: Optional[bool] = None,
        default_transaction_options: Optional[TransactionOptions] = None,
        snapshot: Optional[bool] = False,
    ) -> Coroutine[Any, Any, ClientSession]: ...

    _io_loop: Optional[Any]
    _framework: Any

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def io_loop(self) -> Any: ...
    def get_io_loop(self) -> Any: ...
    def watch(
        self,
        pipeline: Optional[List[Any]] = None,
        full_document: Optional[str] = None,
        resume_after: Optional[Any] = None,
        max_await_time_ms: Optional[int] = None,
        batch_size: Optional[int] = None,
        collation: Optional[Any] = None,
        start_at_operation_time: Optional[Any] = None,
        session: Optional[ClientSession] = None,
        start_after: Optional[Any] = None,
        comment: Optional[str] = None,
        full_document_before_change: Optional[str] = None,
        show_expanded_events: Optional[bool] = None,
    ) -> Any: ...
    def __getattr__(self, name: str) -> Any: ...
    def __getitem__(self, name: str) -> Any: ...
    def wrap(self, obj: Any) -> Any: ...

class _MotorTransactionContext:
    _session: AgnosticClientSession

    def __init__(self, session: AgnosticClientSession): ...
    async def __aenter__(self) -> _MotorTransactionContext: ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

class AgnosticClientSession(AgnosticBase):
    __motor_class_name__: str
    __delegate_class__: ClientSession

    async def commit_transaction(self) -> None: ...
    abort_transaction: AsyncCommand
    end_session: AsyncCommand
    cluster_time: ReadOnlyProperty
    has_ended: ReadOnlyProperty
    in_transaction: ReadOnlyProperty
    options: ReadOnlyProperty
    operation_time: ReadOnlyProperty
    session_id: ReadOnlyProperty
    advance_cluster_time: DelegateMethod
    advance_operation_time: DelegateMethod

    def __init__(self, delegate: ClientSession, motor_client: AgnosticClient): ...
    def get_io_loop(self) -> Any: ...
    async def with_transaction(
        self,
        coro: Coroutine,
        read_concern: ReadConcern = None,
        write_concern: WriteConcern = None,
        read_preference: ReadPreference = None,
        max_commit_time_ms: int = None,
    ) -> Any: ...
    def start_transaction(
        self,
        read_concern: ReadConcern = None,
        write_concern: WriteConcern = None,
        read_preference: ReadPreference = None,
        max_commit_time_ms: int = None,
    ) -> _MotorTransactionContext: ...
    @property
    def client(self) -> AgnosticClient: ...
    async def __aenter__(self) -> AgnosticClientSession: ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

class AgnosticDatabase(AgnosticBaseProperties):
    __motor_class_name__: str
    __delegate_class__: Database

    __hash__: DelegateMethod
    __bool__: DelegateMethod
    command: AsyncCommand
    create_collection: AsyncCommand
    dereference: AsyncRead
    drop_collection: AsyncCommand
    get_collection: DelegateMethod
    list_collection_names: AsyncRead
    list_collections: AsyncRead
    name: ReadOnlyProperty
    validate_collection: AsyncRead
    with_options: DelegateMethod

    _async_aggregate: AsyncRead

    def __init__(self, client: Any, name: str, **kwargs: Any) -> None: ...
    def aggregate(
        self, pipeline: Any, *args: Any, **kwargs: Any
    ) -> AgnosticLatentCommandCursor: ...
    def watch(
        self,
        pipeline: Any = None,
        full_document: Any = None,
        resume_after: Any = None,
        max_await_time_ms: Any = None,
        batch_size: Any = None,
        collation: Any = None,
        start_at_operation_time: Any = None,
        session: Any = None,
        start_after: Any = None,
        comment: Any = None,
        full_document_before_change: Any = None,
        show_expanded_events: Any = None,
    ) -> AgnosticChangeStream: ...
    @property
    def client(self) -> Any: ...
    def __getattr__(self, name: str) -> Any: ...
    def __getitem__(self, name: str) -> AgnosticCollection: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
    def wrap(self, obj: Any) -> Any: ...
    def get_io_loop(self) -> Any: ...

class AgnosticCollection(AgnosticBaseProperties):
    __motor_class_name__: str
    __delegate_class__: Any

    async def bulk_write(
        self,
        requests: Sequence[_WriteOp],
        ordered: bool = True,
        bypass_document_validation: bool = False,
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
        let: Optional[Mapping] = None,
    ) -> BulkWriteResult: ...
    async def count_documents(
        self,
        filter: Mapping[str, Any],
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> int: ...
    async def create_index(
        self,
        keys: _IndexKeyHint,
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> str: ...
    async def create_indexes(
        self,
        indexes: Sequence[IndexModel],
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> List[str]: ...
    async def delete_many(
        self,
        filter: Mapping[str, Any],
        collation: Optional[Union[Mapping[str, Any], "Collation"]] = None,
        hint: Optional[_IndexKeyHint] = None,
        session: Optional[ClientSession] = None,
        let: Optional[Mapping[str, Any]] = None,
        comment: Optional[Any] = None,
    ) -> DeleteResult: ...
    async def delete_one(
        self,
        filter: Mapping[str, Any],
        collation: Optional[Union[Mapping[str, Any], "Collation"]] = None,
        hint: Optional[_IndexKeyHint] = None,
        session: Optional[ClientSession] = None,
        let: Optional[Mapping[str, Any]] = None,
        comment: Optional[Any] = None,
    ) -> DeleteResult: ...
    async def distinct(
        self,
        key: str,
        filter: Optional[Mapping[str, Any]] = None,
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> List[Any]: ...
    async def drop(
        self,
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
        encrypted_fields: Optional[Mapping[str, Any]] = None,
    ) -> None: ...
    async def drop_index(
        self,
        index_or_name: _IndexKeyHint,
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> None: ...
    async def drop_indexes(
        self,
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> None: ...
    async def estimated_document_count(
        self, comment: Optional[Any] = None, **kwargs: Any
    ) -> int: ...
    async def find_one(
        self,
        filter: Optional[Any] = None,
        projection: Optional[Any] = None,
        skip: int = 0,
        no_cursor_timeout: bool = False,
        cursor_type: int = CursorType.NON_TAILABLE,
        sort: Optional[Any] = None,
        allow_partial_results: bool = False,
        oplog_replay: bool = False,
        batch_size: int = 0,
        collation: Optional[Any] = None,
        hint: Optional[Any] = None,
        max_scan: Optional[int] = None,
        max_time_ms: Optional[int] = None,
        max: Optional[Any] = None,
        min: Optional[Any] = None,
        return_key: bool = False,
        show_record_id: bool = False,
        snapshot: bool = False,
        comment: Optional[str] = None,
        session: Optional[Any] = None,
        allow_disk_use: Optional[bool] = None,
    ) -> Mapping[str, Any]: ...
    async def find_one_and_delete(
        self,
        filter: Mapping[str, Any],
        projection: Optional[Union[Mapping[str, Any], Iterable[str]]] = None,
        sort: Optional[_IndexList] = None,
        hint: Optional[_IndexKeyHint] = None,
        session: Optional[ClientSession] = None,
        let: Optional[Mapping[str, Any]] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> Mapping[str, Any]: ...
    async def find_one_and_replace(
        self,
        filter: Mapping[str, Any],
        replacement: Mapping[str, Any],
        projection: Optional[Union[Mapping[str, Any], Iterable[str]]] = None,
        sort: Optional[_IndexList] = None,
        upsert: bool = False,
        return_document: bool = False,
        hint: Optional[_IndexKeyHint] = None,
        session: Optional[ClientSession] = None,
        let: Optional[Mapping[str, Any]] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> Mapping[str, Any]: ...
    async def find_one_and_update(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], _Pipeline],
        projection: Optional[Union[Mapping[str, Any], Iterable[str]]] = None,
        sort: Optional[_IndexList] = None,
        upsert: bool = False,
        return_document: bool = False,
        array_filters: Optional[Sequence[Mapping[str, Any]]] = None,
        hint: Optional[_IndexKeyHint] = None,
        session: Optional[ClientSession] = None,
        let: Optional[Mapping[str, Any]] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> Mapping[str, Any]: ...
    async def index_information(
        self, session: Optional[ClientSession] = None, comment: Optional[Any] = None
    ) -> MutableMapping[str, Any]: ...
    async def insert_many(
        self,
        documents: Sequence[Union[Mapping[str, Any], RawBSONDocument]],
        ordered: bool = True,
        bypass_document_validation: bool = False,
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
    ) -> InsertManyResult: ...
    async def insert_one(
        self,
        document: Union[Mapping[str, Any], RawBSONDocument],
        bypass_document_validation: bool = False,
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
    ) -> InsertOneResult: ...
    async def options(
        self, session: Optional[ClientSession] = None, comment: Optional[Any] = None
    ) -> MutableMapping[str, Any]: ...
    async def rename(
        self,
        new_name: str,
        session: Optional[ClientSession] = None,
        comment: Optional[Any] = None,
        **kwargs: Any,
    ) -> MutableMapping[str, Any]: ...
    async def replace_one(
        self,
        filter: Mapping[str, Any],
        replacement: Mapping[str, Any],
        upsert: bool = False,
        bypass_document_validation: bool = False,
        collation: Optional[Collation] = None,
        hint: Optional[_IndexKeyHint] = None,
        session: Optional[ClientSession] = None,
        let: Optional[Mapping[str, Any]] = None,
        comment: Optional[Any] = None,
    ) -> UpdateResult: ...
    async def update_many(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], _Pipeline],
        upsert: bool = False,
        array_filters: Optional[Sequence[Mapping[str, Any]]] = None,
        bypass_document_validation: Optional[bool] = None,
        collation: Optional[Collation] = None,
        hint: Optional[_IndexKeyHint] = None,
        session: Optional[ClientSession] = None,
        let: Optional[Mapping[str, Any]] = None,
        comment: Optional[Any] = None,
    ) -> UpdateResult: ...
    async def update_one(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], _Pipeline],
        upsert: bool = False,
        bypass_document_validation: bool = False,
        collation: Optional[Collation] = None,
        array_filters: Optional[Sequence[Mapping[str, Any]]] = None,
        hint: Optional[_IndexKeyHint] = None,
        session: Optional[ClientSession] = None,
        let: Optional[Mapping[str, Any]] = None,
        comment: Optional[Any] = None,
    ) -> UpdateResult: ...
    async def with_options(
        self,
        codec_options: Optional[CodecOptions] = None,
        read_preference: Optional[ReadPreference] = None,
        write_concern: Optional[WriteConcern] = None,
        read_concern: Optional[ReadConcern] = None,
    ) -> Collection[Mapping[str, Any]]: ...
    def __init__(
        self,
        database: Any,
        name: str,
        codec_options: Any = None,
        read_preference: Any = None,
        write_concern: Any = None,
        read_concern: Any = None,
        _delegate: Any = None,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __getitem__(self, name: str) -> Any: ...
    def __call__(self, *args, **kwargs) -> Any: ...
    def find(
        self,
        filter: Optional[Any] = None,
        projection: Optional[Any] = None,
        skip: int = 0,
        no_cursor_timeout: bool = False,
        cursor_type: int = CursorType.NON_TAILABLE,
        sort: Optional[Any] = None,
        allow_partial_results: bool = False,
        oplog_replay: bool = False,
        batch_size: int = 0,
        collation: Optional[Any] = None,
        hint: Optional[Any] = None,
        max_scan: Optional[int] = None,
        max_time_ms: Optional[int] = None,
        max: Optional[Any] = None,
        min: Optional[Any] = None,
        return_key: bool = False,
        show_record_id: bool = False,
        snapshot: bool = False,
        comment: Optional[str] = None,
        session: Optional[Any] = None,
        allow_disk_use: Optional[bool] = None,
    ) -> Type[AgnosticCursor]: ...
    def find_raw_batches(self, *args, **kwargs) -> Any: ...
    def aggregate(self, pipeline: Any, *args, **kwargs) -> Any: ...
    def aggregate_raw_batches(self, pipeline: Any, **kwargs: Any) -> Any: ...
    def watch(
        self,
        pipeline: Any = None,
        full_document: Any = None,
        resume_after: Any = None,
        max_await_time_ms: Any = None,
        batch_size: Any = None,
        collation: Any = None,
        start_at_operation_time: Any = None,
        session: Any = None,
        start_after: Any = None,
        comment: Any = None,
        full_document_before_change: Any = None,
        show_expanded_events: Any = None,
    ) -> Any: ...
    def list_indexes(self, session: Any = None, **kwargs: Any) -> Any: ...
    def wrap(self, obj: Any) -> Any: ...
    def get_io_loop(self) -> Any: ...

class AgnosticBaseCursor(AgnosticBase):
    _async_close: Any
    _refresh: Any
    address: Any
    cursor_id: Any
    alive: Any
    session: Any

    def __init__(self, cursor: Any, collection: Any) -> None: ...
    def __aiter__(self) -> Any: ...
    async def next(self) -> Any: ...
    __anext__ = next
    async def __aenter__(self) -> Any: ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any: ...
    def _get_more(self) -> Any: ...
    @property
    def fetch_next(self) -> Any: ...
    def next_object(self) -> Any: ...
    def each(self, callback: Callable) -> None: ...
    def _each_got_more(self, callback: Callable, future: Any) -> None: ...
    def to_list(self, length: int) -> Any: ...
    def _to_list(
        self, length: int, the_list: List, future: Any, get_more_result: Any
    ) -> None: ...
    def get_io_loop(self) -> Any: ...
    async def close(self) -> None: ...
    def batch_size(self, batch_size: int) -> "AgnosticBaseCursor": ...
    def _buffer_size(self) -> int: ...
    def _query_flags(self) -> None: ...
    def _data(self) -> None: ...
    def _killed(self) -> None: ...

class AgnosticCursor(AgnosticBaseCursor):
    __motor_class_name__: str
    __delegate_class__: Any  # replace with actual class
    address: Any
    collation: Any
    distinct: AsyncRead
    explain: AsyncRead
    add_option: Any
    remove_option: Any
    limit: Any
    skip: Any
    max_scan: Any
    sort: Any
    hint: Any
    where: Any
    max_await_time_ms: Any
    max_time_ms: Any
    min: Any
    max: Any
    comment: Any
    allow_disk_use: Any

    def rewind(self) -> "AgnosticCursor": ...
    def clone(self) -> "AgnosticCursor": ...
    def __copy__(self) -> "AgnosticCursor": ...
    def __deepcopy__(self, memo: Any) -> "AgnosticCursor": ...
    def _query_flags(self) -> int: ...
    def _data(self) -> Any: ...
    def _killed(self) -> Any: ...

class AgnosticRawBatchCursor(AgnosticCursor):
    __motor_class_name__: str
    __delegate_class__: Any  # replace with actual class

class AgnosticCommandCursor(AgnosticBaseCursor):
    __motor_class_name__: str
    __delegate_class__: Any  # replace with actual class

    def _query_flags(self) -> int: ...
    def _data(self) -> Any: ...
    def _killed(self) -> Any: ...

class AgnosticRawBatchCommandCursor(AgnosticCommandCursor):
    __motor_class_name__: str
    __delegate_class__: Any

class _LatentCursor:
    alive: bool
    _CommandCursor__data: List
    _CommandCursor__id: NoneType
    _CommandCursor__killed: bool
    _CommandCursor__sock_mgr: NoneType
    _CommandCursor__session: NoneType
    _CommandCursor__explicit_session: NoneType
    cursor_id: NoneType

    def __init__(self, collection: Any): ...
    def _CommandCursor__end_session(self, *args: Any, **kwargs: Any): ...
    def _CommandCursor__die(self, *args: Any, **kwargs: Any): ...
    def clone(self) -> "_LatentCursor": ...
    def rewind(self): ...

class AgnosticLatentCommandCursor(AgnosticCommandCursor):
    __motor_class_name__: str

    def __init__(self, collection: Any, start: Any, *args: Any, **kwargs: Any): ...
    def batch_size(self, batch_size: int) -> "AgnosticLatentCommandCursor": ...
    def _get_more(self): ...
    def _on_started(self, original_future: Any, future: Any): ...

class AgnosticChangeStream(AgnosticBase):
    __delegate_class__: Type[ChangeStream]
    __motor_class_name__: str

    _close: AsyncCommand
    resume_token: ReadOnlyProperty()

    def __init__(
        self,
        target: Any,
        pipeline: List[Dict[str, Any]],
        full_document: str,
        resume_after: Optional[Dict[str, Any]],
        max_await_time_ms: Optional[int],
        batch_size: Optional[int],
        collation: Optional[Dict[str, Any]],
        start_at_operation_time: Optional[datetime.datetime],
        session: Any,
        start_after: Optional[Dict[str, Any]],
        comment: Optional[str],
        full_document_before_change: Optional[bool],
        show_expanded_events: Optional[bool],
    ): ...
    def _lazy_init(self): ...
    def _try_next(self): ...
    @property
    def alive(self) -> bool: ...
    async def next(self): ...
    async def try_next(self): ...
    async def close(self): ...
    def __aiter__(self) -> "AgnosticChangeStream": ...
    __anext__ = next
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...
    def get_io_loop(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...

class AgnosticClientEncryption(AgnosticBase):
    __motor_class_name__: str
    __delegate_class__: Type[ClientEncryption]
    create_data_key: AsyncCommand
    encrypt: AsyncCommand
    decrypt: AsyncCommand
    close: AsyncCommand
    rewrap_many_data_key: AsyncCommand
    delete_key: AsyncCommand
    get_key: AsyncCommand
    add_key_alt_name: AsyncCommand
    get_key_by_alt_name: AsyncCommand
    remove_key_alt_name: AsyncCommand
    encrypt_expression: Optional[AsyncCommand]

    def __init__(
        self,
        kms_providers: List[Dict[str, Any]],
        key_vault_namespace: str,
        key_vault_client: Any,
        codec_options: CodecOptions,
        io_loop: Optional[Any] = None,
        kms_tls_options: Optional[Dict[str, Any]] = None,
    ): ...
    @property
    def io_loop(self) -> Any: ...
    def get_io_loop(self) -> Any: ...
    async def __aenter__(self) -> "AgnosticClientEncryption": ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def __enter__(self) -> NoReturn: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    async def get_keys(self) -> AgnosticCursor: ...
    async def create_encrypted_collection(
        self,
        database: AgnosticDatabase,
        name: str,
        encrypted_fields: Dict[str, Any],
        kms_provider: Optional[Any] = None,
        master_key: Optional[Any] = None,
        **kwargs: Any,
    ) -> Tuple[AgnosticCollection, Any]: ...
