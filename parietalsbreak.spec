# -*- mode: python -*-

block_cipher = None


a = Analysis(['parietalsbreak.py'],
             pathex=['/Users/kellydodson/Documents/parietalsbreak', '/Users/kellydodson/virtualenvironment/my_new_app/bin/python'],
             binaries=[],
             datas=[],
             hiddenimports=['pygame'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
##### include mydir in distribution #######
def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, str(mydir)))

    return extra_datas
###########################################

# append the 'data' dir

a.datas += extra_datas('Fonts')
a.datas += extra_datas('girlpictures')
a.datas += extra_datas('guypictures')
a.datas += extra_datas('boypictures')
a.datas += extra_datas('backgrounds')
a.datas += extra_datas('pictures')
a.datas += extra_datas('other_resources')


print(a.datas)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='parietalsbreak',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='parietalsbreak')

app = BUNDLE(exe,
         name='myscript.app',
         icon=None,
         bundle_identifier=None)
