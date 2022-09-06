docker buildx build --platform=linux/arm64,linux/amd64 -t jxch/hulizhushou:$(Get-Date -Format 'yyyyMMddHH') -t jxch/hulizhushou:latest . --push


