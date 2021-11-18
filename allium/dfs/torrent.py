import os
import sys
import torf

def create_torrent(fname, comment):
    for file in fname:
        if not os.path.isfile(file):
            print(f'The file {file} doesn\'t exist')
            return -1
        torrent = torf.Torrent(file, comment=comment)
        torrent.generate()
        torrent.write(file + '.torrent')
    return 0

def main():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    print(opts)
    print(args)

    if "-f" in opts:
        torrent_created = create_torrent(args, '')
    elif "--psize" in opts:
        tor = read_tor_file(args[0])
        psize = calculate_piece_size(tor)
        print(f'The piece size is {psize}')

def calculate_piece_size(torr_file):
    return torr_file.piece_size

def read_tor_file(fname):
    tor = torf.Torrent()
    tor = tor.read(fname)
    return tor

if __name__ == "__main__":
    main()
