from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from core.schema import schema

graphl_app = GraphQLRouter(schema)
app = FastAPI()

app.include_router(graphl_app, prefix="/graphql")
