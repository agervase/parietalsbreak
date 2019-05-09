import cx_Freeze
import os


executables = [cx_Freeze.Executable("parietalsbreak.py")]

required_files = []
required_executables = []

for root, dirs, files in os.walk(os.path.realpath("."), topdown=True, followlinks=False):
	if ".DS_Store" in dirs:
		dirs.remove(".DS_Store")
	if ".git" in dirs:
		dirs.remove (".git")
	for file in files:
		if file.endswith(".png") or file.endswith(".ttf") or file.endswith(".mp3") or file.endswith(".txt"):
			required_files.append(os.path.join(root, file))
		elif file.endswith(".py") and str(file) is not "setup.py":
			required_executables.append(cx_Freeze.Executable(os.path.join(root,file)))

cx_Freeze.setup(
    name="Parietals Break",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":required_files, 
                           'excludes': ['jinja2', 'pexpect','Tcl','tcl','tk','anaconda','anaconda2']}},
    executables = executables

    )
