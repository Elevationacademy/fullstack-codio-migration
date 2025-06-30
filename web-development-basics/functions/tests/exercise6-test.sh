#!/bin/bash
. /home/codio/workspace/tests/js-test-lib.sh

start_js_test 'exercise6.js'

run_js_test '4, 7' '11' '' 'calculator.add' 
run_js_test '11, 7' '4' '' 'calculator.subtract'  

end_js_test



