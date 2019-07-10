# Created by MysteryBlokHed in 2019.
from tqdm import tqdm
import mbhupdater.updater
import urllib.request
import os

# Subclass of normal Updater to avoid unneccessary rewriting of code.
class TQDMUpdater(mbhupdater.updater.Updater):
    def pull_files(self):
        """Not recommended unless you don't want to update the version file locally.
        Pulls all files to the working directory."""
        # Import the source file, if enabled.
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

        delete = False
        files_to_delete = []
        # Does different things if the new files are online or not.
        if self._new_filesurl:
            tqdm.write("Files are online.")
            # For each new file in array
            for i in tqdm(range(len(self._new_files))):
                if self._new_files[i][:8] == "[DELETE]":
                    delete = True
                if not delete:
                    # Set the target location to output to
                    fname = self._new_files[i].split("/", 3+self._files_offset)[-1:][0]
                    # Remove line endings
                    fname = fname.strip("\n").strip("\r")
                    # Create the directories for the file if they don't exist
                    os.makedirs(os.path.dirname(fname), exist_ok=True)
                    # Read the file line-by-line
                    lines = urllib.request.urlopen(self._new_files[i]).readlines()
                    tqdm.write(f"Read file from {fname}.")
                    # Whether or not the file is stored as bytes
                    b = False
                    # Sometimes breaks, but from testing it seems fine to skip.
                    try:
                        if type(lines[0]) is bytes:
                            b = True
                    except:
                        pass
                    # Write the contents of the new file to the working directory.
                    tqdm.write(f"\nWriting file {fname}...")
                    # Opens the file differently if it is of type bytes.
                    if b:
                        f = open(fname, "wb+")
                    else:
                        f = open(fname, "w+")
                    f.writelines(lines)
                    tqdm.write(f"Wrote file {fname}.")
                else:
                    if not self._new_files[i][:8] == "[DELETE]":
                        files_to_delete.append(self._new_files[i])
        else:
            tqdm.write("Files are offline.")
            # For each new file in array
            for i in tqdm(range(len(self._new_files))):
                fname = self._new_files[i].split("/")[-1:][0]
                # Read the file line-by-line
                lines = open(self._new_files[i], "r").readlines()
                tqdm.write(f"Read file from {fname}.")
                # Whether or not the file is stored as bytes
                b = False
                if type(lines[0]) is bytes:
                    b = True
                # Write the contents of the new file to the working directory.
                tqdm.write(f"\nWriting file from {fname}...")
                # Opens the file differently if it is of type bytes.
                if b:
                    f = open(fname, "wb+")
                else:
                    f = open(fname, "w+")
                f.writelines(lines)
                tqdm.write(f"Wrote file {fname}.")
        # Delete the files marked
        tqdm.write("Deletinng old files...")
        for i in tqdm(range(len(files_to_delete))):
            if os.path.isfile("./"+files_to_delete[i]):
                tqdm.write(f"Deleting file {files_to_delete[i]}...")
                os.remove("./"+files_to_delete[i])