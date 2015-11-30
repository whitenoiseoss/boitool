from archive.archive import Archive
from utils.helpers import errprint, dprint
import glob
import os


class BoITool(object):
    def __init__(self):
        try:
            self.resources_path = os.environ['BOI_RESOURCES_PATH']
            if self.resources_path[-1:] is "/":
                pass
            else:
                self.resources_path = self.resources_path + "/"
        except KeyError:
            errprint("You must set $BOI_RESOUCES_PATH")
            exit(1)
        else:
            dprint(" - Using", self.resources_path, "as resources path")
        dprint("Loading archives...")
        self.archives = {}
        archive_paths = glob.glob(self.resources_path + "*.a")
        archive_paths.sort()
        if len(archive_paths) > 0:
            dprint(" - Found", str(len(archive_paths)), "archives")
            for archive in archive_paths:
                a = Archive(archive)
                self.archives[a.name] = a
