# VeraBuster

VeraBuster is a tool for recovering passwords of VeraCrypt encrypted volumes. The script performs password brute-forcing from a specified list and checks them against the provided encrypted volume.

## Dependencies

`veracrypt`

You can install VeraCrypt on your Linux system using the following steps:

### Ubuntu

`sudo add-apt-repository ppa:unit193/encryption`
`sudo apt-get update`
`sudo apt-get install veracrypt`

### Fedora

`sudo dnf install -y veracrypt`

### Arch/Manjaro

`sudo pacman -S veracrypt`

## Usage

Run the VeraBuster.py script using Python 3.x. The script accepts the following arguments:

`-v - Path to the VeraCrypt encrypted volume.`

`-p - File containing the list of passwords for brute-forcing.`

`-d - Enable debug mode.`

Example usage:

`python VeraBuster.py -v /path/to/veracrypt/volume -p /path/to/wordlist.txt`

## Inspiration

This project has drawn significant inspiration from the [VeraCracker project](https://github.com/NorthernSec/VeraCracker) by [NorthernSec](https://github.com/NorthernSec), which provides similar functionality for cracking VeraCrypt volumes on the Linux operating system.

## License

This project is licensed under the MIT License. Please refer to the LICENSE file for more information.
