import os
import argparse
import stat

def change_file_attributes(file_path, read_only=None, hidden=None, system=None):
    try:
        # Get current file attributes
        attributes = os.stat(file_path).st_file_attributes

        # Set or unset read-only attribute
        if read_only is not None:
            if read_only:
                attributes |= stat.FILE_ATTRIBUTE_READONLY
            else:
                attributes &= ~stat.FILE_ATTRIBUTE_READONLY

        # Set or unset hidden attribute
        if hidden is not None:
            if hidden:
                attributes |= stat.FILE_ATTRIBUTE_HIDDEN
            else:
                attributes &= ~stat.FILE_ATTRIBUTE_HIDDEN

        # Set or unset system attribute
        if system is not None:
            if system:
                attributes |= stat.FILE_ATTRIBUTE_SYSTEM
            else:
                attributes &= ~stat.FILE_ATTRIBUTE_SYSTEM

        # Apply the new attributes
        os.chmod(file_path, attributes)
        print(f"Attributes changed for {file_path}")

    except Exception as e:
        print(f"Error changing attributes for {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Change file attributes on Windows")
    parser.add_argument("files", metavar="F", type=str, nargs="+", help="Files to change attributes for")
    parser.add_argument("--read-only", dest="read_only", action="store_true", help="Set files to read-only")
    parser.add_argument("--no-read-only", dest="read_only", action="store_false", help="Unset read-only attribute")
    parser.add_argument("--hidden", dest="hidden", action="store_true", help="Set files to hidden")
    parser.add_argument("--no-hidden", dest="hidden", action="store_false", help="Unset hidden attribute")
    parser.add_argument("--system", dest="system", action="store_true", help="Set files to system")
    parser.add_argument("--no-system", dest="system", action="store_false", help="Unset system attribute")
    parser.set_defaults(read_only=None, hidden=None, system=None)

    args = parser.parse_args()

    for file_path in args.files:
        change_file_attributes(file_path, args.read_only, args.hidden, args.system)

if __name__ == "__main__":
    main()