#!/bin/bash

curl -X POST 'http://localhost:8086/api/v2/delete?org=telegraf&bucket=telegraf' \
    -H 'Authorization: Token 2YQJbyziFaiDGBoGnv6YLADSKhMzf-OU037poYfMi9uNjFa7NXdqHjmJzeLxFGauo_JUwe9VaDjqi3P6HignFw==' \
    -H 'Content-Type: application/json' \
    --data '{"start": "2022-01-01T00:00:00Z", "stop": "2022-12-12T00:00:00Z"}'