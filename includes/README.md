## Files 

( Links will be changed to master directory after merge )

[`/includes/api_requests.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/includes/api_requests.py "api_requests.py")
Method | Function | Parameters | Uses
--- | --- | --- | ---
`get_access_token` | <ul><li>Uses post request to acquire access token through password grant</li><li>returns access token and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes url, workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>
`get_project_id` | <ul><li>Uses access token to get request project ID of first process on processes page</li><li>returns project id, header token, and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes url, workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>
`get_variable_list`| <ul><li>Uses project id to get request variable list of process</li><li>returns response text and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes url, workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>
`parse_response` | <ul><li>Parses variable list with `json.loads()` to verify GUI list will be populated</li><li>returns boolean and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes url, workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>

[`/includes/util.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/includes/util.py "util.py")
Method | Function | Parameters | Uses
--- | --- | --- | ---
`run_test` | <ul><li>Loads and runs test suite, redirects `unittest` results to memory stream</li><li>returns PM4-friendly output dictionary</li></ul> | `classname, data, modulename` | <ul><li>`classname` passes the test class name</li><li>`data` passes the configuration in PM4's config task</li><li>`modulename` passes `__main__` from test file</li></ul>
`parse_log_error`| <ul><li>Searches text for `'ERROR'`</li><li>returns `ERROR` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
`parse_log_warning`| <ul><li>Searches text for `'WARNING'`</li><li>returns `WARNING` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
`parse_results` | <ul><li>Searches unittest results for `.`, `E`, or `F`</li><li>returns `SUCCESS` or `FAIL`</li></ul> | `buffer` | <ul><li>`buffer` passes memory stream</li></ul>
