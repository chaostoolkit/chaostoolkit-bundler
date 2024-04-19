from PyInstaller.utils.hooks import collect_data_files, collect_submodules, \
    copy_metadata

datas = copy_metadata('chaostoolkit-opentracing', recursive=True) + \
    copy_metadata('opentelemetry-api', recursive=True) + \
    copy_metadata('opentelemetry-sdk', recursive=True) + \
    copy_metadata('opentelemetry-exporter-otlp-proto-http', recursive=True) + \
    copy_metadata('opentelemetry-propagator-b3', recursive=True) + \
    copy_metadata('opentelemetry-semantic-conventions', recursive=True) + \
    copy_metadata('opentelemetry-instrumentation-httpx', recursive=True) + \
    copy_metadata('opentelemetry-instrumentation-requests', recursive=True) + \
    copy_metadata('opentelemetry-instrumentation-botocore', recursive=True) + \
    copy_metadata('opentelemetry-exporter-gcp-trace', recursive=True) + \
    copy_metadata('opentelemetry-resourcedetector-gcp', recursive=True) + \
    copy_metadata('opentelemetry-sdk-extension-aws', recursive=True) + \
    copy_metadata('opentelemetry-propagator-aws-xray', recursive=True) + \
    copy_metadata('opentelemetry-instrumentation-urllib3', recursive=True)
hiddenimports = (
    collect_submodules('chaostracing')
) + (
    collect_submodules('opentelemetry')
)