#!/bin/bash
. /home/codio/workspace/tests/js-test-lib.sh

start_js_test 'exercise1.js'

run_js_test '2017, 1989' '28' '' 'calcAge'
run_js_test '2021, 2000' '21' '' 'calcAge'

end_js_test

