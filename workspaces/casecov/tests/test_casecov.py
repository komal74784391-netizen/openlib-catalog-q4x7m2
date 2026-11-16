from src.casecov import process, healthcheck


def test_process_empty():
    assert process(None) == []


def test_healthcheck():
    assert healthcheck()["status"] == "ok"
