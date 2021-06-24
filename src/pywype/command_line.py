import pywype


def main():
    print(28 * "-", " pyWype ", 28 * "-")
    print(
        "PYTHON DISK & PARTITION WIPING UTILITY FOR GNU/LINUX."
        "\nTHIS UTILITY WILL IRRECOVERABLY WIPE DATA FROM DRIVE.\nPROCEED WITH CAUTION."
    )

    pywype.wipe_device()


if __name__ == "__main__":
    main()
