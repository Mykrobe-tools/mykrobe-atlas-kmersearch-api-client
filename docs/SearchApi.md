# kmersearch_api_client.SearchApi

All URIs are relative to *http://kmersearch-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_post**](SearchApi.md#search_post) | **POST** /search | 


# **search_post**
> SearchResults search_post(search_query)



### Example

```python
from __future__ import print_function
import time
import kmersearch_api_client
from kmersearch_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = kmersearch_api_client.SearchApi()
search_query = kmersearch_api_client.SearchQuery() # SearchQuery | 

try:
    api_response = api_instance.search_post(search_query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | [**SearchQuery**](SearchQuery.md)|  | 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request (i.e. query sequence is too short) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

