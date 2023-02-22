""" Post Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class Post(Model):
    """Post Model"""

    @has_many("id", "post_id")
    def comments(self):
        from .Comment import Comment

        return Comment
