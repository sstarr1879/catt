# -*- mode: python -*-

block_cipher = None


a = Analysis(['opencv_test.py'],
             pathex=['C:\\Users\\sarah\\Documents\\Python_Scripts\\dev_folder\\face_detection'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='opencv_test',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
