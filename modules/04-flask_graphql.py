# 04-flask_graphql


# http://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/

# check the tutorial here

'''
Normal flask has its view function, but for graphql url, it will have its own 
view function. view function tell flask how to handle the request and response data.

'''

# flask_sqlalchemy/app.py
from flask import Flask
from flask_graphql import GraphQLView

from models import db_session
from schema import schema, Department

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()