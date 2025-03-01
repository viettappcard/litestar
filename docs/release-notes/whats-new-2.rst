.. py:currentmodule:: litestar


What's new in 2.0?
==================

This document is an overview of the changes between version **1.51** and **2.0**.
For a detailed list of all changes, including changes between versions leading up to the
2.0 release, consult the :doc:`/release-notes/changelog`.



Starlite -> Litestar
--------------------

One of the biggest changes in version 2 is the renaming of the project from *Starlite*
to *Litestar*.

The name "Starlite" was chosen as an homage to `Starlette <https://www.starlette.io/>`_,
the ASGI framework and toolkit Starlite was initially based on. Over the course of its
development, Starlite grew more independent and relied less on Starlette, up to the
point were Starlette was officially removed as a dependency in November 2022, with the
release of `v1.39.0 <https://github.com/starlite-api/starlite/releases/tag/v1.39.0>`_.

After careful considerations, it was decided that with the release of 2.0, Starlite
would be renamed to Litestar. There were many factors contributing to this decision, but
it was mainly driven by concerns from within and outside the community about the
possible confusion of the names *Starlette* and *Starlite* which (not incidentally) bea
a lot of resemblance, which now had outlived its purpose.

****

Aside from the name, Litestar 2.0 is a direct successor of Starlite 1, and the regular
release cycle will continue. It was determined that making the first release under the
new name 2.0 and continue with the version numbers from Starlite would cause the least
friction. Following that decision, the first release under the new name was
`v2.0.0alpha3 <https://github.com/litestar-org/litestar/releases/tag/v2.0.0alpha3>`_,
following the last alpha release of Starlite 2.0,
`v2.0.0alpha2 <https://github.com/litestar-org/litestar/releases/tag/v2.0.0alpha2>`_.

.. note::
    The **1.51** release line is unaffected by this change


Imports
-------

