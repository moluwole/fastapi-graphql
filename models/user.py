""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class User(Model):
    """User Model"""

    @has_many("id", "user_id")
    def posts(self):
        from .Post import Post

        return Post

    @has_many("id", "user_id")
    def comments(self):
        from .Comment import Comment

        return Comment
