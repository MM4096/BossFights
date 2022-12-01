import os
import shutil
import sys
import zipfile
import wget
import subprocess

launcherVersionURL = "https://drive.google.com/uc?export=download&confirm=yTib&id=1NOmu4-Jhu4hIGRKi7_fGRbEXa0OjTsLG"
launcherDataURL = "https://drive.google.com/uc?export=download&confirm=yTib&id=1WTwE_DIWqARQzCFdHqlqu4af3ouKyRlZ"


def progressBar(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    # Don't use print() as it will print in new line every time.
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()


if __name__ == "__main__":
    if not os.path.exists("Data"):
        os.makedirs("Data")
    if not os.path.exists("Data/launcherVersion.txt"):
        with open("Data/launcherVersion.txt", "w") as file:
            file.write("")

    with open("Data/launcherVersion.txt", "r") as file:
        launcherVersion = file.readline()
    os.remove("Data/launcherVersion.txt")
    print("Getting latest version...")
    wget.download(launcherVersionURL, "Data", bar=progressBar)
    with open("Data/launcherVersion.txt", "r") as file:
        launcherLatestVersion = file.readline()
    if not launcherVersion == launcherLatestVersion:
        try:
            os.remove("main.py")
        except FileNotFoundError:
            pass
        print("")
        print("Updating launcher to V" + launcherLatestVersion)
        wget.download(launcherDataURL, "", bar=progressBar)
    print("")
    print("Running launcher")
