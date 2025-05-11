import os

def main():
    print("Copying files...")

    # Navigate to the package directory
    os.chdir("packagename.tspackage/TSPACKAGE")  

    # Open the file and read the first line
    with open(".tsinfo", "r") as file:
        first_line = file.readline().strip()  # Read and clean line 1

    # Check if the first line starts with "Package Name: "
    if first_line.startswith("Package Name: "):
        package_name = first_line.replace("Package Name: ", "").strip()  # Extract package name

        # Move up directories correctly
        os.chdir("../../subsystem/users/ADMIN_USER/packagename.tspackage/usr")

        # Ensure the directory exists before copying
        os.makedirs(package_name, exist_ok=True)  

        # Use proper path handling for xcopy
        source_path = os.path.dirname(os.path.abspath(__file__))  
        destination_path = os.path.join(os.getcwd(), package_name)

        os.system(f'xcopy "{source_path}" "{destination_path}" /E /H /C /I')

    else:
        print("Error: First line does not contain 'Package Name: '")

if __name__ == "__main__":
    main()
    print("Copying files completed.")
    os.system("pause")
