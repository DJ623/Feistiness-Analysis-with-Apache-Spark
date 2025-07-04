**Big Data Assignment 02: ReadMe**  
Author : Digvijay Jondhale  
Student ID: 0862899

**Overview :** 

This assignment showcases Apache Spark Job usingspark dataframe API using Python to calculate the “feistiness” for each pokemon, find the feistiest pokemon for each type 1 category, and output to a csv file.

## **Prerequisites**

1. **Hadoop installed** (version 3.4.0 on M1 Mac)  
2. **Spark installed** (version 3.5.5 )  
3. **Python 3.9.6** (PySpark requires Python)  
4. **Java 8 or later** (required by Spark)  
5. **Hadoop configurations** should be correctly set up for HDFS and YARN.  
6. Make sure the pokemon.csv file and the script (pokemon\_spark.py) are in same directory.

Environment Details : 

1. Machine :Macbook Air M1  
2. Architecture : ARM-64  
3. Operating System : macOS (Unix Based)

**Deployment :**

1. **Start Hadoop:**   
   In terminal: 

start-all.sh

2. **Check if all services of Hadoop are started (Namenode, Datanode, ResourceManager, SecondaryNameNode, NodeManager, Jps):**   
   In terminal:    
   jps

This shows that Hadoop has started successfully, and it is in pseudo-distributed mode.

3. **Create a new directory named “pokemon” on HDFS:**   
   In terminal: 

hdfs dfs \-mkdir /name/of/directory

Example :  
hdfs dfs \-mkdir /pokemon

You can check the directory using the web interface by visiting [http://localhost:9870](http://localhost:9870) (default port for hadoop configured in core-site.xml)

4. **Upload the pokemon.csv file to the hdfs directory created in the previous step:**  
   In terminal: 

hdfs dfs \-put /path/to/local/file.csv  /path/of/hdfs/directory 

Example :  
hdfs dfs \-put pokemon.csv  /pokemon

5. **Run the pokemon\_spark.py program :**   
   spark-submit \--master yarn pokemon\_spark.py  
     
   –maste yarnr : used to specify that YARN should be used as cluster manager   
   By default this command will run the script into cluster mode.  
 


6. **Copy the output file generated as pokemon\_output.csv to local storage from HDFS :**   
   In terminal:   
   hadoop fs \-copyToLocal /path/of/hdfs/output/file  /path/on/local/storage  
   

Example :  
hadoop fs \-copyToLocal /pokemon/pokemon\_output.csv/part-00000-67d0a64c-e711-4c56-b871-c95c4a24addd-c000.csv /Users/digvijay/

**Key Implementation Choices:** 

1. **Environment:**   
* Hadoop 3.4.0 was used as this was the latest version available for Mac’s with the M1 chip. The virtual machine was not used as the M1 chip has some issues with virtualization and it can support Hadoop natively.

* To make it work with spark , these two configurations were made in bash shell : 

  * export HADOOP\_CONF\_DIR=/path/to/hadoop-3.x.x/etc/hadoop

  * export YARN\_CONF\_DIR=/path/to/hadoop-3.x.x/etc/hadoop

* Apache Spark Dataframe API was used as it makes it easier to code due to its inbuild functions which are similar to dataframe like pandas, also its ease to connect with hadoop (the path for input and output are provide in the script itself).

2. **Processing**  
* As the CSV file contains multiple columns, I have extracted only type1, type2 , name\], weight\_kg, attack and feistiness (calculated) to make the processing easier. Before writing out the file to csv , the attack and weight\_kg columns are dropped.

* In the script file, the weight value is verified to avoid the DIVISION\_BY\_ZERO error, as in the csv file there are multiple entries with weight values of null or zero, which are skipped.

* For rows that contain blank values for Type 2, they are still considered and kept blank in the output csv file. 

  