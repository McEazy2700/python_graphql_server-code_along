from typing import List
import strawberry

from blog.types import PostType


@strawberry.type
class BlogQueries:
    @strawberry.field
    def posts(self) -> List[PostType]:
        posts = [ PostType(title="Test Post", summary="Testing post", body="Testing with hard codded data") ]
        return posts
