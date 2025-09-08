Hadoop – Tesla Sentiment Analysis

This folder documents the Hadoop-based part of the Tesla Sentiment Analysis project.  
The goal was to process raw Reddit posts about Tesla using Hadoop MapReduce, clean the data, and prepare it for SQL analysis and sentiment analysis in Python.  


Folder Structure

- Mapper_and_Reducer - Python scripts for the mapper and reducer.  
- screenshots - Proof of Hadoop daemons running and Hadoop Streaming Job execution.  
- README.md - Documentation of the Hadoop workflow.  


Workflow

1. Start Hadoop Daemons
Before running MapReduce, HDFS and YARN daemons were started:
Command used:
start-dfs.sh
start-yarn.sh

2. Load Data into HDFS - Created an /input directory in HDFS and uploaded the JSON file.
Command used:
hdfs dfs -mkdir -p /input
hdfs dfs -put ConvertedFile.json /input/

3. MapReduce processing
We open the nano text-editor to insert the code for Mapper and Reducer.

4. Run Hadoop Streaming Job
Command used:
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files mapperTeslaSent.py,reduceTeslaSent.py \
  -input /input/ConvertedFile.json \
  -output /output/cleaned_output \
  -mapper mapperTeslaSent.py \
  -reducer reduceTeslaSent.py

5. Saved the data to later export it to PostgreSQL
Command used:
hdfs dfs -get /output/cleaned_output ./cleaned_output


