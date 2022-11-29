import os
import shutil
import sys
import zipfile
import wget
import subprocess

versionURL = "https://drive.google.com/uc?export=download&confirm=yTib&id=17h6tLvjUE8AT9U-kIqWQYRTddNu-gXEU"
dataURL = "https://drive.google.com/uc?export=download&confirm=yTib&id=11U7lW7WdffKjmRsvXL73rGKP_V1JwABP"


def launchGame():
    print("Launching")
    subprocess.Popen("Data/Game/Boss Fights.exe")


def progressBar(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    # Don't use print() as it will print in new line every time.
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()


def download():
    print("")
    print("Starting download. This can take a while")
    wget.download(dataURL, "Data/Game", bar=progressBar)
    print()
    print("Done!")
    print("Unzipping")
    with zipfile.ZipFile("Data/Game/Boss Fights.zip") as gameZip:
        gameZip.extractall("Data/Game")
    print("Cleaning up")
    os.remove("Data/Game/Boss Fights.zip")
    try:
        os.remove("Data/version.txt (1).txt")
    except FileNotFoundError:
        pass
    launchGame()


def deleteGame():
    print("Deleting old files")
    for filename in os.listdir("Data/Game"):
        file_path = os.path.join("Data/Game", filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    print("Done!")


if __name__ == "__main__":
    try:
        with open("Data/version.txt.txt", "r") as version:
            currentVersion = version.readline()
            print("Current Version: " + currentVersion)
        os.remove("Data/version.txt.txt")
        print("Getting Latest version")
        wget.download(versionURL, "Data/", bar=progressBar)
        with open("Data/version.txt.txt", "r") as checkVersion:
            checkVersion = checkVersion.readline()
            print("Latest Version: " + checkVersion)
        if not currentVersion == checkVersion:
            print("New version: V" + checkVersion)
            update = input("Do you want to upgrade to V" + checkVersion + "? [y/n]").lower()
            if update == "y":
                print("Updating")
                deleteGame()
                download()
            else:
                print("Launching V" + currentVersion)
                with open("Data/version.txt.txt", "w") as file:
                    file.write(currentVersion)
                launchGame()
        else:
            print("Up to date!")
            launchGame()

    except FileNotFoundError:
        if not os.path.exists("Data"):
            os.makedirs("Data")
        if not os.path.exists("Data/Game"):
            os.makedirs("Data/Game")
        wget.download(versionURL, "Data/", bar=progressBar)
        download()
