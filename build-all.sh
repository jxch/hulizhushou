#!/bin/bash
sudo docker buildx build --platform=linux/arm64,linux/amd64  -t  jxch/hulizhushou:$(date +%Y%m%d%H) -t jxch/hulizhushou:latest . --push