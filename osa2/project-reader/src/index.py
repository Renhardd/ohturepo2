from project_reader import ProjectReader


def main():
    #Alkuperäinen url ei toimi ja menee tyhjälle sivulle
    #Kävin kaivamassa itse toimivan
    #Alkuperäinen: url = "https://raw.githubusercontent.com/ohjelmistotuotanto-hy/tehtavat/main/viikko2/test-project/pyproject.toml"
    url = "https://raw.githubusercontent.com/ohjelmistotuotanto-jyu/tehtavat/refs/heads/main/osa2/test-project/pyproject.toml"
    reader = ProjectReader(url)
    print(reader.get_project())


if __name__ == "__main__":
    main()
