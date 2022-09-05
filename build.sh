#!/bin/bash
sudo docker buildx build --platform=linux/amd64  -t  jxch/hulizhushou:$(date +%Y%m%d) -t jxch/hulizhushou:latest . --push