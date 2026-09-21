from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_register_and_unregister_participant():
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200

    response = client.delete(f"/activities/{activity_name}/participants?email={email}")
    assert response.status_code == 200

    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]
