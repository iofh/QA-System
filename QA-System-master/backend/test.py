from q_a_transformers import question_answer


def main():
    abc = question_answer('op', 'what is op address')
    print(abc)
    print(type(abc))


if __name__ == "__main__":
    main()


