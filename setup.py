"""Cython build file"""
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os

UNIX = True if os.name == "posix" else False

cythonExt = []
for root, dirs, files in os.walk(os.getcwd()):
	for file in files:
		if file.endswith(".pyx") and ".pyenv" not in root:	# im sorry
			filePath = os.path.relpath(os.path.join(root, file))
			cythonExt.append(Extension(filePath.replace("\\" if not UNIX else "/", ".")[:-4], [filePath]))

setup(
	name = "lets pyx modules",
	ext_modules = cythonize(cythonExt, nthreads = 0 if not UNIX else 4),
)