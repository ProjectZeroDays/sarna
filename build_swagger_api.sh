#!/usr/bin/env bash

DIR=./swagger
CODEGEN_DIR=./lib
CODEGEN=${CODEGEN_DIR}/codegen-cli.jar

export PYTHON_POST_PROCESS_FILE=/bin/yapf

if [[ ! -f ${CODEGEN} ]]; then
    mkdir -p ${CODEGEN_DIR}
    wget https://oss.sonatype.org/content/repositories/snapshots/org/openapitools/openapi-generator-cli/4.0.0-SNAPSHOT/openapi-generator-cli-4.0.0-20181124.120224-42.jar \
        -O ${CODEGEN}
fi

java -jar ${CODEGEN} generate -c ${DIR}/config.json -o . -i ${DIR}/api.yaml --generator-name python-flask

rsync -a --filter=':- .openapi-generator-ignore' sarna.routes.api/* sarna/routes/api/

rm -r sarna.routes.api 2> /dev/null
rm -r .openapi-generator 2> /dev/null
rm -r .swagger-codegen 2> /dev/null
