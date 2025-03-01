from __future__ import annotations

import inspect
import sys
from datetime import datetime, timezone
from typing import Any, Awaitable, TypeVar, cast, overload

import pytest

T = TypeVar("T")


@overload
async def maybe_async(obj: Awaitable[T]) -> T:
    ...


@overload
async def maybe_async(obj: T) -> T:
    ...


async def maybe_async(obj: Awaitable[T] | T) -> T:
    if inspect.isawaitable(obj):
        return cast(T, await obj)
    return cast(T, obj)


def update_raw_records(raw_authors: list[dict[str, Any]], raw_rules: list[dict[str, Any]]) -> None:
    for raw_author in raw_authors:
        raw_author["dob"] = datetime.strptime(raw_author["dob"], "%Y-%m-%d").date()
        raw_author["created_at"] = datetime.strptime(raw_author["created_at"], "%Y-%m-%dT%H:%M:%S").astimezone(
            timezone.utc
        )
        raw_author["updated_at"] = datetime.strptime(raw_author["updated_at"], "%Y-%m-%dT%H:%M:%S").astimezone(
            timezone.utc
        )
    for raw_rule in raw_rules:
        raw_rule["created_at"] = datetime.strptime(raw_rule["created_at"], "%Y-%m-%dT%H:%M:%S").astimezone(timezone.utc)
        raw_rule["updated_at"] = datetime.strptime(raw_rule["updated_at"], "%Y-%m-%dT%H:%M:%S").astimezone(timezone.utc)


mark_requires_docker = [
    pytest.mark.sqlalchemy_integration,
    pytest.mark.skipif(sys.platform != "linux", reason="docker not available on this platform"),
]
