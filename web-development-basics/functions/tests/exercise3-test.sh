#!/bin/bash
. /home/codio/workspace/tests/js-test-lib.sh

start_js_test 'exercise3.js'

run_js_test '-5' 'false' '' 'isEven' 
run_js_test '3' 'false' '' 'isEven' 
run_js_test '4' 'true' '' 'isEven' 

end_js_test



