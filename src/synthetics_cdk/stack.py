from cdktf import App, TerraformStack

from cdktf_cdktf_provider_datadog import DatadogProvider


def build_stack():
    app = App()
    stack = TerraformStack(app, "synthetics_cdk")
    _ = DatadogProvider(
        stack,
        id="datadog-provider",
    )
    return app, stack