+----------------------------------------------------+------------------------------------------------------------------------+
| ``1.51``                                           | ``2.x``                                                                |
+====================================================+========================================================================+
| ``starlite.ASGIConnection``                        | :class:`.connection.ASGIConnection`                                    |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.Partial``                               | :class:`.partial.Partial`                                              |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Enums**                                                                                                                   |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.RequestEncodingType``                   | :class:`.enums.RequestEncodingType`                                    |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ScopeType``                             | :class:`.enums.ScopeType`                                              |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.OpenAPIMediaType``                      | :class:`.enums.OpenAPIMediaType`                                       |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Datastructures**                                                                                                          |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.BackgroundTask``                        | :class:`.background_tasks.BackgroundTask`                              |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.BackgroundTasks``                       | :class:`.background_tasks.BackgroundTasks`                             |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.State``                                 | :class:`.datastructures.State`                                         |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ImmutableState``                        | :class:`.datastructures.ImmutableState`                                |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.Cookie``                                | :class:`.datastructures.Cookie`                                        |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.FormMultiDict``                         | :class:`.datastructures.FormMultiDict`                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ResponseHeader``                        | :class:`.datastructures.ResponseHeader`                                |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.UploadFile``                            | :class:`.datastructures.UploadFile`                                    |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Configuration**                                                                                                           |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AllowedHostsConfig``                    | :class:`.config.allowed_hosts.AllowedHostsConfig`                      |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractSecurityConfig``                | :class:`.security.AbstractSecurityConfig`                              |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.CacheConfig``                           | :class:`.config.response_cache.ResponseCacheConfig`                    |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.CompressionConfig``                     | :class:`.config.compression.CompressionConfig`                         |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.CORSConfig``                            | :class:`.config.cors.CORSConfig`                                       |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.CSRFConfig``                            | :class:`.config.csrf.CSRFConfig`                                       |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.OpenAPIConfig``                         | :class:`.openapi.OpenAPIConfig`                                        |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.StaticFilesConfig``                     | :class:`.static_files.config.StaticFilesConfig`                        |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.TemplateConfig``                        | :class:`.template.TemplateConfig`                                      |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.BaseLoggingConfig``                     | :class:`.logging.config.BaseLoggingConfig`                             |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.LoggingConfig``                         | :class:`.logging.config.LoggingConfig`                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.StructLoggingConfig``                   | :class:`.logging.config.StructLoggingConfig`                           |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Provide**                                                                                                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.datastructures.Provide``                | :class:`.di.Provide`                                                   |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Pagination**                                                                                                              |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractAsyncClassicPaginator``         | :class:`.pagination.AbstractAsyncClassicPaginator`                     |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractAsyncCursorPaginator``          | :class:`.pagination.AbstractAsyncCursorPaginator`                      |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractAsyncOffsetPaginator``          | :class:`.pagination.AbstractAsyncOffsetPaginator`                      |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractSyncClassicPaginator``          | :class:`.pagination.AbstractSyncClassicPaginator`                      |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractSyncCursorPaginator``           | :class:`.pagination.AbstractSyncCursorPaginator`                       |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractSyncOffsetPaginator``           | :class:`.pagination.AbstractSyncOffsetPaginator`                       |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ClassicPagination``                     | :class:`.pagination.ClassicPagination`                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.CursorPagination``                      | :class:`.pagination.CursorPagination`                                  |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.OffsetPagination``                      | :class:`.pagination.OffsetPagination`                                  |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Response containers**                                                                                                     |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.File``                                  | :class:`.response_containers.File`                                     |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.Redirect``                              | :class:`.response_containers.Redirect`                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ResponseContainer``                     | :class:`.response_containers.ResponseContainer`                        |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.Stream``                                | :class:`.response_containers.Stream`                                   |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.Template``                              | :class:`.response_containers.Template`                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Exceptions**                                                                                                              |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.HTTPException``                         | :class:`.exceptions.HTTPException`                                     |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ImproperlyConfiguredException``         | :class:`.exceptions.ImproperlyConfiguredException`                     |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.InternalServerException``               | :class:`.exceptions.InternalServerException`                           |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.MissingDependencyException``            | :class:`.exceptions.MissingDependencyException`                        |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.NoRouteMatchFoundException``            | :class:`.exceptions.NoRouteMatchFoundException`                        |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.NotAuthorizedException``                | :class:`.exceptions.NotAuthorizedException`                            |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.NotFoundException``                     | :class:`.exceptions.NotFoundException`                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.PermissionDeniedException``             | :class:`.exceptions.PermissionDeniedException`                         |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ServiceUnavailableException``           | :class:`.exceptions.ServiceUnavailableException`                       |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.StarliteException``                     | :class:`.exceptions.LitestarException`                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.TooManyRequestsException``              | :class:`.exceptions.TooManyRequestsException`                          |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ValidationException``                   | :class:`.exceptions.ValidationException`                               |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.WebSocketException``                    | :class:`.exceptions.WebSocketException`                                |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Testing**                                                                                                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.TestClient``                            | :class:`.testing.TestClient`                                           |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AsyncTestClient``                       | :class:`.testing.AsyncTestClient`                                      |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.create_test_client``                    | :class:`.testing.create_test_client`                                   |
+----------------------------------------------------+------------------------------------------------------------------------+
| **OpenAPI**                                                                                                                 |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.OpenAPIController``                     | :class:`.openapi.controller.OpenAPIController`                         |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ResponseSpec``                          | :class:`.openapi.datastructures.ResponseSpec`                          |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Middleware**                                                                                                              |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractAuthenticationMiddleware``      | :class:`.middleware.authentication.AbstractAuthenticationMiddleware`   |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AuthenticationResult``                  | :class:`.middleware.authentication.AuthenticationResult`               |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractMiddleware``                    | :class:`.middleware.AbstractMiddleware`                                |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.DefineMiddleware``                      | :class:`.middleware.DefineMiddleware`                                  |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.MiddlewareProtocol``                    | :class:`.middleware.MiddlewareProtocol`                                |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Security**                                                                                                                |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.AbstractSecurityConfig``                | :class:`.security.AbstractSecurityConfig`                              |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Route Handlers**                                                                                                          |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.handlers.asgi``                         | :mod:`.handlers`                                                       |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.handlers.http``                         | :mod:`.handlers`                                                       |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.handlers.websocket``                    | :class:`.handlers`                                                     |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ASGIRouteHandler``                      | :class:`.handlers.ASGIRouteHandler`                                    |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.BaseRouteHandler``                      | :class:`.handlers.BaseRouteHandler`                                    |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.HTTPRouteHandler``                      | :class:`.handlers.HTTPRouteHandler`                                    |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.WebsocketRouteHandler``                 | :class:`.handlers.WebsocketRouteHandler`                               |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Routes**                                                                                                                  |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.ASGIRoute``                             | :class:`.routes.ASGIRoute`                                             |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.BaseRoute``                             | :class:`.routes.BaseRoute`                                             |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.HTTPRoute``                             | :class:`.routes.HTTPRoute`                                             |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.WebSocketRoute``                        | :class:`.routes.WebSocketRoute`                                        |
+----------------------------------------------------+------------------------------------------------------------------------+
| **Parameters**                                                                                                              |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.Body``                                  | :class:`.params.Body`                                                  |
+----------------------------------------------------+------------------------------------------------------------------------+
| ``starlite.Parameter``                             | :class:`.params.Parameter`                                             |
+----------------------------------------------------+------------------------------------------------------------------------+


