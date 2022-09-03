#!/bin/bash

ZSCALER_CERT_FILE=/Users/white1/Downloads/ZscalerRootCerts/ZscalerRootCertificate-2048-SHA256.crt

MARKER_STRING="zscaler-certificate"

while read -r certFile;
do
    grep -i "${MARKER_STRING}" "${certFile}" > /dev/null
    exitCode="$?"
    if [[ $exitCode -eq 0 ]]; then
        true
    else
        echo "Patching ${certFile} to include ZScaler certificate from ${ZSCALER_CERT_FILE}"
        cat ${certFile} <(echo "${MARKER_STRING}") ${ZSCALER_CERT_FILE} > new-cert-file.pem
        mv new-cert-file.pem ${certFile}
    fi
done < <(find . -name *.pem)
