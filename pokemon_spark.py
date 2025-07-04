from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, row_number
from pyspark.sql.window import Window

# Initialize Spark Session
spark = SparkSession.builder.appName("PokemonFeistiness").getOrCreate()

# Loading the Datset from HDFS to a spark dataframe
df = spark.read.option("header", "true").csv("hdfs:///pokemon/pokemon.csv")

# only selecting the colums that will be used and casting them properly where required
df = df.select(
    col("type1"),
    col("type2"),
    col("name"),
    col("attack").cast("float"),
    col("weight_kg").cast("float")
)

# As the main file(pokemon.csv) contaisn some valuees where weight is null , tis may cause division by zero error
# to avoid this , we simply filter out these rows where weith-kg is null
df = df.filter(df["weight_kg"] > 0)


# calculating the feistnes of the pokemon based on the given formula : (F = attack / weight) upto 2 decimal places
df = df.withColumn("feistiness", round(col("attack") / col("weight_kg"), 2))

# As the output does not requires attack and weight columns , we drop them
df = df.drop("attack", "weight_kg")

# Window functions is used to rank the pokemons by type1 by feistiness to get the highest for each type
get_high_feistness = Window.partitionBy("type1").orderBy(col("feistiness").desc())
df_ranked = df.withColumn("rank", row_number().over(get_high_feistness))
df_top = df_ranked.filter(col("rank") == 1).drop("rank")


# Save the output to HDFS in CSV format
# the path is hdfs path 
df_top.write.option("header", "true").csv("hdfs:///pokemon/pokemon_output.csv")

# Stop the Spark session
spark.stop()
