import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: task cli <command> [options]")
        sys.exit(1)
    command = sys.argv[1]

    if command is 'add':
        pass
    elif command is 'list':
        pass
    elif command is 'update':
        pass
    elif command is 'delete':
        pass
    elif command in ['mark-in-progress', 'mark-done']:
        pass
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()