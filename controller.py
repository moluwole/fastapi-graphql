from typing import List

from models.Comment import Comment
from models.Post import Post
from models.User import User
from schema import CommentInput, CommentsType, PostInput, PostType, UserInput, UserType


class CreateMutation:

    def add_user(self, user_data: UserInput):
        user = User.where("email", user_data.email).get()
        if user:
            raise Exception("User already exists")

        user = User()

        user.name = user_data.name
        user.email = user_data.email
        user.address = user_data.address
        user.phone_number = user_data.phone_number
        user.sex = user_data.sex

        user.save()

        return user

    def add_post(self, post_data: PostInput):
        user = User.find(post_data.user_id)
        if not user:
            raise Exception("User not found")
        post = Post()
        post.title = post_data.title
        post.body = post_data.body
        post.user_id = post_data.user_id
        post.save()

        user.attach("posts", post)

        return post

    def add_comment(self, comment_data: CommentInput):
        post = Post.find(comment_data.post_id)
        if not post:
            raise Exception("Post not found")
        user = User.find(comment_data.user_id)
        if not user:
            raise Exception("User not found")

        comment = Comment()
        comment.body = comment_data.body
        comment.user_id = comment_data.user_id
        comment.post_id = comment_data.post_id

        comment.save()

        user.attach("comments", comment)
        post.attach("comments", comment)

        return comment


class Queries:

    def get_all_users(self) -> List[UserType]:
        return User.all()

    def get_single_user(self, user_id: int) -> UserType:
        user = User.find(user_id)
        if not user:
            raise Exception("User not found")
        return user
