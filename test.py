import pyappdevkit

pyappdevkit.app_info("NAME:","TEST [PROGRAM_LIBRARY_INFO]","","","","","","","","","","","","","","","","","","")

pyappdevkit.file(file_name="test.txt",file_mode="w",file_write="test1")
pyappdevkit.file(file_name="test.txt",file_mode="a",file_write="test2")
pyappdevkit.file(file_name="test.txt",file_mode="r",file_write="")