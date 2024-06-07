import pytest
import boto3
from unittest.mock import patch, MagicMock


def detect_text_resource(image_path: str):
    session = boto3.Session(profile_name='default')
    client = session.client('rekognition')
    with open(image_path, 'rb') as image_file:
        response = client.detect_text(
            Image={'Bytes': image_file.read()},
        )
    return response

def test_detect_text_resource():
    client_mock = MagicMock()
    client_mock.detect_text.return_value = {
        'TextDetections': [
            {'DetectedText': 'Hello', 'Confidence': 99.0},
            {'DetectedText': 'World', 'Confidence': 95.0}
        ]
    }

    open_mock = MagicMock()
    open_mock.return_value.__enter__.return_value.read.return_value = b'fake_image_data'

    with patch('boto3.Session') as session_mock, \
         patch('builtins.open', open_mock):
        session_mock.return_value.client.return_value = client_mock

        response = detect_text_resource('path/to/image.jpg')

    assert response == {
        'TextDetections': [
            {'DetectedText': 'Hello', 'Confidence': 99.0},
            {'DetectedText': 'World', 'Confidence': 95.0}
        ]
    }

    client_mock.detect_text.assert_called_once_with(Image={'Bytes': b'fake_image_data'})

    open_mock.assert_called_once_with('path/to/image.jpg', 'rb')


