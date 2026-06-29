#!/bin/bash
TIME_STAMP=$(date +%Y%m%d-%H%M)

if [[ "$(uname)" == "Darwin" ]]; then
  export ALLURE_TOKEN=$(security find-generic-password -a "$USER" -s "TESTING_ALLURE_TOKEN" -w)
  export ALLURE_ENDPOINT=$(security find-generic-password -a "$USER" -s "TESTING_ALLURE_ENDPOINT" -w)
fi

export ALLURE_PROJECT_ID=${1:-14832}

export ALLURE_LAUNCH_NAME="$(date "+%Y-%m-%d %H%M%S") local launch"
export ALLURE_RESULTS=allure-results


# launch's configuration

export COMMAND_USED=watch

export ALLURE_LAUNCH_TAGS="pytest, allurectl, ${COMMAND_USED}"

rm -rf ${ALLURE_RESULTS}
mkdir ${ALLURE_RESULTS}


sleep 2

allurectl ${COMMAND_USED} -- pytest tests