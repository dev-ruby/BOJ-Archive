# -*- coding: utf-8 -*-

import bs4
import clipboard
import os
import requests

os.system("cls")


def get_response(problem_number: str) -> requests.Response:
    url = f"https://www.acmicpc.net/problem/{problem_number}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    return response


def is_reponse_ok(response: requests.Response) -> bool:
    return response.status_code == 200


def get_title(response: requests.Response) -> str:
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    title = soup.select_one("#problem_title").text

    return title


def create_file(problem_number: str, path: str) -> None:
    response = get_response(problem_number)

    assert is_reponse_ok(response), f"백준 서버에 연결할 수 없습니다. {response.status_code}"

    title = get_title(response)

    with open("template.py", "r") as fp:
        template = fp.read()

    with open(path, mode="w", encoding="utf-8") as fp:
        fp.write(template.format(problem_number, title))


def main():
    while True:
        os.system("cls")
        print(" >>>", end="  ")
        command = input().split()
        problem_number = command[1]

        path = rf"problems\{problem_number}.py"

        if command[0] == "open":
            os.system("cls")

            if not os.path.exists(path):
                create_file(problem_number, path)

            title = ""
            with open(path, mode="r", encoding="utf-8") as fp:
                title = fp.readline()[2:]

            while True:
                os.system("cls")
                print(title)
                print("================\n")

                command = input().strip()

                if command == "exit":
                    os.system("cls")
                    break

                elif command == "commit":
                    os.system(f"black {path}")
                    os.system(f"git add {path}")
                    os.system(f'git commit -m "{title}" ')
                    break

                elif command == "copy":
                    with open(path, mode="r", encoding="utf-8") as fp:
                        data = fp.read()
                    clipboard.copy(data)

                print("\n\n\n\n\n\n\n\n\n")

        elif command[0] == "del":
            print("delete? y/n")
            if input() == "y":
                os.remove(path)


if __name__ == "__main__":
    main()
