from fastapi.testclient import TestClient

from main import app  # => FastAPI app created in our main.py file


client = TestClient(app)


def test_create_user():
    query = """
        mutation {
            addUser(userData: {
                name: "Test User",
                email: "email@test.com",
                sex: "male",
                address: "My Address",
                phoneNumber: "123456789",
            })
            {
                id
                name
                address
            }
        }
    """

    response = client.post("/graphql", json={"query": query})
    assert response is not None
    assert response.status_code == 200

    result = response.json()
    assert result["data"]["addUser"]["name"] == "Test User"
    assert result["data"]["addUser"]["address"] == "My Address"

def test_get_user_list(user):
    query = """
      query {
          users {
              name
              address
          }
      }
    """

    response = client.post("/graphql", json={"query": query})
    assert response is not None
    assert response.status_code == 200

    result = response.json()
    assert type(result['data']['users']) == list
    assert result["data"]["users"][0]["name"] == user.name



def test_get_single_user(user):
    query = """
      query {
          getSingleUser(userId: %s) {
              name
              address
          }
      }
    """ % user.id

    response = client.post("/graphql", json={"query": query})
    assert response is not None
    assert response.status_code == 200

    result = response.json()
    assert type(result['data']['getSingleUser']) == dict
    assert result["data"]["getSingleUser"]["name"] == user.name
