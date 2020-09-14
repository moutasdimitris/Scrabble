import classes


def guidelines():
    '''
    gbgfbfgb
    :return:
    '''
    print(guidelines().__doc__)
    return None


def start_game():
    classes.Game().setup()


if __name__ == "__main__":
    start_game()
