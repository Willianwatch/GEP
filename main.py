from ga_mgg import mgg


def main():
    terminator = mgg.Population(restriction=10)
    terminator.mgg(1000)
    print(terminator[terminator.search_for_best(i.fitness for i in terminator)])


if __name__ == "__main__":
    main() 