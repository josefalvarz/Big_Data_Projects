Hadoop Execution Proof – Tesla Sentiment Analysis

This folder contains screenshots that demonstrate the execution of Hadoop during the Tesla Sentiment Analysis project.

1. Start DFS and YARN Daemons
- Verified that Hadoop services were running with the jps command.  
- Shows active daemons: NameNode, DataNode, SecondaryNameNode, ResourceManager, NodeManager.  

2. Run Hadoop Streaming Job
- Executed the Hadoop Streaming job with  mapper and reducer scripts.  
- Input: ConvertedFile.json (Reddit posts).  
- Output: /output/cleaned_output.  
