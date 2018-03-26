###### os module commands #####
os.path.join('/test/', 'myfile')  ->  /test/myfile
os.path.expanduser('~')	   ->	\home\calsoft
os.path.join(os.path.expanduser('~'),'dir', 'subdir', 'myfile.py')	->	/home/calsoft/dir/subdir/myfile.py
#If we use '/', it tells Python that we're using absolute path, and it overrides the path before it:
os.path.join('/test/', '/myfile.py')	->	/myfile.py
os.path.split('/home/calsoft/anil/linux-commands/commands.py')	->	('/home/calsoft/anil/linux-commands','commands.py')
os.path.splitext('/home/calsoft/anil/linux-commands/commands.py')	->	('/home/calsoft/anil/linux-commands/commands','.py')
os.path.realapth('myfile.py') -> /home/calsoft/myfile.py


##### glob module #######
# The glob module takes a wildcard and returns the path of all files and directories matching the wildcard.

glob.glob('subdir/*.py') -> ['subdir\\tes3.py', 'subdir\\test1.py', 'subdir\\test2.py']
