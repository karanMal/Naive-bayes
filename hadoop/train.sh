## flushing folders first

rm -r /home/kmkaran212/results/*

hadoop fs -rm /user/kmkaran212/results/*

hadoop fs -rm -r /user/kmkaran212/output

hadoop fs -rm -r /user/kmkaran212/.Trash

## Training commands


hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapred.map.tasks=2 -D mapred.reduce.tasks=1 -files /home/kmkaran212/ass1/mapper.py,/home/kmkaran212/ass1/reducer.py -mapper /home/kmkaran212/ass1/mapper.py -combiner /home/kmkaran212/ass1/reducer.py -reducer /home/kmkaran212/ass1/reducer.py -input /user/ds222/assignment-1/DBPedia.full/full_train.txt -output /user/kmkaran212/output

hadoop fs -cat /user/kmkaran212/output/* > /home/kmkaran212/results/out_.txt
sort /home/kmkaran212/results/out_.txt > /home/kmkaran212/results/out.txt
hadoop fs -copyFromLocal /home/kmkaran212/results/out.txt /user/kmkaran212/results/
hadoop fs -rm -r /user/kmkaran212/output
