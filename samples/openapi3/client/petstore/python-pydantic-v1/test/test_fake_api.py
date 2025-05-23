# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_api.api.fake_api import FakeApi  # noqa: E501


class TestFakeApi(unittest.TestCase):
    """FakeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FakeApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_fake_any_type_request_body(self) -> None:
        """Test case for fake_any_type_request_body

        test any type request body  # noqa: E501
        """
        pass

    def test_fake_enum_ref_query_parameter(self) -> None:
        """Test case for fake_enum_ref_query_parameter

        test enum reference query parameter  # noqa: E501
        """
        pass

    def test_fake_health_get(self) -> None:
        """Test case for fake_health_get

        Health check endpoint  # noqa: E501
        """
        pass

    def test_fake_http_signature_test(self) -> None:
        """Test case for fake_http_signature_test

        test http signature authentication  # noqa: E501
        """
        pass

    def test_fake_outer_boolean_serialize(self) -> None:
        """Test case for fake_outer_boolean_serialize

        """
        pass

    def test_fake_outer_composite_serialize(self) -> None:
        """Test case for fake_outer_composite_serialize

        """
        pass

    def test_fake_outer_number_serialize(self) -> None:
        """Test case for fake_outer_number_serialize

        """
        pass

    def test_fake_outer_string_serialize(self) -> None:
        """Test case for fake_outer_string_serialize

        """
        pass

    def test_fake_property_enum_integer_serialize(self) -> None:
        """Test case for fake_property_enum_integer_serialize

        """
        pass

    def test_fake_ref_enum_string(self) -> None:
        """Test case for fake_ref_enum_string

        test ref to enum string  # noqa: E501
        """
        pass

    def test_fake_return_boolean(self) -> None:
        """Test case for fake_return_boolean

        test returning boolean  # noqa: E501
        """
        pass

    def test_fake_return_byte_like_json(self) -> None:
        """Test case for fake_return_byte_like_json

        test byte like json  # noqa: E501
        """
        pass

    def test_fake_return_enum(self) -> None:
        """Test case for fake_return_enum

        test returning enum  # noqa: E501
        """
        pass

    def test_fake_return_enum_like_json(self) -> None:
        """Test case for fake_return_enum_like_json

        test enum like json  # noqa: E501
        """
        pass

    def test_fake_return_float(self) -> None:
        """Test case for fake_return_float

        test returning float  # noqa: E501
        """
        pass

    def test_fake_return_int(self) -> None:
        """Test case for fake_return_int

        test returning int  # noqa: E501
        """
        pass

    def test_fake_return_list_of_objects(self) -> None:
        """Test case for fake_return_list_of_objects

        test returning list of objects  # noqa: E501
        """
        pass

    def test_fake_return_str_like_json(self) -> None:
        """Test case for fake_return_str_like_json

        test str like json  # noqa: E501
        """
        pass

    def test_fake_return_string(self) -> None:
        """Test case for fake_return_string

        test returning string  # noqa: E501
        """
        pass

    def test_fake_uuid_example(self) -> None:
        """Test case for fake_uuid_example

        test uuid example  # noqa: E501
        """
        pass

    def test_test_additional_properties_reference(self) -> None:
        """Test case for test_additional_properties_reference

        test referenced additionalProperties  # noqa: E501
        """
        pass

    def test_test_body_with_binary(self) -> None:
        """Test case for test_body_with_binary

        """
        pass

    def test_test_body_with_file_schema(self) -> None:
        """Test case for test_body_with_file_schema

        """
        pass

    def test_test_body_with_query_params(self) -> None:
        """Test case for test_body_with_query_params

        """
        pass

    def test_test_client_model(self) -> None:
        """Test case for test_client_model

        To test \"client\" model  # noqa: E501
        """
        pass

    def test_test_date_time_query_parameter(self) -> None:
        """Test case for test_date_time_query_parameter

        """
        pass

    def test_test_empty_and_non_empty_responses(self) -> None:
        """Test case for test_empty_and_non_empty_responses

        test empty and non-empty responses  # noqa: E501
        """
        pass

    def test_test_endpoint_parameters(self) -> None:
        """Test case for test_endpoint_parameters

        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트   # noqa: E501
        """
        pass

    def test_test_error_responses_with_model(self) -> None:
        """Test case for test_error_responses_with_model

        test error responses with model  # noqa: E501
        """
        pass

    def test_test_group_parameters(self) -> None:
        """Test case for test_group_parameters

        Fake endpoint to test group parameters (optional)  # noqa: E501
        """
        pass

    def test_test_inline_additional_properties(self) -> None:
        """Test case for test_inline_additional_properties

        test inline additionalProperties  # noqa: E501
        """
        pass

    def test_test_inline_freeform_additional_properties(self) -> None:
        """Test case for test_inline_freeform_additional_properties

        test inline free-form additionalProperties  # noqa: E501
        """
        pass

    def test_test_json_form_data(self) -> None:
        """Test case for test_json_form_data

        test json serialization of form data  # noqa: E501
        """
        pass

    def test_test_object_for_multipart_requests(self) -> None:
        """Test case for test_object_for_multipart_requests

        """
        pass

    def test_test_query_parameter_collection_format(self) -> None:
        """Test case for test_query_parameter_collection_format

        """
        pass

    def test_test_string_map_reference(self) -> None:
        """Test case for test_string_map_reference

        test referenced string map  # noqa: E501
        """
        pass

    def test_upload_file_with_additional_properties(self) -> None:
        """Test case for upload_file_with_additional_properties

        uploads a file and additional properties using multipart/form-data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
