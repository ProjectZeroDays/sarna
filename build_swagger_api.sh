#!/usr/bin/env bash

java -jar ./lib/swagger-codegen-cli.jar generate -c ./swagger/config.json -o . -i ./swagger/api.yaml -l python-flask
rsync -a --filter=':- .swagger-codegen-ignore' sarna.routes.api/* sarna/routes/api/
rm -r sarna.routes.api
rm -r .swagger-codegen