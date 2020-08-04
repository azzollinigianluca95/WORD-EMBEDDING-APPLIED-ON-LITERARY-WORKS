from __future__ import print_function
import ListSum

from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec

class Main():

   def __init__(self):

      self.sc = SparkContext(appName='Word2Vec')
      self.word2vec = Word2Vec()


   def run(self, input_file_path, word, iterations):

      doc = self.sc.textFile(input_file_path).map(lambda row: row.split(" "))

      synonyms_list = ListSum.ListSum([])


      for x in range(iterations):

         model = self.word2vec.setVectorSize(500).fit(doc)
         synonyms = model.findSynonyms(word, 20)

         synonyms_list.addList(synonyms)


      synonyms_list.orderList()

      return (synonyms_list.terms_list)

      self.sc.stop()


