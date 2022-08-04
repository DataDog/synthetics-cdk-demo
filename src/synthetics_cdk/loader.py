from urllib.parse import urlparse

from cdktf_cdktf_provider_datadog import (
    SyntheticsTest,
    SyntheticsTestApiStep,
    SyntheticsTestApiStepAssertion,
    SyntheticsTestApiStepExtractedValue,
    SyntheticsTestApiStepExtractedValueParser,
    SyntheticsTestApiStepRequestDefinition,
    SyntheticsTestOptionsList,
    SyntheticsTestOptionsListRetry,
)


def build_tests(config, stack):
    for i, test_data in enumerate(config):
        url = urlparse(test_data["endpoint"])
        SyntheticsTest(
            stack,
            f"synthetics_test_{url.hostname}_{i}",
            locations=["aws:eu-west-3"],
            name=f"Test {url.hostname} {test_data['method']}",
            status="live",
            type="api",
            subtype="multi",
            tags=[
                "cdktf",
            ],
            options_list=SyntheticsTestOptionsList(
                accept_self_signed=False,
                allow_insecure=False,
                follow_redirects=False,
                min_failure_duration=0,
                min_location_failed=1,
                retry=SyntheticsTestOptionsListRetry(count=0, interval=300),
                tick_every=14400,
            ),
            api_step=[
                SyntheticsTestApiStep(
                    name="step",
                    subtype="http",
                    allow_failure=False,
                    assertion=[SyntheticsTestApiStepAssertion(operator="matches", target=str(test_data["status"]), type="statusCode")],
                    retry={"count": 5, "interval": 1000},
                    is_critical=True,
                    request_definition=SyntheticsTestApiStepRequestDefinition(
                        method=test_data["method"],
                        url=test_data["endpoint"],
                    ),
                ),
            ]
        )
