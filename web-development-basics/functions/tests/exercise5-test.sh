#!/bin/bash
. /home/codio/workspace/tests/js-test-lib.sh

start_js_test 'exercise5.js'

run_js_test '[0, 4, 3, 6], 7' 'false' '' 'checkExists' 
run_js_test '[2, 34, -5], -5' 'true' '' 'checkExists'  

end_js_test



