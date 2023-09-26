#!/bin/bash
spark-submit \
  --master local[*] \
  --deploy-mode client \
  --executor-memory 2g \
  --num-executors 5 \
  --executor-cores 2 \
  /streaming-app/scripts/stream_to_kafka.py