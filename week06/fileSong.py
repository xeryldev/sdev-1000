# fileSong.py
# read a song from a file, line by line and print it out

def main():
  print('1' * 20)
  infile = open("twelveDaysInput.txt")
 
  # echo print the contents of the file to the screen
  # read each line from the file
  for line in infile:
    #remove the linefeed at the end of the line
    toPrint = line[:-1]
    print(toPrint)

  # If you want to reprocess the contents of a file, 
  # do not close/open again. Simply reset the file pointer
  # back to the start of the file.
  infile.seek(0)  # do not change this line
  print('2' * 20)
  for line in infile:
    #TODO: 
    # - remove the linefeed at the end of the line, 
    # - then convert the line to all uppercase
    toPrint = line[:-1].upper()
    print(toPrint)

  infile.seek(0)

  print('3' * 20)
  for line in infile:
    #TODO: 
    # - remove the linefeed at the end of the line, 
    # - then center the line within 50 characters
    toPrint = line[:-1].center(50)
    print(toPrint)
  infile.seek(0)

  print('4' * 20)
  outputFilename = "formattedSong.txt"
  outfile = open("formattedSong.txt", "w")
  # TODO: change this line to open the output file for WRITING
  # outfile = ""
  for line in infile:
    #TODO: 
    # - remove the linefeed at the end of the line, 
    # - convert the line to title case
    # - center the line within 50 80 characters 
    # 
    toPrint = line[:-1].title().center(65)
    # TODO: change the following line to print to the
    # output file once you have the open statement working above
    print(toPrint)
    outfile.write(toPrint)
    
  # TODO: add a line to close the output file
  print("Song has been printed to:", outputFilename)
  outfile.close()
  infile.close()
  
main()
