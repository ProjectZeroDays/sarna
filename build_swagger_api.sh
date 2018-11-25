#!/usr/bin/env bash

DIR=./swagger
CODEGEN_DIR=./lib
CODEGEN=${CODEGEN_DIR}/codegen-cli.jar

if [[ ! -f ${CODEGEN} ]]; then
    mkdir -p ${CODEGEN_DIR}
    wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar \
        -O ${CODEGEN}
fi

java -jar ${CODEGEN} generate -c ${DIR}/config.json -o . -i ${DIR}/api.yaml -l python-flask

rsync -a --filter=':- .swagger-codegen-ignore' sarna.routes.api/* sarna/routes/api/

rm -r sarna.routes.api
rm -r .swagger-codegen
