#!/bin/bash

chmod +x /users/david/mapper.py
chmod +x /users/david/reducer.py

hdfs dfs -copyFromLocal /users/maria_dev/Project/input/ /users/david/input
hadoop jar /usr/hdp/3.0.1.0-187/hadoop-mapreduce/hadoop-streaming-3.1.1.3.0.1.0-187.jar \
-input /users/maria_dev/Project/input/* -output /users/maria_dev/Project/output1
-file /users/david/mapper.py -mapper /users/david/mapper.py \
-file /users/david/reducer.py -reducer /users/david/reducer.py \
