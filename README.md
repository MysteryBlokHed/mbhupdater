# MBH Updater
A Python script designed for frontend updating of files.

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
                new_filesurl=True)
        """
        local_version_file: The downloaded version of the software.
        Should contain a number, like 1, 1.2, 1.234.
        latest_version_file: Likely stored online. This is the latest version of the software.
        Should contain a number, like 2, 2.3, 2.345.
        latesturl: Boolean. Whether or not the file stored at latest_version_file is a url.
        new_files: Array. Contains the location of the files to update if the versions don't match.
        new_filesurl: Boolean. Whether or not the items listed in new_files are urls.
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

### Getters and setters
Pretty easy to guess what they do, they just use the variable names in the functions. Here's a list:

    # Getters
    get_local_version_file()
    get_latest_version_file()
    get_latesturl_status()
    get_new_filesurl_status()
    get_local_version()
    get_latest_version()
    # Setters
    set_local_version_file(local_version_file)
    set_latest_version_file(latest_version_file)
    toggle_latesturl()
    toggle_new_filesurl()
All functions have descriptions that will show up in IDEs.

### Other functions
    # Other functions
    compare_versions() - Returns True if the versions match and False if the local one is out of date.
    read_files()       - Reads the content of the version files. Must use before get_local_version() or get_latest_version()