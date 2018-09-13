# -*- mode: python -*-

block_cipher = None


a = Analysis(['<CHAOS_PATH>'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[
                 'chaosk8s',
                 'chaosaws',
                 'chaosprometheus',
                 'chaoshumio',
                 'chaosgce',
                 'chaosspring',
                 'chaosazure',
                 'chaoscf',
                 'chaosgremlin',
                 'chaosslack',
                 'chaostoxi'
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
