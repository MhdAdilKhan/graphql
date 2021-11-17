import graphene

from expertlaptop.queries import Query
from custom_user.schema import Query as CQuery
from custom_user.schema import Mutation as MMutation
from expertlaptop.mutation import Mutation

class Query(Query,CQuery):
    pass

class Mutation(Mutation,MMutation):
    pass

schema = graphene.Schema(query = Query,mutation = Mutation)