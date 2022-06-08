from PyInstaller.utils.hooks import collect_data_files, collect_submodules, \
    copy_metadata

datas = copy_metadata('chaostoolkit-opentracing', recursive=True) + \
    copy_metadata('opentelemetry-api', recursive=True) + \
    copy_metadata('opentelemetry-exporter-jaeger-proto-grpc', recursive=True) + \
    copy_metadata('opentelemetry-exporter-otlp-proto-grpc', recursive=True) + \
    copy_metadata('opentelemetry-exporter-otlp-proto-http', recursive=True) + \
    copy_metadata('opentelemetry-opentracing-shim', recursive=True) + \
    copy_metadata('opentelemetry-exporter-jaeger-thrift', recursive=True) + \
    copy_metadata('opentelemetry-propagator-b3', recursive=True) + \
    copy_metadata('opentelemetry-sdk', recursive=True)
hiddenimports = (
    collect_submodules('chaostracing')
) + (
    collect_submodules('opentelemetry')
)