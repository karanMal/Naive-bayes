
## flushing folders first

rm -r /home/kmkaran212/results/*

hadoop fs -rm /user/kmkaran212/results/*

hadoop fs -rm -r /user/kmkaran212/output



## Training commands


hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapred.map.tasks=4 -D mapred.reduce.tasks=4 -files /home/kmkaran212/ass1/mapper.py,/home/kmkaran212/ass1/reducer.py -mapper /home/kmkaran212/ass1/mapper.py -combiner /home/kmkaran212/ass1/reducer.py -reducer /home/kmkaran212/ass1/reducer.py -input /user/ds222/assignment-1/DBPedia.full/full_train.txt -output /user/kmkaran212/output

hadoop fs -cat /user/kmkaran212/output/* > /home/kmkaran212/results/out_.txt
sort /home/kmkaran212/results/out_.txt > /home/kmkaran212/results/out.txt
hadoop fs -copyFromLocal /home/kmkaran212/results/out.txt /user/kmkaran212/results/
hadoop fs -rm -r /user/kmkaran212/output





## Testing Commands 


hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapred.map.tasks=4 -D mapred.reduce.tasks=4 -files /home/kmkaran212/ass1/mapper1.py,/home/kmkaran212/ass1/reducer1.py -mapper /home/kmkaran212/ass1/mapper1.py -reducer /home/kmkaran212/ass1/reducer1.py -cacheFile /user/kmkaran212/results/out.txt#train_dict -input /user/ds222/assignment-1/DBPedia.full/full_test.txt -output /user/kmkaran212/output


hadoop fs -cat /user/kmkaran212/output/* > /home/kmkaran212/results/out_1.txt
sort /home/kmkaran212/results/out_1.txt > /home/kmkaran212/results/out1.txt
hadoop fs -copyFromLocal /home/kmkaran212/results/out1.txt /user/kmkaran212/results/
hadoop fs -rm -r /user/kmkaran212/output


hadoop fs -copyToLocal /user/ds222/assignment-1/DBPedia.full/full_test.txt /home/kmkaran212/results/
awk '{printf "%d\t%s\n", NR, $0}' /home/kmkaran212/results/full_test.txt > /home/kmkaran212/results/full_test_id.txt
hadoop fs -copyFromLocal /home/kmkaran212/results/full_test_id.txt /user/kmkaran212/results/


hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapred.map.tasks=4 -D mapred.reduce.tasks=4 -files /home/kmkaran212/ass1/mapper2.py,/home/kmkaran212/ass1/reducer2.py,/home/kmkaran212/ass1/combiner2.py -mapper /home/kmkaran212/ass1/mapper2.py -combiner /home/kmkaran212/ass1/combiner2.py -reducer /home/kmkaran212/ass1/reducer2.py -cacheFile /user/kmkaran212/results/out1.txt#test_dict -input /user/kmkaran212/results/full_test_id.txt -output /user/kmkaran212/output

#hadoop fs -cat /user/kmkaran212/output/* > /home/kmkaran212/results/out_2.txt
#sort /home/kmkaran212/results/out_2.txt > /home/kmkaran212/results/out2.txt
hadoop fs -copyFromLocal /home/kmkaran212/results_/out2.txt /user/kmkaran212/results/
hadoop fs -rm -r /user/kmkaran212/output


hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapred.map.tasks=4 -D mapred.reduce.tasks=6 -D stream.map.output.field.separator='\t' -D stream.num.map.output.key.fields=2 -D mapred.text.key.partitioner.options=-k1,1 -files /home/kmkaran212/ass1/mapper3.py,/home/kmkaran212/ass1/reducer3.py -mapper /home/kmkaran212/ass1/mapper3.py -reducer /home/kmkaran212/ass1/reducer3.py -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -input /user/kmkaran212/results/out2.txt -output /user/kmkaran212/output


hadoop fs -cat /user/kmkaran212/output/* > /home/kmkaran212/results/out_3.txt
sort /home/kmkaran212/results/out_3.txt > /home/kmkaran212/results/out3.txt
hadoop fs -copyFromLocal /home/kmkaran212/results/out3.txt /user/kmkaran212/results/
hadoop fs -rm -r /user/kmkaran212/output



hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapred.map.tasks=4 -D mapred.reduce.tasks=1 -files /home/kmkaran212/ass1/mapper4.py,/home/kmkaran212/ass1/reducer4.py -mapper /home/kmkaran212/ass1/mapper4.py -reducer /home/kmkaran212/ass1/reducer4.py -input /user/kmkaran212/results/out3.txt -output /user/kmkaran212/output

hadoop fs -cat /user/kmkaran212/output/* > /home/kmkaran212/results/out4.txt
hadoop fs -copyFromLocal /home/kmkaran212/results/out4.txt /user/kmkaran212/results/



## for printing test_accuracy

python3 /home/kmkaran212/ass1/print_accuracy.py




