# Created by MysteryBlokHed in 2019.
import urllib.request
import os
import shutil

class Updater(object):
    def __init__(self, local_version_file="version.txt", latest_version_file="new_version.txt", latesturl=False, new_files=[], new_filesurl=True, output=True, source_file="", source_file_enabled=True, source_fileurl=True, files_offset=0):
        ## Verify the types of all variables
        # Verify the type of local_version_file
        if type(local_version_file) is str:
            self._local_version_file = local_version_file
        else:
            raise TypeError(f"Expected string for local_version_file, got {type(local_version_file)}.")
        # Verify the type of latest_version_file
        if type(latest_version_file) is str:
            self._latest_version_file = latest_version_file
        else:
            raise TypeError(f"Expected string for latest_version_file, got {type(latest_version_file)}.")
        # Verify the type of new_files
        if type(new_files) is list:
            self._new_files = new_files
        else:
            raise TypeError(f"Expected list for new_files, got {type(new_files)}.")
        # Verify the type of source_file
        if type(source_file) is str:
            self._source_file = source_file
        else:
            raise TypeError(f"Expected str for source_file, got {type(source_file)}.")
        # Verify the type of latesturl
        if type(latesturl) is bool:
            self._latesturl = latesturl
        else:
            raise TypeError(f"Expected boolean for latesturl, got {type(latesturl)}.")
        # Verify the type of new_filesurl
        if type(new_filesurl) is bool:
            self._new_filesurl = new_filesurl
        else:
            raise TypeError(f"Expected boolean for new_filesurl, got {type(new_filesurl)}.")
        # Verify the type of output
        if type(output) is bool:
            self._output = output
        else:
            raise TypeError(f"Expected boolean for output, got {type(output)}.")
        # Verify the type of source_file_enabled
        if type(source_file_enabled) is bool:
            self._source_file_enabled = source_file_enabled
        else:
            raise TypeError(f"Expected boolean for source_file_enabled, got {type(source_file_enabled)}.")
        # Verify the type of source_fileurl
        if type(source_fileurl) is bool:
            self._source_fileurl = source_fileurl
        else:
            raise TypeError(f"Expected boolean for source_fileurl, got {type(source_fileurl)}.")
        # Verify the type of files_offset
        if type(files_offset) is int:
            self._files_offset = files_offset
        else:
            raise TypeError(f"Expected int for files_offset, got {type(files_offset)}.")
    
    def get_local_version_file(self):
        """Returns the location of the local version file."""
        return self._local_version_file
    
    def get_latest_version_file(self):
        """Returns the location of the latest version file."""
        return self._latest_version_file
    
    def get_source_file(self):
        """Returns the location of the source file to use if the feature is enabled."""
        return self._source_file

    def get_files_offset(self):
        """Returns the amount of folders into a URL to go."""
        return self._files_offset

    def get_latesturl_status(self):
        """Returns a boolean of whether or not latest_version_file contains a URL."""
        return self._latesturl
    
    def get_new_filesurl_status(self):
        """Returns a boolean of whether or not the new files that (might) need copying are URLs."""
        return self._new_filesurl
    
    def get_output_status(self):
        """Returns a boolean of whether or not to print to screen."""
        return self._output
    
    def get_source_file_enabled(self):
        """Returns a boolean of whether or not to use the source file feature."""
        return self._source_file_enabled
    
    def get_source_fileurl_status(self):
        """Returns a boolean of whether or not the source file is stored online."""
        return self._source_fileurl
    
    def get_local_version(self):
        """Returns the version of the local files.
        Must use read_files() first."""
        return self._local_version
    
    def get_latest_version(self):
        """Returns the version of the latest files.
        Must use read_files() first."""
        return self._latest_version
    
    def set_local_version_file(self, local_version_file):
        """Set the location of the local version file."""
        # Verify the type of local_version_file
        if type(local_version_file) is str:
            self._local_version_file = local_version_file
        else:
            raise TypeError(f"Expected string for local_version_file, got {type(local_version_file)}.")
    
    def set_latest_version_file(self, latest_version_file):
        """Set the location of the latest version file."""
        # Verify the type of latest_version_file
        if type(latest_version_file) is str:
            self._latest_version_file = latest_version_file
        else:
            raise TypeError(f"Expected string for latest_version_file, got {type(latest_version_file)}.")
    
    def set_source_file(self, source_file):
        """Set the location of the source file to use if the feature is enabled."""
        # Verify the type of source_file
        if type(source_file) is str:
            self._source_file = source_file
        else:
            raise TypeError(f"Expected str for source_file, got {type(source_file)}.")
    
    def set_files_offset(self, files_offset):
        """Set the amount of folders into a URL to go."""
        # Verify the type of files_offset
        if type(files_offset) is int:
            self._files_offset = files_offset
        else:
            raise TypeError(f"Expected int for files_offset, got {type(files_offset)}.")

    def toggle_latesturl(self):
        """Toggles the boolean of whether or not latest_version_file contains a URL."""
        # Simple toggle for booleans
        self._latesturl = not self._latesturl
    
    def toggle_new_filesurl(self):
        """Toggles the boolean of whether or not the new files that (might) need copying are URLs."""
        local = open(self._local_version_file, "r")
        # Simple toggle for booleans
        self._new_filesurl = not self._new_filesurl
        
        self._local_version = local.readlines()
        local.close()
    
    def toggle_output(self):
        """Toggles the boolean of whether or not to print progress to screen."""
        # Simple toggle for booleans
        self._output = not self._output
    
    def toggle_source_file_enabled(self):
        """Toggles the boolean of whether or not to use the source file feature."""
        # Simple toggle for booleans
        self._source_file_enabled = not self._source_file_enabled
    
    def toggle_source_fileurl(self):
        """Toggles the boolean of whether or not the source file is stored online."""
        # Simple toggle for booleans
        self._source_fileurl = not self._source_fileurl
    
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
    
    def _get_source_file(self):
        if self._source_file_enabled:
            # Does different things if the source file is online or not.
            if self._source_fileurl:
                # Read the file line-by-line
                self._new_files = urllib.request.urlopen(self._source_file).readlines()
                # Convert it to be usable
                for i in range(len(self._new_files)):
                    try:
                        self._new_files[i] = self._new_files[i].decode()
                    except:
                        # Oops, it won't work :(
                        pass
            else:
                # Read the file line-by-line
                f = open(self._source_file)
                lines = f.readlines()
                for i in range(0, len(lines)):
                    if lines[i][-1:] == "\n":
                        lines[i] = lines[i][:-1]
                self._new_files = lines

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
        # Import the source file, if enabled.
        self._get_source_file()

        delete = False
        files_to_delete = []
        # Does different things if the new files are online or not.
        if self._new_filesurl:
            if self._output:
                print("Files are online.")
            # For each new file in array
            for item in self._new_files:
                # Check if the files listed should be deleted
                if item[:8] == "[DELETE]":
                    delete = True
                if not delete:
                    # Set the target location to output to
                    fname = item.split("/", 3+self._files_offset)[-1:][0]
                    # Remove line endings
                    fname = fname.strip("\n").strip("\r")
                    # Create the directories for the file if they don't exist
                    os.makedirs(os.path.dirname(fname), exist_ok=True)
                    # Read the file line-by-line
                    lines = urllib.request.urlopen(item).readlines()
                    if self._output:
                        print(f"Read file from {fname}.")
                    # Whether or not the file is stored as bytes
                    b = False
                    # Sometimes breaks, but from testing it seems fine to skip.
                    try:
                        if type(lines[0]) is bytes:
                            b = True
                    except:
                        pass
                    # Write the contents of the new file to the working directory.
                    if self._output:
                        print(f"Writing file {fname}...")
                    # Opens the file differently if it is of type bytes.
                    if b:
                        f = open(fname, "wb+")
                    else:
                        f = open(fname, "w+")
                    f.writelines(lines)
                    if self._output:
                        print(f"Wrote file {fname}.")
                else:
                    if not item[:8] == "[DELETE]":
                        files_to_delete.append(item)
        else:
            if self._output:
                print("Files are offline.")
            # For each new file in array
            for item in self._new_files:
                fname = item.split("/")[-1:][0]
                # Read the file line-by-line
                lines = open(item, "r").readlines()
                if self._output:
                    print(f"Read file from {fname}.")
                # Write the contents of the new file to the working directory.
                f = open(fname, "w+")
                f.writelines(lines)
                if self._output:
                    print(f"Wrote file {fname}.")
                f.close()
        
        # Delete the files marked
        if self._output:
            print("Deleting old files...")
        for item in files_to_delete:
            # Check if the item is a file or folder
            if item.strip("\n").strip("\r")[-1] == "/": # Remove line endings to check last character
                if os.path.isdir(item.strip("\n").strip("\r").strip("/")):
                    if self._output:
                        print(f"Deleting folder {item}...")
                    shutil.rmtree(item.strip("\n").strip("\r").strip("/"))
            else:
                if os.path.isfile("./"+item):
                    if self._output:
                        print(f"Deleting file {item}...")
                    os.remove("./"+item)
    
    def compare_and_pull(self):
        """Compares the versions. If the current version is older, it will update the current files.
        Returns True if the files were up to date, and false if the update failed/files were up to date."""
        self.read_files()

        if not self.compare_versions():
            if self._output:
                print("Outdated version detected. Updating...")
            self.pull_files()
            f = open(self._local_version_file, "w+")
            # Attempt to decode the latest version
            try:
                self._latest_version = self._latest_version.decode()
            except:
                # Oof
                pass
            f.writelines(str(self._latest_version))
            f.close()
            return True
        else:
            if self._output:
                print("Files are up to date.")
            return False