import os

def rewrite_tsx_file(file_path):
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read the contents of the file
            original_content = file.read()

        # Define the rewriting pattern
        pattern = 'import Image from "next/image";'
        replacement = 'import Image from "next/image";\nimport { useClient } from "<your-import-path>";'

        # Perform rewriting
        modified_content = original_content.replace(
            'export default function Home() {', 
            'export default function Home() {\n  useClient();'
        )

        # Insert the import statement after the existing import statements
        modified_content = modified_content.replace(pattern, replacement, 1)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

        print("File '{}' has been rewritten successfully.".format(file_path))

    except FileNotFoundError:
        print("File '{}' not found.".format(file_path))
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    # Provide the path to the TypeScript file
    file_path = input("Enter the path to the TypeScript file (page.tsx): ")

    # Check if the provided path exists and if it's a file
    if os.path.exists(file_path) and os.path.isfile(file_path) and file_path.endswith('.tsx'):
        rewrite_tsx_file(file_path)
    else:
        print("Invalid file path or file is not a TypeScript file.")
