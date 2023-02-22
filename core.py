from typing import List, Optional

import strawberry

from controller import CreateMutation, Queries
from schema import UserType, PostType, CommentsType


@strawberry.type
class Mutation:
    add_user: UserType = strawberry.mutation(resolver=CreateMutation.add_user)
    add_post: PostType = strawberry.mutation(resolver=CreateMutation.add_post)
    add_comment: CommentsType = strawberry.mutation(resolver=CreateMutation.add_comment)


@strawberry.type
class Query:
    users: List[UserType] = strawberry.field(resolver=Queries.get_all_users)
    get_single_user: UserType = strawberry.field(resolver=Queries.get_single_user)
