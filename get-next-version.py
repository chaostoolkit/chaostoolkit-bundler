from datetime import date


def run():
    with open('VERSION') as f:
        current = f.read()
        new_version = date.today().strftime("%Y.%m.%d")

        if current.startswith(new_version):
            _, index = current.rsplit('.', 1)
            index = int(index) + 1
            print('{}.{}'.format(new_version, index))
            return

        print(new_version)


if __name__ == '__main__':
    run()
