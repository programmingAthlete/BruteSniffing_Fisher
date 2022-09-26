from bs4 import BeautifulSoup


def html_parser(file_name: str, output_file: str) -> None:
    """
    Edits the action parameter of the form to index.txt of the file "filename"

    :param      file_name:   input of the file: str
    :param      output_file: edited file:       str
    :return:    void
    """

    with open(file_name, 'r') as f:
        txt = f.read()
    soup = BeautifulSoup(txt, features='lxml')
    tag = soup.form
    tag['action'] = "index.php"
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("---------------------------------------------")
    html = soup.prettify("utf-8")
    with open(output_file, "wb") as file:
        file.write(html)