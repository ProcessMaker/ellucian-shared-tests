# Files 

( Links will be changed to master directory after merge )

## Classes

[`/includes/test_classes.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/includes/test_classes.py "test_classes.py")
Class | Function | Extends
--- | --- | ---
`CustomTestSuite` | Add custom attributes | `unittest.TestSuite`
`CustomTestLoader` | Set custom `suiteClass` | `unittest.TestLoader`
`CustomTextTestResult` | Add custom attributes to instantiation | `unittest.TextTestResult`
`CustomTextTestRunner` | Set custom `resultclass`, add custom attributes, and set custom `_makeResult()` | `unittest.TextTestRunner`

[`/includes/test_parent.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/includes/test_parent.py "test_parent.py")
Class | Function | Extends | Methods | Attributes
--- | --- | --- | --- | ---
`BaseTest` | Defines base test class | `unittest.TestCase` | <ul><li>`setUpClass()`: instantiates webdriver instance</li><li>`tearDownClass()`: closes webdriver instance</li></ul> | <ul><li>`page`: an empty string</li><li>`log`: an empty list</li></ul>

## Methods

[`/includes/api_requests.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/includes/api_requests.py "api_requests.py")
Method | Function | Parameters | Uses
--- | --- | --- | ---
`get_access_token` | <ul><li>Uses post request to acquire access token through password grant</li><li>returns access token and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes server url, server workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>
`get_project_id` | <ul><li>Uses access token to get request project ID of first process on processes page</li><li>returns project id, header token, and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes server url, server workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>
`get_variable_list`| <ul><li>Uses project id to get request variable list of process</li><li>returns response text and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes server url, server workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>
`parse_response` | <ul><li>Parses variable list with `json.loads()` to verify GUI list will be populated</li><li>returns boolean and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes server url, server workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>

[`/includes/util.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/includes/util.py "util.py")
Method | Function | Parameters | Uses
--- | --- | --- | ---
`run_test` | <ul><li>Loads and runs test suite, redirects `unittest` results to memory stream</li><li>returns PM4-friendly output dictionary</li></ul> | `classname, data, modulename` | <ul><li>`classname` passes the test class name</li><li>`data` passes the configuration from PM4's config task</li><li>`modulename` passes `__main__` from test file</li></ul>
`parse_log_error`| <ul><li>Searches text for `'ERROR'`</li><li>returns `ERROR` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
`parse_log_warning`| <ul><li>Searches text for `'WARNING'`</li><li>returns `WARNING` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
`parse_results` | <ul><li>Searches unittest results for `.`, `E`, or `F`</li><li>returns `SUCCESS` or `FAIL`</li></ul> | `buffer` | <ul><li>`buffer` passes memory stream</li></ul>
`login` | <ul><li>Navigates to login page and sends keys to log in</li><li>returns `timezone_check()` method call</li></ul> | `data, driver, log` | <ul><li>`data` passes the configuration from PM4's config task</li><li>`driver` passes webdriver instance</li><li>`log` passes event log</li></ul>
`timezone_check` | <ul><li>Checks that login was successful and looks for timezone checkpoint</li><li>returns driver</li></ul> | `driver, wait` | <ul><li>`driver` passes webdriver instance</li><li>`wait` passes `WebDriverWait` instance</li></ul>
`read_from_json_file` | <ul><li>Reads `JSON` file</li><li>returns decoded JSON: whole file or specific key</li></ul> | `repository_path, filename, key=''` | <ul><li>`repository_path` passes the mounted path from `bootstrap.py`, which loads file in Docker container</li><li>`filename` passes the name of the relative path of the file to read</li><li>`key` passes the name of the nested dictionary desired (optional parameter)</li></ul>
