import typing as t

import pytest
from starlette.testclient import TestClient


@pytest.fixture
def client() -> t.Generator[TestClient, None, None]:
    from fast_stack.app import app

    with TestClient(app) as client:
        yield client


@pytest.mark.parametrize(
    "path",
    [
        "/",
        "/auth/login/password",
        "/auth/login/github",
        "/components",
        "/components#button-and-modal",
        "/components#link-list",
        "/components#link-list",
        "/components#dynamic-modal",
        "/components#server-load-sse",
        "/components#image",
        "/components#iframe",
        "/components#video",
        "/components#toast",
        "/table/cities",
        "/table/users",
        "/table/cities",
        "/forms/login",
        "/auth/login/password",
        "/auth/login/github",
        "/robots.txt",
    ],
)
def test_gets(path: str, client: TestClient) -> None:
    response = client.get(path)
    print(response)
    print(response.content)
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "-vv"])
