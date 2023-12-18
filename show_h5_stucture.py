import h5py
import argparse

def print_structure(h5file, indent=0):
    for key in h5file.keys():
        if isinstance(h5file[key], h5py.Dataset):
            print(' ' * indent + f'{key}: {h5file[key].shape}')
        else:
            print(' ' * indent + key)
            print_structure(h5file[key], indent + 4)

def main():
    parser = argparse.ArgumentParser(description='Process .h5 file.')
    parser.add_argument('--file_path', type=str, help='Path to the .h5 file')
    args = parser.parse_args()

    with h5py.File(args.file_path, 'r') as h5file:
        print_structure(h5file, indent=8)

if __name__ == "__main__":
    main()