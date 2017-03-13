from imdbpie import Imdb
imdb = Imdb()
imdb = Imdb(anonymize=True)
var1 = imdb.top_250()
var2 = imdb.search_for_title("The Dark Knight")
print(var2)
text_file = open("/test/src/test/output.txt", "w")
text_file.write(" %s" % var1)
text_file.close()