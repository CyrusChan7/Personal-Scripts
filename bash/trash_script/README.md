### A script that emulates the trash functionality found on Microsoft Windows and macOS for Linux server/GUI-less distros.

<br/>  

#### **How to use:**
1. Place this script in the user's home directory.
2. Type command `chmod +x trash_script` in the Terminal to give the script permission to execute.
3. Add alias `alias rm='~/trash_script'` to `.bashrc` file, located in the current user's home directory.
4. Type command `. .bashrc` to refresh the Bash shell and apply the alias set above.  
5. Type in `rm -d example_dir` to delete directory `example_dir`.
6. Type in `rm example_file` to delete file `example_file`.  
  
**Note: To use the "real" `rm` command, type in `"rm" example_file`.**

![](images/usage.png)
