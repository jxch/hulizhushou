docker buildx build --platform=linux/arm64,linux/amd64 -t jxch/hulizhushou:$(Get-Date -Format 'yyyyMMdd') -t jxch/hulizhushou:latest . --push


