import graphene
import pytest
from graphene.test import Client
from orator import DatabaseManager, Model, Schema
from orator.migrations import DatabaseMigrationRepository, Migrator

from models.comment import Comments
from models.post import Post
from models.user import User
from schema import Query, Mutation


@pytest.fixture(autouse=True)
def setup_database():
    DATABASES = {
        "sqlite": {
            "driver": "sqlite",
            "database": "test.db"
        }
    }

    db = DatabaseManager(DATABASES)
    Schema(db)

    Model.set_connection_resolver(db)

    repository = DatabaseMigrationRepository(db, "migrations")
    migrator = Migrator(repository, db)

    if not repository.repository_exists():
        repository.create_repository()

    migrator.reset("migrations")
    migrator.run("migrations")


@pytest.fixture(scope="module")
def client():
    client = Client(schema=graphene.Schema(query=Query, mutation=Mutation))
    return client


@pytest.fixture(scope="function")
def user():
    user = User()
    user.name = "John Doe"
    user.address = "United States of Nigeria"
    user.phone_number = 123456789
    user.sex = "male"
    user.save()

    return user


@pytest.fixture(scope="function")
def post(user):
    post = Post()
    post.title = "Test Title"
    post.body = "this is the post body and can be as long as possible"

    user.posts().save(post)
    return post


@pytest.fixture(scope="function")
def comment(user, post):
    comment = Comments()
    comment.body = "This is a comment body"

    user.comments().save(comment)
    post.comments().save(comment)

    return comment
