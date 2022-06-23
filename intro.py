import pyspark

sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:///us/share/doc/python/copyright')
print(txt.count())