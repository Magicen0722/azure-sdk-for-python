# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# Network

_REDIRECT_STATUS_CODES = (
    307,  # Temporary redirect
    308,  # Permanent redirect
)

_RETRYABLE_STATUS_CODES = (
    206,  # Partial success
    401,  # Unauthorized
    403,  # Forbidden
    408,  # Request Timeout
    429,  # Too Many Requests - retry after
    500,  # Internal Server Error
    502,  # BadGateway
    503,  # Service Unavailable
    504,  # Gateway timeout
)

_THROTTLE_STATUS_CODES = (
    402,  # Quota, too Many Requests over extended time
    439,  # Quota, too Many Requests over extended time (legacy)
)

# Statsbeat

# (OpenTelemetry metric name, Statsbeat metric name)
_ATTACH_METRIC_NAME = "Attach"
_FEATURE_METRIC_NAME = "Feature"
_REQ_EXCEPTION_NAME = ("statsbeat_exception_count", "Exception Count")
_REQ_DURATION_NAME = ("statsbeat_duration", "Request Duration")
_REQ_FAILURE_NAME = ("statsbeat_failure_count", "Request Failure Count")
_REQ_RETRY_NAME = ("statsbeat_retry_count", "Retry Count")
_REQ_SUCCESS_NAME = ("statsbeat_success_count", "Request Success Count")
_REQ_THROTTLE_NAME = ("statsbeat_throttle_count", "Throttle Count")

_STATSBEAT_METRIC_NAME_MAPPINGS = dict(
    [
        _REQ_DURATION_NAME,
        _REQ_EXCEPTION_NAME,
        _REQ_FAILURE_NAME,
        _REQ_SUCCESS_NAME,
        _REQ_RETRY_NAME,
        _REQ_THROTTLE_NAME,
    ]
)
