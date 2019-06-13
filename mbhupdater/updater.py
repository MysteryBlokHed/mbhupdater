# Created by MysteryBlokHed in 2019.
import urllib.request
import os

class Updater(object):
    # Location of the local version file
    _local_version_file = ""
    # Location of the latest version file
    _latest_version_file = ""
    # If the latest update file is online or not
    _latesturl = False

    _local_version = ""
    _latest_version = ""

    _new_files = []

    _new_filesurl = True

    def __init__(self, local_version_file="version.txt", latest_version_file="new_version.txt", latesturl=False, new_files=[], new_filesurl=True):
        # Verify the type of local_version_file
        if type(local_version_file) is str:
            self._local_version_file = local_version_file
        else:
            raise TypeError("Expected string for local_version_file, got {}.".format(type(local_version_file)))
        # Verify the type of latest_version_file
        if type(latest_version_file) is str:
            self._latest_version_file = latest_version_file
        else:
            raise TypeError("Expected string for latest_version_file, got {}.".format(type(latest_version_file)))
        # Verify the type of latesturl
        if type(latesturl) is bool:
            self._latesturl = latesturl
        else:
            raise TypeError("Expected boolean for latesturl, got {}.".format(type(latesturl)))
        # Verify the type of new_files
        if type(new_files) is list:
            self._new_files = new_files
        else:
            raise TypeError("Expected list for new_files, got {}.".format(type(new_files)))
        # Verify the type of new_filesurl
        if type(new_filesurl) is bool:
            self._new_filesurl = new_filesurl
        else:
            raise TypeError("Expected boolean for new_filesurl, got {}.".format(type(new_filesurl)))
    
    def get_local_version_file(self):
        """Returns the location of the local version file."""
        return self._local_version_file
    
    def get_latest_version_file(self):
        """Returns the location of the latest version file."""
        return self._latest_version_file
    
    def get_latesturl_status(self):
        """Returns a boolean of whether or not latest_version_file contains a URL."""
        return self._latesturl
    
    def get_new_filesurl_status(self):
        """Returns a boolean of whether or not the new files that (might) need copying are URLs."""
        return self._new_filesurl
    
    def get_local_version(self):
        """Returns the version of the local files.
        Must use read_files() first."""
        return self._local_version
    
    def get_local_version(self):
        """Returns the version of the latest files.
        Must use read_files() first."""
        return self._latest_version
    
    def set_local_version_file(self, local_version_file):
        """Set the location of the local version file."""
        # Verify the type of local_version_file
        if type(local_version_file) is str:
            self._local_version_file = local_version_file
        else:
            raise TypeError("Expected string for local_version_file, got {}.".format(type(local_version_file)))
    
    def set_latest_version_file(self, latest_version_file):
        """Set the location of the latest version file."""
        # Verify the type of latest_version_file
        if type(latest_version_file) is str:
            self._latest_version_file = latest_version_file
        else:
            raise TypeError("Expected string for latest_version_file, got {}.".format(type(latest_version_file)))
    
    def toggle_latesturl(self):
        """Toggles the boolean of whether or not latest_version_file contains a URL."""
        # Simple toggle for booleans
        self._latesturl = not self._latesturl
    
    def toggle_new_filesurl(self):
        """Toggles the boolean of whether or not the new files that (might) need copying are URLs."""
        # Simple toggle for booleans
        self._new_filesurl = not self._new_filesurl
        
        self._local_version = local.readlines()
        local.close()
    
    def read_files(self):
        """Reads the version files to ready them for comparison.
        Not neccessary unless you need to use the get_local_version() or get_latest_version() functions."""
        local = open(self._local_version_file, "r")
        
        # Does different things if the latest version file is a url or not.
        if self._latesturl:
            latest = urllib.request.urlopen(self._latest_version_file)
            self._latest_version = latest.readlines()[0]
        else:
            latest = open(self._latest_version_file, "r")
            self._latest_version = latest.readlines()[0]
            latest.close()
        
        self._local_version = local.readlines()[0]
        local.close()
    
    def compare_versions(self):
        """Returns True if the versions match, and False if they don't. Throws an error if the local version is newer."""
        self.read_files()

        if float(self._latest_version) == float(self._local_version):
            return True
        elif float(self._latest_version) > float(self._local_version):
            return False
        else:
            raise ValueError("Local version is newer than the latest version listed, consider updating the latest version file.")

    def pull_files(self):
        """Not recommended unless you don't want to update the version file locally.
        Pulls all files to the working directory."""
        # Does different things if the new files are online or not.
        if self._new_filesurl:
            print("Files are online.")
            i = 0
            # For each new file in array
            for item in self._new_files:
                # Set the target location to output to
                fname = item.split("/", 3)[-1:][0]
                # Create the directories for the file if they don't exist
                os.makedirs(os.path.dirname(fname), exist_ok=True)
                # Read the file line-by-line
                lines = urllib.request.urlopen(item).readlines()
                print("Read file from {}".format(fname))
                # Whether or not the file is stored as bytes
                b = False
                # Sometimes breaks, but from testing it seems fine to skip.
                try:
                    if type(lines[0]) is bytes:
                        print("{} is of type bytes.".format(fname))
                        b = True
                except:
                    pass
                # Write the contents of the new file to the working directory.
                print("\nWriting file {}...".format(fname))
                # Opens the file differently if it is of type bytes.
                if b:
                    f = open(fname, "wb+")
                else:
                    f = open(fname, "w+")
                f.writelines(lines)
                print("Wrote file {}.".format(fname))
                i+=1
        else:
            print("Files are offline.")
            i = 0
            # For each new file in array
            for item in self._new_files:
                fname = item.split("/")[-1:][0]
                # Read the file line-by-line
                lines = open(item, "r").readlines()
                print("Read file from {}".format(fname))
                # Write the contents of the new file to the working directory.

                f = open(fname, "w+")
                f.writelines(lines)
                print("Wrote file {}.".format(fname))
                f.close()
    
    def compare_and_pull(self):
        """Compares the versions. If the current version is older, it will update the current files."""
        self.read_files()

        if not self.compare_versions():
            print("Outdated version detected. Updating...")
            self.pull_files()
            f = open(self._local_version_file, "w+")
            f.writelines(self._latest_version)
            f.close()
        else:
            print("Files are up to date.")