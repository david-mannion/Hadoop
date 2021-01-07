#!/bin/bash
i=1
while :
do
	hadoop jar /usr/hdp/3.0.1.0-187/hadoop-mapreduce/hadoop-streaming-3.1.1.3.0.1.0-187.jar -file /home/maria_dev/centroids.txt -file /home/maria_dev/km_mapper.py -mapper ./home/maria_dev/km_mapper.py -file /home/maria_dev/km_reducer.py -reducer /home/maria_dev/km_reducer.py -input /users/maria_dev/Project/Input3/testMapReduce/dataset.txt -output /users/maria_dev/Project/Input3/testMapReduce/mapreduce-output$i
	rm -f centroids1.txt
	hadoop fs -copyToLocal /users/maria_dev/Project/Input3/testMapReduce/mapreduce-output$i/part-00000 centroids1.txt
	seeiftrue=`python reader.py`
	if [ $seeiftrue = 1 ]
	then
		rm centroids.txt
		hadoop fs -copyToLocal /users/maria_dev/Project/Input3/testMapReduce/mapreduce-output$i/part-00000 centroids.txt
		break
	else
		rm centroids.txt
		hadoop fs -copyToLocal /users/maria_dev/Project/Input3/testMapReduce/mapreduce-output$i/part-00000 centroids.txt
	fi
	i=$((i+1))
done
