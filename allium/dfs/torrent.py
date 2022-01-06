import os
import sys
import torf

def main():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    print(opts)
    print(args)

    if "-f" in opts:
        torrent_created = create_torrent(args, '')
    elif "-h" in opts:
        help()
    elif "--psize" in opts:
        tor = read_tor_file(args[0])
        psize = calculate_piece_size(tor)
        print(f'The piece size is {psize}')

def create_torrent(fname, comment):
    for file in fname:
        if not os.path.isfile(file):
            print(f'The file {file} doesn\'t exist')
            return -1
        torrent = torf.Torrent(file, comment=comment)
        torrent.generate()
        torrent.write(file + '.torrent')
    return 0

def help():
    help_text = """Welcome to Allium, this is the distributed file sharing module (dfs).
    This software is licensed with the GPL-3+, see the License file for more info.

    You have quite a few options and flags to use here. Let's see a list of them:
    -h: help
            Print this help text
    -f: create torrent file from files
            Pass the files as arguments after the option to create a torrent
            file for each one of them.
    --psize: calculates the piece from the torrent file
            Pass the torrent file as argument after this option."""
    print(help_text)

def calculate_piece_size(torr_file):
    return torr_file.piece_size

def distribute_tor_file(torr_file):
    if not os.path.isfile(torr_file):
        print(f'The file {file} doesn\'t exist')
        return -1
    riffle_con()
    riffle_broadcast(torr_file)
    return 0

def distribute_tor_parts(torr_file):
    if not os.path.isfile(torr_file):
        print(f'The file {file} doesn\'t exist')
        return -1
    tor_parts = load_tor_parts(torr_file)
    for part in tor_parts:
        riffle_send_tor_part()
    return 0

def load_tor_parts(torr_file):
    pass

def riffle_send_tor_part():
    pass

def riffle_con():
    pass

def riffle_broadcast():
    pass

def read_tor_file(fname):
    tor = torf.Torrent()
    tor = tor.read(fname)
    return tor

if __name__ == "__main__":
    main()
