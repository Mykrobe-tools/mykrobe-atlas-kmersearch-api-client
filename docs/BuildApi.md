# kmersearch-api-client.BuildApi

All URIs are relative to *http://kmersearch-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_post**](BuildApi.md#build_post) | **POST** /build | 


# **build_post**
> Samples build_post(new_samples)



### Example

```python
from __future__ import print_function
import time
import kmersearch-api-client
from kmersearch-api-client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = kmersearch-api-client.BuildApi()
new_samples = kmersearch-api-client.NewSamples() # NewSamples | 

try:
    api_response = api_instance.build_post(new_samples)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->build_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_samples** | [**NewSamples**](NewSamples.md)|  | 

### Return type

[**Samples**](Samples.md)

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

