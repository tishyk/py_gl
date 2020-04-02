import argparse

parser = argparse.ArgumentParser()
parser.add_argument('agent_ip', type=str, help="Agent IP address to obtaining the file system")
parser.add_argument('-agent_password', '--p', dest='password', metavar='password', type=str,
                    help="Agent host 'root' password")
parser.add_argument('--master_ip', default='127.0.0.0',
                    help=argparse.SUPPRESS)  # Argument transferred to ESD agent.py call

args = parser.parse_args()
print(args.agent_ip, args.password)
print(args.master_ip)
