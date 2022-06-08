from PyInstaller.utils.hooks import collect_data_files, collect_submodules, \
    copy_metadata

datas = copy_metadata('chaostoolkit-opentracing', recursive=True) + \
    copy_metadata('opentelemetry-api', recursive=True)
hiddenimports = (
    collect_submodules('chaostracing')
) + (
    collect_submodules('opentelemetry')
)