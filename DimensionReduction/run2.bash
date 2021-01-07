#!/bin/bash

chmod +x /users/david/AAT_mapper.py
chmod +x /users/david/AAT_reducer.py
chmod +x /users/david/eigen_mapper.py
chmod +x /users/david/eigen_reducer.py
chmod +x /users/david/mmult_mapper.py
chmod +x /users/david/mmult_reducer.py

hadoop jar /usr/hdp/3.0.1.0-187/hadoop-mapreduce/hadoop-streaming-3.1.1.3.0.1.0-187.jar \
-input /users/maria_dev/Project/output1/* -output /users/maria_dev/Project/output2/AAT
-file /users/david/AAT_mapper.py -mapper /users/david/AAT_mapper.py \
-file /users/david/AAT_reducer.py -reducer /users/david/AAT_reducer.py \

hadoop jar /usr/hdp/3.0.1.0-187/hadoop-mapreduce/hadoop-streaming-3.1.1.3.0.1.0-187.jar \
-input /users/maria_dev/Project/output2/AAT -output /users/maria_dev/Project/output2/eigen
-file /users/david/eigen_mapper.py -mapper /users/david/eigen_mapper.py \
-file /users/david/eigen_reducer.py -reducer /users/david/eigen_reducer.py \

hadoop jar /usr/hdp/3.0.1.0-187/hadoop-mapreduce/hadoop-streaming-3.1.1.3.0.1.0-187.jar \
-input /users/maria_dev/Project/output2/eigen -output /users/maria_dev/Project/output2/mmult
-file /users/david/mmult_mapper.py -mapper /users/david/mmult_mapper.py \
-file /users/david/mmult_reducer.py -reducer /users/david/mmult_reducer.py \