Response headers
----------------

Response header can now be set using either a :class:`Sequence <typing.Sequence>` of
:class:`ResponseHeader <.datastructures.response_header.ResponseHeader>`, or by using a
plain :class:`Mapping[str, str] <typing.Mapping>`. The typing of
:class:`ResponseHeader <.datastructures.response_header.ResponseHeader>` was also
changed to be more strict and now only allows string values.

.. code-block:: python
    :caption: 1.51

    from starlite import ResponseHeader, get


    @get(response_headers={"my-header": ResponseHeader(value="header-value")})
    async def handler() -> str:
        ...


.. code-block:: python
    :caption: 2.x

    from litestar import ResponseHeader, get


    @get(response_headers=[ResponseHeader(name="my-header", value="header-value")])
    async def handler() -> str:
        ...


    # or


    @get(response_headers={"my-header": "header-value"})
    async def handler() -> str:
        ...


Response cookies
----------------

Response cookies might now also be set using a
:class:`Mapping[str, str] <typing.Mapping>`, analogous to `Response headers`_.

.. code-block:: python

    @get("/", response_cookies=[Cookie(key="foo", value="bar")])
    async def handler() -> None:
        ...

is equivalent to

.. code-block:: python

    @get("/", response_cookies={"foo": "bar"})
    async def handler() -> None:
        ...


SQLAlchemy Plugin
-----------------

Support for SQLAlchemy 1 has been dropped and the new plugin will now support
SQLAlchemy 2 only.

TODO: Migration instructions

.. seealso::
    :doc:`/usage/contrib/sqlalchemy/index`
    :doc:`/reference/contrib/sqlalchemy/index`


Removal of Pydantic models
--------------------------

Several Pydantic models used for configuration have been replaced with dataclasses or
plain classes. If you relied on implicit data conversion from these models or subclassed
them, you might need to adjust your code accordingly.

.. seealso::

    :ref:`change:2.0.0alpha1-replace pydantic models with dataclasses`


Plugin protocols
----------------

The plugin protocol has been split into three distinct protocols, covering different use
cases:

:class:`litestar.plugins.InitPluginProtocol`
    Hook into an application's initialization process

:class:`litestar.plugins.SerializationPluginProtocol`
    Extend the serialization and deserialization capabilities of an application

:class:`litestar.plugins.OpenAPISchemaPluginProtocol`
    Extend OpenAPI schema generation


Plugins that made use of all features of the previous API should simply inherit from
all three base classes.


Remove 2 argument ``before_send``
---------------------------------

The 2 argument for of ``before_send`` hook handlers has been removed. Existing handlers
should be changed to include an additional ``scope`` parameter.


.. code-block:: python
    :caption: 1.51

    async def before_send(message: Message, state: State) -> None:
        ...


.. code-block:: python
    :caption: 2.x

    async def before_send(message: Message, state: State, scope: Scope) -> None:
        ...



.. seealso::
    :ref:`change:2.0.0alpha2-remove support for 2 argument form of`
    :ref:`before_send`


``initial_state`` application parameter
---------------------------------------

The ``initial_state`` argument to :class:`~litestar.app.Litestar` has been replaced
with a ``state`` keyword argument, accepting an optional
:class:`~litestar.datastructures.state.State` instance.

Existing code using this keyword argument will need to be changed from

.. code-block:: python
    :caption: 1.51

    app = Starlite(..., initial_state={"some": "key"})

to

.. code-block:: python
    :caption: 2.x

    app = Litestar(..., state=State({"some": "key"}))


Stores
------

A new module, ``litestar.stores`` has been introduced, which replaces the previously
used ``starlite.cache.Cache`` and server-side session storage backends.

