#!/usr/bin/env bash

DIR=./swagger
CODEGEN_DIR=./lib
CODEGEN=${CODEGEN_DIR}/codegen-cli.jar

if [[ ! -f ${CODEGEN} ]]; then
    mkdir -p ${CODEGEN_DIR}
    wget http://central.maven.org/maven2/org/openapitools/openapi-generator-cli/3.3.3/openapi-generator-cli-3.3.3.jar \
        -O ${CODEGEN}
fi

java -jar ${CODEGEN} generate -c ${DIR}/config.json -o . -i ${DIR}/api.yaml --generator-name python-flask

rsync -a --filter=':- .openapi-generator-ignore' sarna.routes.api/* sarna/routes/api/

rm -r sarna.routes.api
rm -r .swagger-codegen
