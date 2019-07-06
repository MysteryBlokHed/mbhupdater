# MBH Updater
A Python script designed for frontend updating of files.
Not for use as a GIT alternative for backend programming.

## Overview
This is a fairly simple program that will copy files from online and keep the file structure. For example, if you have `/path/to/file/code.txt` and `/path/to/code.txt`, it will keep those files in those folders locally.

## Requirements
**Python v3+**  
If you don't already have it, download it [here](https://www.python.org/downloads/).  
**tqdm if you're using tqdm_updater**  
Download using `pip install tqdm`, or download the latest wheel [here](https://pypi.org/project/tqdm/#files) and use `pip install (.whl file)`.

## Documentation
### Updater class
What each class variable means.

    class Updater(object):

    def __init__(local_version_file="version.txt",
                latest_version_file="new_version.txt",
                latesturl=False, new_files=[],
                new_filesurl=True, output=True,
                source_file="", source_file_enabled=True,
                source_fileurl=True, files_offset=0)
        """
        local_version_file: The downloaded version of the software.
        Should contain a number, like 1, 1.2, 1.234.
        latest_version_file: Likely stored online. This is the latest version of the software.
        Should contain a number, like 2, 2.3, 2.345.
        latesturl: Boolean. Whether or not the file stored at latest_version_file is a url.
        new_files: Array. Contains the location of the files to update if the versions don't match.
        new_filesurl: Boolean. Whether or not the items listed in new_files are urls.
        output: Boolean. Whether or not to write to screen. Ignored for TQDMUpdater.
        source_file: (optional) The location of the source file (where all files required to pull
        are stored).
        source_file_enabled: Boolean. Whether or not to use the source file feature.
        source_fileurl: Whether or not the source file is stored online.
        files_offset: Integer. Contains the folder offset to add to URLs when pulling from online. (eg. If the url is http://files.net/files/source/file.txt, and files_offset is 1, it will be pulled into /source/file.txt. If the offset is 2, it will not be stored in an extra folder.)
        """

### Initialize the updater
##### Standard
    import mbhupdater.updater

    updater = mbhupdater.updater.Updater()
##### tqdm (Progress Bar)
    import mbhupdater.tqdm_updater

    updater = mbhupdater.tqdm_updater.TQDMUpdater()

### Pull the new files
Pull without comparing versions:  
    `updater.pull_files()`  
Pull if local version is outdated:  
    `updater.compare_and_pull()`  

When you are pulling files from online, you MUST include the `http://` or `https://` part of the URL in the sources list, otherwise there may be errors in both pulling the file from online, and writing the files locally.

### Example source file
There is an optional source file feature in the updater.
If you're using it, this is how you would format it:

    http://www.location1.com/file/file.txt
    http://files.server.net/files/code.py
    [DELETE]
    /local/path/to/file.txt
    /local/path/to/file2.txt
    /old/thing/file.txt
Make sure to include the `http://` or `https://` for online files, otherwise it will not output to the correct folder and may crash.  
Any files under the `[DELETE]` tag will be deleted instead of updated/created. The path for deletion must be a local file, not a URL.

### Getters and setters
Pretty easy to guess what they do, they just use the variable names in the functions. Here's a list:

    # Getters
    get_local_version_file()
    get_latest_version_file()
    get_latesturl_status()
    get_files_offset()
    get_new_filesurl_status()
    get_output_status()
    get_local_version()
    get_latest_version()
    get_source_file_enabled()
    get_source_fileurl_status()
    # Setters
    set_local_version_file(local_version_file)
    set_latest_version_file(latest_version_file)
    set_source_file(source_file)
    set_files_offset()
    toggle_latesturl()
    toggle_new_filesurl()
    toggle_output()
    toggle_source_file_enabled()
    toggle_source_fileurl()
All functions have descriptions that will show up in IDEs.

### Other functions
    # Other functions
    compare_versions() - Returns True if the versions match and False if the local one is out of date.
    read_files()       - Reads the content of the version files. Must use before get_local_version() or get_latest_version()
