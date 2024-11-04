import glob, os

prefix = os.path.join('extension', 'core_functions')

include_directories = [os.path.join(prefix, x) for x in ['include']]

# Save the current working directory
current_dir = os.getcwd()

try:
    # Change to the target directory
    os.chdir(prefix)
    
    # Use glob to find the files, without root_dir
    source_files = [os.path.join(prefix, x) for x in glob.glob("**/*.cpp", recursive=True)]

finally:
    # Restore the original working directory
    os.chdir(current_dir)

