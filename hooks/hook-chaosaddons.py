from PyInstaller.utils.hooks import collect_data_files, collect_submodules, \
    copy_metadata

datas = copy_metadata('chaostoolkit-addons', recursive=True)
hiddenimports = (
    collect_submodules('chaosaddons')
)
