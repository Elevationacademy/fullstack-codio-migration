#!/bin/bash
. /home/codio/workspace/tests/js-test-lib.sh

start_js_test 'exercise4.js'

run_js_test '[0, 4, 3, 6]' '[3]' '' 'oddArr' 
run_js_test '[2, 34, -5, 43]' '[-5, 43]' '' 'oddArr'  

end_js_test



