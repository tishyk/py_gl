# This is the code that runs this example.
import Pyro5.api
import argparse
from person import Person

parser = argparse.ArgumentParser()
parser.add_argument('-ip', default='192.168.0.105')
parser.add_argument('-p', '--port', default=9000, type=int)
parser.add_argument('-ron', dest='remote', default="warehouse")

args = parser.parse_args()

warehouse = Pyro5.api.Proxy("PYRO:{}@{}:{}".format(args.remote, args.ip, args.port))

sergii = Person("Sergii")
janet = Person("Janet")
henry = Person("Henry")
sergii.visit(warehouse)
janet.visit(warehouse)
henry.visit(warehouse)
