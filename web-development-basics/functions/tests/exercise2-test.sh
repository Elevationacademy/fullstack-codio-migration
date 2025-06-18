#!/bin/bash
. /home/codio/workspace/tests/js-test-lib.sh

start_js_test 'exercise2.js'

run_js_test '2017, 1989' 'You are either 27 or 28' '' 'calcAge' 
run_js_test '2021, 2000' 'You are either 20 or 21' '' 'calcAge' 

end_js_test



