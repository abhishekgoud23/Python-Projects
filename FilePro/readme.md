FilePro is a software product that analyzes and visualizes a directory/ folder with diff files and sub-folders and does some operations like:

1. Creates a "file_info" CSV file that contains a folder summary with details of extensions, and sizes, and creates a hash based on a checksum hash technique - SHA256, filenames, file paths, and the date the file was modified on.

2. Constructor should take the path where the folder is located. Then, if the “file_info” file is not present in CWD or DOM is older than 2 days, we get the most updated version of “file_info”.

3. Generates a report on the screen with an option to save it to a file (CSV). It would contain the following information:
a. Different types of files present in the folders (including all sub-folders)
b. Mean and median size of the files (in general and by type)
c. The folder name (not including subfolders) with the largest amount of files by (i) number and
(ii) size

and Visualization of these reports in Bar graphs, Pie charts, and line chart
