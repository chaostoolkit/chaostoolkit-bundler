#-*- coding: utf-8 -*-
#-*- mode: python -*-
import os

block_cipher = None

chaos_path = os.environ.get('CHAOSTOOLKIT_PATH')
if not chaos_path:
    raise RuntimeError("Please point CHAOSTOOLKIT_PATH to the 'chaos' CLI location")

a = Analysis([chaos_path],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[
                 'chaosk8s',
                 'chaosaws',
                 'chaosprometheus',
                 'chaoshumio',
                 'chaosgcp',
                 'chaosspring',
                 'chaosazure',
                 'chaoscf',
                 'chaosgremlin',
                 'chaosslack',
                 'chaostoxi',
                 'chaosreliably'
             ],
             hookspath=['./hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='chaos',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
