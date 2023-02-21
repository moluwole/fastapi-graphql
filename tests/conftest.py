import pytest
from masoniteorm.migrations import Migration

from models.Comment import Comment
from models.Post import Post
from models.User import User


@pytest.fixture(autouse=True)
def setup_database():
    config_path = "config/test_config.py"

    migrator = Migration(config_path=config_path)
    migrator.create_table_if_not_exists()

    migrator.refresh()


@pytest.fixture(scope="function")
def user():
    user = User()
    user.name = "John Doe"
    user.address = "United States of Nigeria"
    user.phone_number = 123456789
    user.sex = "male"
    user.email = "foo@bar.com"
    user.save()

    return user


@pytest.fixture(scope="function")
def post(user):
    post = Post()
    post.title = "Test Title"
    post.body = "this is the post body and can be as long as possible"
    post.user_id = user.id
    post.save()

    user.attach("posts", post)
    return post


@pytest.fixture(scope="function")
def comment(user, post):
    comment = Comment()
    comment.body = "This is a comment body"
    comment.user_id = user.id
    comment.post_id = post.id

    comment.save()

    user.attach("comments", comment)
    post.attach("comments", comment)

    return comment
