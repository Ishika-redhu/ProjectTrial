
import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/ishik/Downloads"

class FileEventHandler(FileSystemEventHandler):


    def on_created(self, event):
        print("Hey {event.src_path} has been created")

    def on_deleted(self, event):
        print("Oops! Someone deleted{event.src_path}")

    def on_modified(self, event):
        print("hey there ! {event.src_path} has been modifies")

    def on_moved(self, event):
        print("someone moved {event.src_path}to {event.dest_path}")
        

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
   while True:
    print("running...")
except KeyboardInterrupt:
    observer.stop()
    print("Event stopped..")
