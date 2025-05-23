# \FakeAPI

All URIs are relative to *http://petstore.swagger.io:80/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**FakeHealthGet**](FakeAPI.md#FakeHealthGet) | **Get** /fake/health | Health check endpoint
[**FakeOuterBooleanSerialize**](FakeAPI.md#FakeOuterBooleanSerialize) | **Post** /fake/outer/boolean | 
[**FakeOuterCompositeSerialize**](FakeAPI.md#FakeOuterCompositeSerialize) | **Post** /fake/outer/composite | 
[**FakeOuterNumberSerialize**](FakeAPI.md#FakeOuterNumberSerialize) | **Post** /fake/outer/number | 
[**FakeOuterStringSerialize**](FakeAPI.md#FakeOuterStringSerialize) | **Post** /fake/outer/string | 
[**GetParameterNameMapping**](FakeAPI.md#GetParameterNameMapping) | **Get** /fake/parameter-name-mapping | parameter name mapping test
[**TestAdditionalPropertiesReference**](FakeAPI.md#TestAdditionalPropertiesReference) | **Post** /fake/additionalProperties-reference | test referenced additionalProperties
[**TestBodyWithFileSchema**](FakeAPI.md#TestBodyWithFileSchema) | **Put** /fake/body-with-file-schema | 
[**TestBodyWithQueryParams**](FakeAPI.md#TestBodyWithQueryParams) | **Put** /fake/body-with-query-params | 
[**TestClientModel**](FakeAPI.md#TestClientModel) | **Patch** /fake | To test \&quot;client\&quot; model
[**TestEndpointParameters**](FakeAPI.md#TestEndpointParameters) | **Post** /fake | Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 
[**TestEnumParameters**](FakeAPI.md#TestEnumParameters) | **Get** /fake | To test enum parameters
[**TestGroupParameters**](FakeAPI.md#TestGroupParameters) | **Delete** /fake | Fake endpoint to test group parameters (optional)
[**TestInlineAdditionalProperties**](FakeAPI.md#TestInlineAdditionalProperties) | **Post** /fake/inline-additionalProperties | test inline additionalProperties
[**TestInlineFreeformAdditionalProperties**](FakeAPI.md#TestInlineFreeformAdditionalProperties) | **Post** /fake/inline-freeform-additionalProperties | test inline free-form additionalProperties
[**TestJsonFormData**](FakeAPI.md#TestJsonFormData) | **Get** /fake/jsonFormData | test json serialization of form data
[**TestQueryDeepObject**](FakeAPI.md#TestQueryDeepObject) | **Get** /fake/deep_object_test | 
[**TestQueryDeepObjectAnyof**](FakeAPI.md#TestQueryDeepObjectAnyof) | **Get** /fake/deep_object_anyof_test | 
[**TestQueryParameterCollectionFormat**](FakeAPI.md#TestQueryParameterCollectionFormat) | **Put** /fake/test-query-parameters | 
[**TestStringMapReference**](FakeAPI.md#TestStringMapReference) | **Post** /fake/stringMap-reference | test referenced string map
[**TestUniqueItemsHeaderAndQueryParameterCollectionFormat**](FakeAPI.md#TestUniqueItemsHeaderAndQueryParameterCollectionFormat) | **Put** /fake/test-unique-parameters | 



## FakeHealthGet

> HealthCheckResult FakeHealthGet(ctx).Execute()

Health check endpoint

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FakeAPI.FakeHealthGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.FakeHealthGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FakeHealthGet`: HealthCheckResult
	fmt.Fprintf(os.Stdout, "Response from `FakeAPI.FakeHealthGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiFakeHealthGetRequest struct via the builder pattern


### Return type

[**HealthCheckResult**](HealthCheckResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FakeOuterBooleanSerialize

> bool FakeOuterBooleanSerialize(ctx).Body(body).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	body := true // bool | Input boolean as post body (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FakeAPI.FakeOuterBooleanSerialize(context.Background()).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.FakeOuterBooleanSerialize``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FakeOuterBooleanSerialize`: bool
	fmt.Fprintf(os.Stdout, "Response from `FakeAPI.FakeOuterBooleanSerialize`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiFakeOuterBooleanSerializeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool** | Input boolean as post body | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FakeOuterCompositeSerialize

> OuterComposite FakeOuterCompositeSerialize(ctx).OuterComposite(outerComposite).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	outerComposite := *openapiclient.NewOuterComposite() // OuterComposite | Input composite as post body (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FakeAPI.FakeOuterCompositeSerialize(context.Background()).OuterComposite(outerComposite).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.FakeOuterCompositeSerialize``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FakeOuterCompositeSerialize`: OuterComposite
	fmt.Fprintf(os.Stdout, "Response from `FakeAPI.FakeOuterCompositeSerialize`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiFakeOuterCompositeSerializeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outerComposite** | [**OuterComposite**](OuterComposite.md) | Input composite as post body | 

### Return type

[**OuterComposite**](OuterComposite.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FakeOuterNumberSerialize

> float32 FakeOuterNumberSerialize(ctx).Body(body).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	body := float32(8.14) // float32 | Input number as post body (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FakeAPI.FakeOuterNumberSerialize(context.Background()).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.FakeOuterNumberSerialize``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FakeOuterNumberSerialize`: float32
	fmt.Fprintf(os.Stdout, "Response from `FakeAPI.FakeOuterNumberSerialize`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiFakeOuterNumberSerializeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **float32** | Input number as post body | 

### Return type

**float32**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FakeOuterStringSerialize

> string FakeOuterStringSerialize(ctx).Body(body).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	body := "body_example" // string | Input string as post body (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FakeAPI.FakeOuterStringSerialize(context.Background()).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.FakeOuterStringSerialize``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FakeOuterStringSerialize`: string
	fmt.Fprintf(os.Stdout, "Response from `FakeAPI.FakeOuterStringSerialize`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiFakeOuterStringSerializeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **string** | Input string as post body | 

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetParameterNameMapping

> GetParameterNameMapping(ctx).UnderscoreType(underscoreType).Type_(type_).TypeWithUnderscore(typeWithUnderscore).HttpDebugOption(httpDebugOption).Execute()

parameter name mapping test

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	underscoreType := int64(789) // int64 | _type
	type_ := "type__example" // string | type
	typeWithUnderscore := "typeWithUnderscore_example" // string | type_
	httpDebugOption := "httpDebugOption_example" // string | http debug option (to test parameter naming option)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.GetParameterNameMapping(context.Background()).UnderscoreType(underscoreType).Type_(type_).TypeWithUnderscore(typeWithUnderscore).HttpDebugOption(httpDebugOption).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.GetParameterNameMapping``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetParameterNameMappingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underscoreType** | **int64** | _type | 
 **type_** | **string** | type | 
 **typeWithUnderscore** | **string** | type_ | 
 **httpDebugOption** | **string** | http debug option (to test parameter naming option) | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestAdditionalPropertiesReference

> TestAdditionalPropertiesReference(ctx).RequestBody(requestBody).Execute()

test referenced additionalProperties



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	requestBody := map[string]interface{}{"key": interface{}(123)} // map[string]interface{} | request body

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestAdditionalPropertiesReference(context.Background()).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestAdditionalPropertiesReference``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestAdditionalPropertiesReferenceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | **map[string]interface{}** | request body | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestBodyWithFileSchema

> TestBodyWithFileSchema(ctx).FileSchemaTestClass(fileSchemaTestClass).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	fileSchemaTestClass := *openapiclient.NewFileSchemaTestClass() // FileSchemaTestClass | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestBodyWithFileSchema(context.Background()).FileSchemaTestClass(fileSchemaTestClass).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestBodyWithFileSchema``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestBodyWithFileSchemaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileSchemaTestClass** | [**FileSchemaTestClass**](FileSchemaTestClass.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestBodyWithQueryParams

> TestBodyWithQueryParams(ctx).Query(query).User(user).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	query := "query_example" // string | 
	user := *openapiclient.NewUser() // User | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestBodyWithQueryParams(context.Background()).Query(query).User(user).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestBodyWithQueryParams``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestBodyWithQueryParamsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **string** |  | 
 **user** | [**User**](User.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestClientModel

> Client TestClientModel(ctx).Client(client).Execute()

To test \"client\" model



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	client := *openapiclient.NewClient() // Client | client model

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FakeAPI.TestClientModel(context.Background()).Client(client).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestClientModel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestClientModel`: Client
	fmt.Fprintf(os.Stdout, "Response from `FakeAPI.TestClientModel`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestClientModelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**Client**](Client.md) | client model | 

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestEndpointParameters

> TestEndpointParameters(ctx).Number(number).Double(double).PatternWithoutDelimiter(patternWithoutDelimiter).Byte_(byte_).Integer(integer).Int32_(int32_).Int64_(int64_).Float(float).String_(string_).Binary(binary).Date(date).DateTime(dateTime).Password(password).Callback(callback).Execute()

Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	number := float32(8.14) // float32 | None
	double := float64(1.2) // float64 | None
	patternWithoutDelimiter := "patternWithoutDelimiter_example" // string | None
	byte_ := string(BYTE_ARRAY_DATA_HERE) // string | None
	integer := int32(56) // int32 | None (optional)
	int32_ := int32(56) // int32 | None (optional)
	int64_ := int64(789) // int64 | None (optional)
	float := float32(3.4) // float32 | None (optional)
	string_ := "string__example" // string | None (optional)
	binary := os.NewFile(1234, "some_file") // *os.File | None (optional)
	date := time.Now() // string | None (optional)
	dateTime := time.Now() // time.Time | None (optional)
	password := "password_example" // string | None (optional)
	callback := "callback_example" // string | None (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestEndpointParameters(context.Background()).Number(number).Double(double).PatternWithoutDelimiter(patternWithoutDelimiter).Byte_(byte_).Integer(integer).Int32_(int32_).Int64_(int64_).Float(float).String_(string_).Binary(binary).Date(date).DateTime(dateTime).Password(password).Callback(callback).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestEndpointParameters``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestEndpointParametersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **float32** | None | 
 **double** | **float64** | None | 
 **patternWithoutDelimiter** | **string** | None | 
 **byte_** | **string** | None | 
 **integer** | **int32** | None | 
 **int32_** | **int32** | None | 
 **int64_** | **int64** | None | 
 **float** | **float32** | None | 
 **string_** | **string** | None | 
 **binary** | ***os.File** | None | 
 **date** | **string** | None | 
 **dateTime** | **time.Time** | None | 
 **password** | **string** | None | 
 **callback** | **string** | None | 

### Return type

 (empty response body)

### Authorization

[http_basic_test](../README.md#http_basic_test)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestEnumParameters

> TestEnumParameters(ctx).EnumHeaderStringArray(enumHeaderStringArray).EnumHeaderString(enumHeaderString).EnumQueryStringArray(enumQueryStringArray).EnumQueryString(enumQueryString).EnumQueryInteger(enumQueryInteger).EnumQueryDouble(enumQueryDouble).EnumFormStringArray(enumFormStringArray).EnumFormString(enumFormString).Execute()

To test enum parameters



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	enumHeaderStringArray := []string{"EnumHeaderStringArray_example"} // []string | Header parameter enum test (string array) (optional)
	enumHeaderString := "enumHeaderString_example" // string | Header parameter enum test (string) (optional) (default to "-efg")
	enumQueryStringArray := []string{"EnumQueryStringArray_example"} // []string | Query parameter enum test (string array) (optional)
	enumQueryString := "enumQueryString_example" // string | Query parameter enum test (string) (optional) (default to "-efg")
	enumQueryInteger := int32(56) // int32 | Query parameter enum test (double) (optional)
	enumQueryDouble := float64(1.2) // float64 | Query parameter enum test (double) (optional)
	enumFormStringArray := []string{"Inner_example"} // []string | Form parameter enum test (string array) (optional) (default to "$")
	enumFormString := "enumFormString_example" // string | Form parameter enum test (string) (optional) (default to "-efg")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestEnumParameters(context.Background()).EnumHeaderStringArray(enumHeaderStringArray).EnumHeaderString(enumHeaderString).EnumQueryStringArray(enumQueryStringArray).EnumQueryString(enumQueryString).EnumQueryInteger(enumQueryInteger).EnumQueryDouble(enumQueryDouble).EnumFormStringArray(enumFormStringArray).EnumFormString(enumFormString).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestEnumParameters``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestEnumParametersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enumHeaderStringArray** | **[]string** | Header parameter enum test (string array) | 
 **enumHeaderString** | **string** | Header parameter enum test (string) | [default to &quot;-efg&quot;]
 **enumQueryStringArray** | **[]string** | Query parameter enum test (string array) | 
 **enumQueryString** | **string** | Query parameter enum test (string) | [default to &quot;-efg&quot;]
 **enumQueryInteger** | **int32** | Query parameter enum test (double) | 
 **enumQueryDouble** | **float64** | Query parameter enum test (double) | 
 **enumFormStringArray** | **[]string** | Form parameter enum test (string array) | [default to &quot;$&quot;]
 **enumFormString** | **string** | Form parameter enum test (string) | [default to &quot;-efg&quot;]

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestGroupParameters

> TestGroupParameters(ctx).RequiredStringGroup(requiredStringGroup).RequiredBooleanGroup(requiredBooleanGroup).RequiredInt64Group(requiredInt64Group).StringGroup(stringGroup).BooleanGroup(booleanGroup).Int64Group(int64Group).Execute()

Fake endpoint to test group parameters (optional)



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	requiredStringGroup := int32(56) // int32 | Required String in group parameters
	requiredBooleanGroup := true // bool | Required Boolean in group parameters
	requiredInt64Group := int64(789) // int64 | Required Integer in group parameters
	stringGroup := int32(56) // int32 | String in group parameters (optional)
	booleanGroup := true // bool | Boolean in group parameters (optional)
	int64Group := int64(789) // int64 | Integer in group parameters (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestGroupParameters(context.Background()).RequiredStringGroup(requiredStringGroup).RequiredBooleanGroup(requiredBooleanGroup).RequiredInt64Group(requiredInt64Group).StringGroup(stringGroup).BooleanGroup(booleanGroup).Int64Group(int64Group).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestGroupParameters``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestGroupParametersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requiredStringGroup** | **int32** | Required String in group parameters | 
 **requiredBooleanGroup** | **bool** | Required Boolean in group parameters | 
 **requiredInt64Group** | **int64** | Required Integer in group parameters | 
 **stringGroup** | **int32** | String in group parameters | 
 **booleanGroup** | **bool** | Boolean in group parameters | 
 **int64Group** | **int64** | Integer in group parameters | 

### Return type

 (empty response body)

### Authorization

[bearer_test](../README.md#bearer_test)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestInlineAdditionalProperties

> TestInlineAdditionalProperties(ctx).RequestBody(requestBody).Execute()

test inline additionalProperties



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	requestBody := map[string]string{"key": "Inner_example"} // map[string]string | request body

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestInlineAdditionalProperties(context.Background()).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestInlineAdditionalProperties``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestInlineAdditionalPropertiesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | **map[string]string** | request body | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestInlineFreeformAdditionalProperties

> TestInlineFreeformAdditionalProperties(ctx).TestInlineFreeformAdditionalPropertiesRequest(testInlineFreeformAdditionalPropertiesRequest).Execute()

test inline free-form additionalProperties



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	testInlineFreeformAdditionalPropertiesRequest := *openapiclient.NewTestInlineFreeformAdditionalPropertiesRequest() // TestInlineFreeformAdditionalPropertiesRequest | request body

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestInlineFreeformAdditionalProperties(context.Background()).TestInlineFreeformAdditionalPropertiesRequest(testInlineFreeformAdditionalPropertiesRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestInlineFreeformAdditionalProperties``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestInlineFreeformAdditionalPropertiesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testInlineFreeformAdditionalPropertiesRequest** | [**TestInlineFreeformAdditionalPropertiesRequest**](TestInlineFreeformAdditionalPropertiesRequest.md) | request body | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestJsonFormData

> TestJsonFormData(ctx).Param(param).Param2(param2).Execute()

test json serialization of form data



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	param := "param_example" // string | field1
	param2 := "param2_example" // string | field2

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestJsonFormData(context.Background()).Param(param).Param2(param2).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestJsonFormData``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestJsonFormDataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param** | **string** | field1 | 
 **param2** | **string** | field2 | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestQueryDeepObject

> TestQueryDeepObject(ctx).TestPet(testPet).InputOptions(inputOptions).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	testPet := *openapiclient.NewPet("doggie", []string{"PhotoUrls_example"}) // Pet |  (optional)
	inputOptions := *openapiclient.NewCategory("Name_example") // Category |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestQueryDeepObject(context.Background()).TestPet(testPet).InputOptions(inputOptions).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestQueryDeepObject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestQueryDeepObjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testPet** | [**Pet**](Pet.md) |  | 
 **inputOptions** | [**Category**](Category.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestQueryDeepObjectAnyof

> TestQueryDeepObjectAnyof(ctx).Filter(filter).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	filter := *openapiclient.NewFilterAny() // FilterAny |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestQueryDeepObjectAnyof(context.Background()).Filter(filter).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestQueryDeepObjectAnyof``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestQueryDeepObjectAnyofRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**FilterAny**](FilterAny.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestQueryParameterCollectionFormat

> TestQueryParameterCollectionFormat(ctx).Pipe(pipe).Ioutil(ioutil).Http(http).Url(url).Context(context).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	pipe := []string{"Inner_example"} // []string | 
	ioutil := []string{"Inner_example"} // []string | 
	http := []string{"Inner_example"} // []string | 
	url := []string{"Inner_example"} // []string | 
	context := []string{"Inner_example"} // []string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestQueryParameterCollectionFormat(context.Background()).Pipe(pipe).Ioutil(ioutil).Http(http).Url(url).Context(context).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestQueryParameterCollectionFormat``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestQueryParameterCollectionFormatRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipe** | **[]string** |  | 
 **ioutil** | **[]string** |  | 
 **http** | **[]string** |  | 
 **url** | **[]string** |  | 
 **context** | **[]string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestStringMapReference

> TestStringMapReference(ctx).RequestBody(requestBody).Execute()

test referenced string map



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	requestBody := map[string]string{"key": "Inner_example"} // map[string]string | request body

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FakeAPI.TestStringMapReference(context.Background()).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestStringMapReference``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestStringMapReferenceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | **map[string]string** | request body | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestUniqueItemsHeaderAndQueryParameterCollectionFormat

> []Pet TestUniqueItemsHeaderAndQueryParameterCollectionFormat(ctx).QueryUnique(queryUnique).HeaderUnique(headerUnique).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	queryUnique := []string{"Inner_example"} // []string | 
	headerUnique := []string{"Inner_example"} // []string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FakeAPI.TestUniqueItemsHeaderAndQueryParameterCollectionFormat(context.Background()).QueryUnique(queryUnique).HeaderUnique(headerUnique).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FakeAPI.TestUniqueItemsHeaderAndQueryParameterCollectionFormat``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestUniqueItemsHeaderAndQueryParameterCollectionFormat`: []Pet
	fmt.Fprintf(os.Stdout, "Response from `FakeAPI.TestUniqueItemsHeaderAndQueryParameterCollectionFormat`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTestUniqueItemsHeaderAndQueryParameterCollectionFormatRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryUnique** | **[]string** |  | 
 **headerUnique** | **[]string** |  | 

### Return type

[**[]Pet**](Pet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

