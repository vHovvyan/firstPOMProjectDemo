class Lib:

    def writeToFile(self, links):
        try:
            with open('test_file.txt', 'a') as f:
                for link in links:
                    href = link.get_attribute('href')
                    f.write(str(href) + "\n")
        except (IOError, ValueError, EOFError) as error:
            print(error)
            raise Exception("Unexpected error to write in file")
        finally:
            f.close()
