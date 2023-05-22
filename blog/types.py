import strawberry


@strawberry.type
class PostType:
    id: int
    title: str
    summary: str
    body: str
