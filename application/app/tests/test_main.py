from fastapi.testclient import TestClient
from main import app

from datetime import date, timedelta


client = TestClient(app)

test_username = 'someoneusername'
prefix = "/hello"
date_year_ago = date(date.today().year - 1, date.today().month, date.today().day)
date_after_past_birthday = (date_year_ago + timedelta(days=1)).strftime('%Y-%m-%d')


def test_read_nonexisting_user():
    response = client.get(f"{prefix}/{test_username}")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_post_user_with_not_only_letters():
    response = client.put(
        f"{prefix}/someoneus1ername",
        headers={"Content-Type": "application/json"},
        json={"dateOfBirth": f"{date(date.today().year -1 , date.today().month, date.today().day)}"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "name must contain only letters"}


def test_post_user_with_not_past_date():
    response = client.put(
        f"{prefix}/{test_username}",
        headers={"Content-Type": "application/json"},
        json={"dateOfBirth": f"{date.today()}"}
    )

    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == "Date should be in the past"


def test_add_user():
    response = client.put(
        f"{prefix}/{test_username}",
        headers={"Content-Type": "application/json"},
        json={"dateOfBirth": f"{date_year_ago}"}
    )

    assert response.status_code == 204


def test_birthday():
    response = client.get(f"{prefix}/{test_username}")

    assert response.status_code == 200
    assert response.json() == {"message": f"Hello, {test_username}! Happy birthday!"}


def test_update_birthday():
    response = client.put(
        f"{prefix}/{test_username}",
        headers={"Content-Type": "application/json"},
        json={"dateOfBirth": f"{date_after_past_birthday}"}
    )

    assert response.status_code == 204


def test_updated_birthday():
    response = client.get(f"{prefix}/{test_username}")

    assert response.status_code == 200
    assert response.json() == {"message": f"Hello, {test_username}! Your birthday is in 1 day(s)"}


def test_delete_user_after_testing():
    response = client.delete(f"{prefix}/{test_username}")

    assert response.status_code == 200
