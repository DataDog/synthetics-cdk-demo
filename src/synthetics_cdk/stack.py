from cdktf import App, TerraformStack, TerraformVariable

from cdktf_cdktf_provider_datadog import DatadogProvider


def build_stack():
    app = App()
    stack = TerraformStack(app, "synthetics_cdk")
    api_key = TerraformVariable(
        stack,
        "api_key",
        type="string",
        sensitive=True,
    )
    app_key = TerraformVariable(
        stack,
        "app_key",
        type="string",
        sensitive=True,
    )
    _ = DatadogProvider(
        stack,
        id="datadog-provider",
        api_key=api_key.string_value,
        app_key=app_key.string_value,
    )
    return app, stack
