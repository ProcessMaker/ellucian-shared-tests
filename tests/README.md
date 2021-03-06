# Files 

## Tests

File | Class | Function | Success | Failure
--- | --- | --- | --- | ---
[`test_1_up.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/master/tests/test_1_up.py "test_1_up.py") | TestLoginPage | Navigate to Login Page and verify login succeeds | `Main page loaded successfully` | `Main page failed to load`
[`test_2_1_mysql_version.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/master/tests/test_2_1_mysql_version.py "test_2_1_mysql_version.py") | TestRDSVersions | Navigate to Case List Cache Builder page and verify correct MySQL version | `Correct MySQL version` | `Wrong MySQL version`
[`test_2_component_versions.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/master/tests/test_2_component_versions.py "test_2_component_versions.py") | TestComponentVersions | Navigate to System Information page and verify correct component versions | `Correct [component]` | `Wrong [component]`
[`test_3_variables_load.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/master/tests/test_3_variables_load.py "test_3_variables_load.py") | TestVariablesLoad | Navigate to applications page to get client id and client secret, then make api requests to verify process variables list loads correctly | `Variable list loaded` | `JSON Decode Error. First 20 chars of response: [first 20 chars of response]`
[`test_4_language_spot_check.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/master/tests/test_4_language_spot_check.py "test_4_language_spot_check.py") | TestLanguageSpotCheck | Navigate to main page, change the url to different language versions, and verify there are no label placeholders instead of translated values | `Labels not found` | `Labels found`
[`test_5_plugin_versions.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/master/tests/test_5_plugin_versions.py "test_5_plugin_versions.py") | TestPluginVersions | Navigate to Plugins Manager page and verify custom plugin versions are correct | <ul><li>`Correct [plugin] version, Enabled`</li><li>`All plugins found`</li></ul> | <ul><li>`Wrong [plugin] version, Enabled`</li><li>`Correct [plugin] version, Disabled`</li><li>`Wrong [plugin] version, Disabled`</li><li>`Not found: [plugins]`</li></ul>


#### Writing New Tests

File structure with comments in `test_template.py`.

### Helpful Links 

(Hover for https:// address)
* [Python unittest Documentation](https://docs.python.org/3.5/library/unittest.html "https://docs.python.org/3.5/library/unittest.html")
* [Python unittest Source Code](https://github.com/python/cpython/tree/3.5/Lib/unittest "https://github.com/python/cpython/tree/3.5/Lib/unittest")
* [Selenium Documentation](https://selenium-python.readthedocs.io "https://selenium-python.readthedocs.io")
* [Selenium - Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html "https://selenium-python.readthedocs.io/locating-elements.html")
* [Selenium - Waits](https://selenium-python.readthedocs.io/waits.html "https://selenium-python.readthedocs.io/waits.html")
* [Xpath cheatsheet](https://devhints.io/xpath "https://devhints.io/xpath")