These stores provide a low-level, asynchronous interface for common key/value stores
such as Redis and an in-memory implementation. They are currently used for server-side
sessions, caching and rate limiting.

Stores are integrated into the :class:`~app.Litestar` application object via the
:class:`~.stores.registry.StoreRegistry`, which can be used to register and access
stores as well as provide defaults.

.. literalinclude:: /examples/stores/get_set.py
    :language: python

.. literalinclude:: /examples/stores/namespacing.py
    :language: python
    :caption: Using namespacing

.. literalinclude:: /examples/stores/registry.py
    :language: python
    :caption: Using the registry

.. seealso::

    :doc:`/usage/stores`


Usage of the ``stores`` for caching and other integrations
-----------------------------------------------------------

The newly introduced :doc:`stores </usage/stores>` have superseded the removed
``starlite.cache`` module in various places.

The following now make use of stores:

- :class:`~litestar.middleware.rate_limit.RateLimitMiddleware`
- :class:`~litestar.config.response_cache.ResponseCacheConfig`
- :class:`~litestar.middleware.session.server_side.ServerSideSessionConfig`

The following attributes have been renamed to reduce ambiguity:

- ``Starlite.cache_config`` > ``Litestar.response_cache_config``
- ``AppConfig.cache_config`` > :attr:`~litestar.config.app.AppConfig.response_cache_config`

In addition, the ``ASGIConnection.cache`` property has been removed. It can be replaced
by accessing the store directly as described in :doc:`stores </usage/stores>`


DTOs
----

DTOs are now defined using the ``dto`` and ``return_dto`` arguments to
handlers/controllers/routers and the application.

A DTO is any type that conforms to the :class:`litestar.dto.interface.DTOInterface`
protocol.

Litestar provides a suite of factory types that implement the ``DTOInterface`` protocol
and can be used to define DTOs:

- :class:`litestar.dto.factory.stdlib.DataclassDTO`
- :class:`litestar.contrib.sqlalchemy.dto.SQLAlchemyDTO`
- :class:`litestar.contrib.pydantic.PydanticDTO`
- :class:`litestar.contrib.msgspec.MsgspecDTO`
- ``litestar.contrib.piccolo.PiccoloDTO`` (TODO)
- ``litestar.contrib.tortoise.TortoiseDTO`` (TODO)

For example, to define a DTO from a dataclass:

.. code-block:: python

    from dataclasses import dataclass

    from litestar import get
    from litestar.dto.factory import DTOConfig
    from litestar.dto.factory.stdlib import DataclassDTO


    @dataclass
    class MyType:
        some_field: str
        another_field: int


    class MyDTO(DataclassDTO[MyType]):
        config = DTOConfig(exclude={"another_field"})


    @get(dto=MyDTO)
    async def handler() -> MyType:
        return MyType(some_field="some value", another_field=42)


.. literalinclude:: /examples/data_transfer_objects/the_return_dto_parameter.py
    :language: python

.. literalinclude:: /examples/data_transfer_objects/factory/renaming_fields.py
    :language: python
    :caption: Renaming fields

.. literalinclude:: /examples/data_transfer_objects/factory/excluding_fields.py
    :language: python
    :caption: Excluding fields

.. literalinclude:: /examples/data_transfer_objects/factory/marking_fields.py
    :language: python
    :caption: Marking fields

.. seealso::
    :doc:`/usage/dto/index`


Application lifespan hooks
--------------------------

All application lifespan hooks have been merged into ``on_startup`` and ``on_shutdown``.
The following hooks have been removed:

- ``before_startup``
- ``after_startup``
- ``before_shutdown``
- ``after_shutdown``


``on_startup`` and ``on_shutdown`` now optionally receive the application instance as
their first parameter. If your ``on_startup`` and ``on_shutdown`` hooks made use of the
application state, they will now have to access it through the provided application
instance.

.. code-block:: python
    :caption: 1.51

    def on_startup(state: State) -> None:
        print(state.something)


.. code-block:: python
    :caption: 2.x

    def on_startup(app: Litestar) -> None:
        print(app.state.something)


Dependencies without ``Provide``
--------------------------------

Dependencies may now be declared without :class:`~litestar.di.Provide`, by passing the
callable directly. This can be advantageous in places where the configuration options
of :class:`~litestar.di.Provide` are not needed.

