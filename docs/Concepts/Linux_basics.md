# Linux Basics

Linux is a powerful open-source operating system. As a contributor, understanding basic command-line usage is key. This guide covers essential commands, system updates, and best practices for command-line work.

---

## Basic Linux Commands

The command line is your main interface. Here are core commands you'll use often:

* **`ls` (list):** Shows directory contents.
    * `ls`: Lists files and directories in the current location.
        * _Example:_ `ls` might output `documents images myproject.txt`
    * `ls -l`: Provides a "long listing" with details like permissions, size, and date.
        * _Example:_ `ls -l` might show `-rw-r--r-- 1 user group 1024 Jul 10 10:30 myproject.txt`
    * `ls -a`: Shows all files, including hidden ones (starting with a `.`).
        * _Example:_ `ls -a` might reveal `.bashrc .config documents`
* **`cd` (change directory):** Navigates between directories.
    * `cd <directory_name>`: Moves to a specific directory.
        * _Example:_ `cd documents`
    * `cd ..`: Moves up one directory level.
        * _Example:_ If in `/home/user/documents`, `cd ..` moves to `/home/user/`
    * `cd ~`: Returns to your home directory.
        * _Example:_ No matter where you are, `cd ~` takes you to `/home/user/`
* **`pwd` (print working directory):** Displays your current directory's full path.
    * _Example:_ `pwd` might output `/home/user/myproject`
* **`mkdir` (make directory):** Creates a new directory.
    * _Example:_ `mkdir new_folder`
* **`rmdir` (remove directory):** Deletes an empty directory.
    * _Example:_ `rmdir empty_folder`
* **`touch`:** Creates an empty file or updates a file's timestamp.
    * _Example:_ `touch new_file.txt` (creates a new empty file)
* **`cp` (copy):** Copies files or directories.
    * `cp <source_file> <destination_file>`: Copies a file.
        * _Example:_ `cp report.docx report_backup.docx`
    * `cp -r <source_directory> <destination_directory>`: Copies a directory and its contents.
        * _Example:_ `cp -r myproject myproject_copy`
* **`mv` (move):** Moves or renames files/directories.
    * _Example (move):_ `mv old_file.txt documents/` (moves `old_file.txt` into the `documents` folder)
    * _Example (rename):_ `mv old_name.txt new_name.txt`
* **`rm` (remove):** Deletes files or directories.
    * `rm <file_name>`: Deletes a file.
        * _Example:_ `rm unwanted_file.txt`
    * `rm -r <directory_name>`: Recursively deletes a directory (use with extreme caution!).
        * _Example:_ `rm -r old_project_folder` (Deletes the folder and everything inside it)
* **`cat` (concatenate):** Displays a file's content.
    * _Example:_ `cat README.md` (shows the content of the README.md file)
* **`less` / `more`:** Views file content page by page for large files.
    * _Example:_ `less /var/log/syslog` (allows you to scroll through a large log file; press `q` to quit)
* **`grep`:** Searches for text patterns within files.
    * _Example:_ `grep "error" /var/log/syslog` (finds all lines containing "error" in the syslog file)
* **`man` (manual):** Provides documentation for commands.
    * _Example:_ `man ls` (shows the manual page for the `ls` command; press `q` to quit)

---

## How to Update and Upgrade the System

Keeping your system updated is vital for security and new features. For Debian-based systems (like Ubuntu), use `apt`:

* **`sudo apt update`**: Refreshes the list of available packages from repositories.
    * _Example:_ `sudo apt update` (You'll see a list of package information being downloaded)
* **`sudo apt upgrade`**: Installs newer versions of all currently installed packages.
    * _Example:_ `sudo apt upgrade` (Prompts you to confirm the installation of available updates)
* **`sudo apt full-upgrade`**: Performs a more comprehensive upgrade, installing new packages if needed for dependencies and removing obsolete ones.
    * _Example:_ `sudo apt full-upgrade` (Use for major system version upgrades or when `upgrade` is insufficient)

**To update:**

1.  Open your terminal.
2.  Run `sudo apt update`.
3.  Then, run `sudo apt upgrade`.
4.  Optionally, use `sudo apt full-upgrade` for a deeper update.

---

## How `sudo` and `apt` Work

* **`sudo` (SuperUser DO):**
    * **Function:** Allows you to run commands with **root (administrator) privileges** using *your own password*.
    * **When to use:** For tasks requiring elevated permissions, like installing software, modifying system files, or managing services.
    * **Caution:** Always be careful with `sudo`; incorrect commands can harm your system.
        * _Example:_ `sudo systemctl restart apache2` (restarts the Apache web server, requires root privileges)

* **`apt` (Advanced Package Tool):**
    * **Function:** A command-line utility for managing software packages (installing, updating, removing) on Debian-based systems. It interacts with software repositories.
    * **When to use:**
        * `apt install <package_name>`: Install new software.
            * _Example:_ `sudo apt install git` (installs the Git version control system)
        * `apt remove <package_name>`: Uninstall software (leaves configuration files).
            * _Example:_ `sudo apt remove firefox`
        * `apt purge <package_name>`: Uninstall software and its configuration files.
            * _Example:_ `sudo apt purge apache2`
        * `apt search <keyword>`: Find packages.
            * _Example:_ `apt search text editor` (lists available text editor packages)

---

## Tips for Command-Line Navigation and Safety

Here are some best practices to make your command-line work more efficient and secure:

* **Tab Completion:** Press the `Tab` key to auto-complete commands, file names, or directory names. Press `Tab` twice to see all available options if there's more than one.
* **Arrow Keys:** Use the `Up` and `Down` arrow keys to cycle through your command history. This saves typing and helps recall previous commands.
* **`Ctrl+R` (Reverse Search):** Press `Ctrl+R` and start typing to search your command history for a specific command. It's incredibly useful for finding a command you ran a while ago.
* **Read the Manual (`man`):** If you're unsure about a command or its options, use `man <command_name>` for detailed documentation. Press `q` to quit the manual.
* **Be Careful with `sudo`:** Always double-check your commands before pressing Enter when using `sudo`. Commands run with root privileges can make significant, irreversible changes to your system if executed incorrectly.
* **Backup Regularly:** Make a habit of backing up important files and configurations, especially before performing major system changes or software installations. This can save you from potential data loss.