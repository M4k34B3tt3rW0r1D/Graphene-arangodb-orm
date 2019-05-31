import sys
# contains env variables
sys.path.append('/app/settings/arangodb')
import config


from database import init_arangodb
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from database import init_arangodb, test
#from testDocumentRelations import initTest
#from testGraph import initGraph


# Remote debugging
# import pydevd_pycharm
# pydevd_pycharm.settrace('91.160.10.43', port=16384, stdoutToServer=True, stderrToServer=True)
# end remote debugging

app = Flask(__name__)
app.debug = True

default_query = '''
query{
  allEmployees{
    totalCount,
    edges{
      node{
        name,
        role{
          id,
          Key,
          name
        },
        department{
          name,
        }
      }
    }
  }
}
             
'''.strip()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    #initGraph()
    init_arangodb()
    test()
    #initTest()
    app.run(host=config.HOST_CONFIG['host'], port=config.HOST_CONFIG['port'])
