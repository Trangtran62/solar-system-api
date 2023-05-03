def test_get_planets_with_no_records(client):
    response = client.get("/planet")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_planets_with_records(client, add_two_planets):
    response = client.get("/planet")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
        "id": 1,
        "name": "Saturn",
        "description": "Rings",
        "order_from_sun": "6th from sun"
        },
        {
        "id": 2,
        "name": "Mars",
        "description": "Hot red",
        "order_from_sun": "4th from sun"
        }
    ]

def test_get_one_planet(client, add_two_planets):
    response = client.get("/planet/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Saturn",
        "description": "Rings",
        "order_from_sun": "6th from sun"
        }

def test_get_one_planet_return_404(client, add_two_planets):
    response = client.get("planet/3")

    assert response.status_code == 404

def test_post_one_planet(client):
    response = client.post("/planet", json={
        "name": "Neptune",
        "description": "Icy",
        "order_from_sun": "Farthest from sun"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {"message": "Planet 1 successfuly created"}

def test_put_one_planet(client, add_two_planets):
    response = client.put("/planet/2", json={
        "name": "Mars",
        "description": "Elon's private residence",
        "order_from_sun": "4th from sun"
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"message": "planet 2 updated"}

def test_delete_one_planet(client, add_two_planets):
    response = client.delete("/planet/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"message": "planet 1 deleted"}
