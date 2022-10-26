class Logger:
    file = "log.txt"
    @staticmethod
    def print_to_file(data):
        f = open(Logger.file, mode='a', encoding='utf-8')
        f.write(str(data) + "\n")
        f.write("\n")
        f.close()

    @staticmethod
    def clear_file():
        f = open(Logger.file, mode='w', encoding='utf-8')
        f.close()