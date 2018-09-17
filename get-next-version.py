from datetime import date


def run():
    with open('VERSION') as f:
        current = f.read().strip()
        new_version = date.today().strftime("%Y.%m.%d")

        if current and current.startswith(new_version):
            if new_version == current:
                index = 0
            else:
                _, index = current.rsplit('.', 1)
            index = int(index) + 1
            print('{}.{}'.format(new_version, index))
            return

        print(new_version)


if __name__ == '__main__':
    run()
