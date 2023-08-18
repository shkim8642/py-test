def test_login_api(client, create_user):
    data = {
        "email" : "",
        "password" : "",
    }

    r = client.post("http://apdcm.remotevs.com/api/agent/login", json=data)

    r_massage = r.json()
    assert r.status_code == 200
    assert r_message.get("access_token")
    assert r_message.get("refresh_token")