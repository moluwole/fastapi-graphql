def test_create_user(client):
    query = """
    mutation {
        createUser(userDetails: {
            name: "Test User",
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

    result = client.execute(query)
    assert result['data']['createUser']['id'] == 1
    assert result['data']['createUser']['name'] == "Test User"


def test_get_user_list(client, user):
    query = """
    query {
        listUsers {
            name
            address
        }
    }
    """

    result = client.execute(query)
    assert type(result['data']['listUsers']) == list


def test_get_single_user(client, user):
    query = """
    query {
        getSingleUser(userId: %s){
            address
        }
    }
    """ % user.id
    result = client.execute(query)

    assert result['data']['getSingleUser'] is not None
    assert result['data']['getSingleUser']['address'] == user.address
