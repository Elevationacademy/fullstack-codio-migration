#!/bin/bash

cd /home/codio/workspace/exercises

DEFAULT_FAILURE_MESSAGE='Your output was incorrect. Try again.'

function start_js_test {
  echo "<h3>Program Output</h3>"

  JS_TEST_SCRIPT="${1}"
  
  if [ "${2}" != "" ]; then
    DEFAULT_FAILURE_MESSAGE="${2}"
  fi

}

LAST_SUCCESS=""

# 
# 1: ARGS to script
# 2: Expected output from script
# 3: Optional error message
#
function run_js_test {
  ARGS="${1}"
  if [ "${4}" == "" ]; then
    ACTUAL_OUTPUT=$(node "${JS_TEST_SCRIPT}" ${ARGS})
    if [ $? -ne 0 ]; then
      # bad exit code
      exit 1
    fi
  else
    function_test "${4}(${ARGS})"
#     echo "${FUNCTION_TO_CALL}"
  fi
  
  EXPECTED_OUTPUT="${2}"
  
  MESSAGE_ON_ERROR=${DEFAULT_FAILURE_MESSAGE}
  if [ "${3}" != "" ]; then
    MESSAGE_ON_ERROR="${3}"
  fi
  
  if [ "$ACTUAL_OUTPUT" == "$EXPECTED_OUTPUT" ]; then
    LAST_SUCCESS="<small><b>Input:</b> ${ARGS}</small>"
    LAST_SUCCESS="${LAST_SUCCESS}<br/><small><b>Your Output: </b></small>${ACTUAL_OUTPUT}"
    LAST_SUCCESS="${LAST_SUCCESS}<br/><small><b>Tested Function:</b> </small>${4}"
    return 0
  fi
  echo "<small><b>Program Failed for Input: </b></small>${ARGS}"
  echo "<small><b>Expected Output:</b> </small>${EXPECTED_OUTPUT}"
  echo "<small><b>Your Program Output:</b> </small>${ACTUAL_OUTPUT}"
  echo "<small><b>Tested Function:</b> </small>${4}"

  echo "<br/>${MESSAGE_ON_ERROR}"
  exit 1
}

function end_js_test {
  echo ${LAST_SUCCESS}
  echo "<hr/><h3>Challenge Feedback</h3>"
  echo "Well done!"
  exit 0
}

function function_test {
  FUNCTION_TO_CALL=${1}
  ACTUAL_OUTPUT=$(node <<EOF
    var fs = require('fs');
    var stdout= console.log;
    console.log= function(){};
    eval(fs.readFileSync("${JS_TEST_SCRIPT}", 'UTF8'));
    console.log= stdout;
    console.log(${FUNCTION_TO_CALL})
EOF
)
}


