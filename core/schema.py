import strawberry
from strawberry.schema import Schema

from blog.queries import BlogQueries

@strawberry.type
class Query(BlogQueries):
    pass

schema = Schema(query=Query)
