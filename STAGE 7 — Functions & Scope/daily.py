def read_file(path):
    """Fayldan matnni o'qiydi va qaytaradi."""
    with open(path, "r") as file:
        return file.read()

def count_words(text):
    """Matndagi so'zlar sonini hisoblaydi."""
    return len(text.split())

def main():
    text = read_file("./data.txt")
    total = count_words(text)
    print("So'zlar soni:", total)

main()
