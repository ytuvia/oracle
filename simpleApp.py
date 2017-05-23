from pyspark import SparkContext

logFile = "/Users/yuramolodez/jud/spark-2.1.1-bin-hadoop2.7/README.md"
sc = SparkContext("local", "simple app")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

sc.stop()