.. code-block:: python

    async def some_dependency() -> str:
        ...


    app = Litestar(dependencies={"some": Provide(some_dependency)})

is equivalent to

.. code-block:: python

    async def some_dependency() -> str:
        ...


    app = Litestar(dependencies={"some": some_dependency})


``sync_to_thread``
------------------

The ``sync_to_thread`` option can be use to run a synchronous callable provided to a
route handler or :class:`~litestar.di.Provide` inside a thread pool. Since synchronous
functions may block the main thread when not used with ``sync_to_thread=True``, a
warning will be raised in these cases. If the synchronous function should not be run in
a thread pool, passing ``sync_to_thread=False`` will also silence the warning.

.. tip::
    The warning can be disabled entirely by setting the environment variable
    ``LITESTAR_WARN_IMPLICIT_SYNC_TO_THREAD=0``


.. code-block:: python
    :caption: 1.51

    @get()
    def handler() -> None:
        ...


.. code-block:: python
    :caption: 2.x

    @get(sync_to_thread=False)
    def handler() -> None:
        ...

or

.. code-block:: python
    :caption: 2.x

    @get(sync_to_thread=True)
    def handler() -> None:
        ...


.. seealso::
    :doc:`/topics/sync-vs-async`


HTMX
----

Basic support for HTMX requests and responses was added with the
``litestar.contrib.htmx`` module.

.. seealso::

    :doc:`/usage/contrib/htmx`


Event bus
---------

A simple event bus system for Litestar, supporting synchronous and asynchronous
listeners and emitters, providing a similar interface to handlers. It currently
features a simple in-memory, process-local backend.


.. seealso::
    :doc:`/usage/events`
    :doc:`/reference/events`


SQLAlchemy Repository
---------------------

TBD



Enhanced WebSocket support
--------------------------

A new set of features for handling WebSockets, including automatic connection
handling, (de)serialization of incoming and outgoing data analogous to route
handlers, OOP based event dispatching, data iterators and more.

.. literalinclude:: /examples/websockets/listener_class_based.py
    :caption: Using a class based listener
    :language: python

.. literalinclude:: /examples/websockets/mode_send_text.py
    :caption: Echo text
    :language: python

.. literalinclude:: /examples/websockets/sending_json_dataclass.py
    :caption: Wrapping data in a dataclass
    :language: python

.. literalinclude:: /examples/websockets/with_dto.py
    :language: python

.. code-block:: python
    :caption: Receiving JSON and sending it back as MessagePack

    from litestar import websocket, WebSocket


    @websocket("/")
    async def handler(socket: WebSocket) -> None:
        await socket.accept()
        async for message in socket.iter_data(mode):
            await socket.send_msgpack(message)


.. seealso::
    :ref:`change:2.0.0alpha3-enhanced websockets support`
    :ref:`change:2.0.0alpha6-websockets: managing a socket's lifespan using a context manager in websocket listeners`
    :ref:`change:2.0.0alpha6-websockets: messagepack support`
    :ref:`change:2.0.0alpha6-websockets: data iterators`
    :doc:`/usage/websockets`


Attrs signature modelling
-------------------------

TBD


:class:`~typing.Annotated` support in route handlers
----------------------------------------------------

:class:`Annotated <typing.Annotated>` can now be used in route handler and
dependencies to specify additional information about the fields

.. code-block:: python

    @get("/")
    def index(param: int = Parameter(gt=5)) -> dict[str, int]:
        ...

.. code-block:: python

    @get("/")
    def index(param: Annotated[int, Parameter(gt=5)]) -> dict[str, int]:
        ...


Channels
---------

:doc:`/usage/channels` are a general purpose event streaming module,
which can for example be used to broadcast messages via WebSockets and includes
functionalities such as automatically generating WebSocket route handlers to
broadcast messages.

.. literalinclude:: /examples/channels/run_in_background.py
    :language: python

.. seealso::
    :doc:`channels </usage/channels>`


Application lifespan context managers
--------------------------------------

A new ``lifespan`` argument has been added to :class:`~litestar.app.Litestar`,
accepting an asynchronous context manager, wrapping the lifespan of the application.
It will be entered with the startup phase and exited on shutdown, providing
functionality equal to the ``on_startup`` and ``on_shutdown`` hooks.


.. literalinclude:: /examples/application_hooks/lifespan_manager.py
    :language: python
