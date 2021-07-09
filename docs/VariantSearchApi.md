# kmersearch-api-client.VariantSearchApi

All URIs are relative to *http://kmersearch-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variant_search_post**](VariantSearchApi.md#variant_search_post) | **POST** /variant_search | 


# **variant_search_post**
> VariantSearchResults variant_search_post(variant_search_query)



### Example

```python
from __future__ import print_function
import time
import kmersearch-api-client
from kmersearch-api-client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = kmersearch-api-client.VariantSearchApi()
variant_search_query = kmersearch-api-client.VariantSearchQuery() # VariantSearchQuery | 

try:
    api_response = api_instance.variant_search_post(variant_search_query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantSearchApi->variant_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant_search_query** | [**VariantSearchQuery**](VariantSearchQuery.md)|  | 

### Return type

[**VariantSearchResults**](VariantSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

