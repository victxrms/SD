import argparse


def main(host, port):
    # ...


    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--port', default=1024, help="listening port")
        parser.add_argument('--host', default='localhost', help="hostname")
        args = parser.parse_args()

        main(args.host, args.port)
