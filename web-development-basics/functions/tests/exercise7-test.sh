#!/bin/bash
. /home/codio/workspace/tests/js-test-lib.sh

start_js_test 'exercise7.js'

run_js_test "'david', 200" 'His Royal Highness, DAVID has 1000 gold coins' '' 'turnToKing'
run_js_test "'John'" 'His Royal Highness, John' '' 'makeRegal'
run_js_test "400, 'Sam'" '1200' '' 'increaseByNameLength'  

end_js_test



