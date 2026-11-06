import pytest

from processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T10:30:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-03-10T09:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-20T15:45:00"},
    ]


def test_filter_by_state(sample_transactions):
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


def test_filter_by_state_default(sample_transactions):
    result = filter_by_state(sample_transactions)
    assert len(result) == 2


def test_filter_by_state_empty(sample_transactions):
    result = filter_by_state(sample_transactions, "PENDING")
    assert result == []


def test_sort_by_date_descending(sample_transactions):
    result = sort_by_date(sample_transactions)
    dates = [t["date"] for t in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(sample_transactions):
    result = sort_by_date(sample_transactions, reverse=False)
    dates = [t["date"] for t in result]
    assert dates == sorted(dates)
