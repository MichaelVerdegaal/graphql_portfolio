from flask import Flask
from flask_graphql import GraphQLView

from util.db_session import session
from schema import schema

app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    return "Welcome, this is a GraphQL API running on Flask!"


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                                                           schema=schema,
                                                           graphiql=True))


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


if __name__ == '__main__':
    app.run()
